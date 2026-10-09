"""Tests for TopoFormer membrane-training utilities."""

from pathlib import Path

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from topoformer_membrane import find_split_overlap
from topoformer_membrane.analysis import (
    parse_prediction_id,
    summarize_predictions,
)


def test_find_split_overlap_detects_shared_ids() -> None:
    """Shared identifiers should be returned."""
    train_ids = ["1abc", "2def", "3ghi"]
    test_ids = ["3ghi", "4jkl"]

    assert find_split_overlap(train_ids, test_ids) == {"3ghi"}


def test_find_split_overlap_returns_empty_set() -> None:
    """Non-overlapping splits should return an empty set."""
    train_ids = ["1abc", "2def"]
    test_ids = ["3ghi", "4jkl"]

    assert find_split_overlap(train_ids, test_ids) == set()


def test_find_split_overlap_removes_duplicates() -> None:
    """Repeated identifiers should only appear once in the result."""
    train_ids = ["1abc", "1abc", "2def"]
    test_ids = ["1abc", "1abc"]

    assert find_split_overlap(train_ids, test_ids) == {"1abc"}


def test_parse_prediction_id() -> None:
    """Parse transporter, ligand, and replicate from a valid identifier."""
    result = parse_prediction_id("1B3_17-b-estradiol_AF3_51")

    assert result == ("1B3", "17-b-estradiol", 51)


def test_parse_prediction_id_handles_long_ligand_name() -> None:
    """Ligand names should be preserved between transporter and AF3 fields."""
    result = parse_prediction_id(
        "1B3_5-carboxyfluoresceindiacetate_AF3_74"
    )

    assert result == ("1B3", "5-carboxyfluoresceindiacetate", 74)


def test_parse_prediction_id_rejects_invalid_format() -> None:
    """Malformed identifiers should raise ValueError."""
    with pytest.raises(ValueError):
        parse_prediction_id("bad_identifier")


def test_summarize_predictions_aggregates_by_ligand() -> None:
    """Replicate-level predictions should collapse to one row per ligand."""
    df = pd.DataFrame(
        {
            "pdbid": [
                "1B3_ligandA_AF3_1",
                "1B3_ligandA_AF3_2",
                "1B3_ligandB_AF3_1",
            ],
            "pK_predicted": [5.0, 7.0, 4.0],
            "t_prep_s": [10.0, 14.0, 8.0],
            "t_inf_s": [1.0, 3.0, 2.0],
        }
    )

    summary = summarize_predictions(df)

    assert len(summary) == 2

    ligand_a = summary.loc[summary["ligand"] == "ligandA"].iloc[0]

    assert ligand_a["transporter"] == "1B3"
    assert ligand_a["n_structures"] == 2
    assert ligand_a["mean_pK"] == 6.0
    assert ligand_a["median_pK"] == 6.0
    assert ligand_a["min_pK"] == 5.0
    assert ligand_a["max_pK"] == 7.0
    assert ligand_a["mean_prep_s"] == 12.0
    assert ligand_a["mean_inf_s"] == 2.0


def test_summarize_predictions_tracks_incomplete_replicates() -> None:
    """The output should report the number of predictions actually present."""
    df = pd.DataFrame(
        {
            "pdbid": [
                "1B3_ligandA_AF3_1",
                "1B3_ligandA_AF3_2",
                "1B3_ligandA_AF3_3",
            ],
            "pK_predicted": [5.0, 5.5, 6.0],
            "t_prep_s": [10.0, 10.0, 10.0],
            "t_inf_s": [1.0, 1.0, 1.0],
        }
    )

    summary = summarize_predictions(df)

    assert summary.loc[0, "n_structures"] == 3


def test_summarize_predictions_rejects_missing_columns() -> None:
    """Missing TopoFormer output columns should raise ValueError."""
    df = pd.DataFrame(
        {
            "pdbid": ["1B3_ligandA_AF3_1"],
            "pK_predicted": [5.0],
        }
    )

    with pytest.raises(ValueError):
        summarize_predictions(df)





def test_reference_oatp1b3_workflow() -> None:
    """Reference OATP1B3 example should reproduce the committed summary."""
    repo_root = Path(__file__).resolve().parents[2]

    input_path = repo_root / "examples" / "1b3_example_predictions.csv"
    expected_path = repo_root / "results" / "1b3_example_summary.csv"

    predictions = pd.read_csv(input_path)
    expected = pd.read_csv(expected_path)

    observed = summarize_predictions(predictions)

    assert len(predictions) == 28
    assert len(observed) == 3

    assert_frame_equal(
        observed,
        expected,
        check_exact=False,
        rtol=1e-10,
        atol=1e-12,
    )
