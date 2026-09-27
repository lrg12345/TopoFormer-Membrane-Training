"""Analysis utilities for TopoFormer inference output."""

import pandas as pd


def parse_prediction_id(pdbid: str) -> tuple[str, str, int]:
    """Parse a TopoFormer prediction identifier.

    Parameters
    ----------
    pdbid
        Identifier in the form ``TRANSPORTER_LIGAND_AF3_REPLICATE``.

    Returns
    -------
    tuple[str, str, int]
        Transporter name, ligand name, and AF3 replicate number.

    Raises
    ------
    ValueError
        If the identifier does not match the expected format.
    """
    try:
        prefix, replicate = pdbid.rsplit("_AF3_", 1)
        transporter, ligand = prefix.split("_", 1)
        return transporter, ligand, int(replicate)
    except (ValueError, AttributeError) as exc:
        raise ValueError(
            f"Invalid TopoFormer prediction identifier: {pdbid!r}"
        ) from exc


def summarize_predictions(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate structure-level TopoFormer predictions by ligand.

    Parameters
    ----------
    df
        DataFrame containing ``pdbid``, ``pK_predicted``,
        ``t_prep_s``, and ``t_inf_s`` columns.

    Returns
    -------
    pandas.DataFrame
        One row per transporter-ligand pair with prediction and runtime
        summary statistics.

    Raises
    ------
    ValueError
        If required columns are missing.
    """
    required = {"pdbid", "pK_predicted", "t_prep_s", "t_inf_s"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    parsed = df["pdbid"].apply(parse_prediction_id)

    working = df.copy()
    working[["transporter", "ligand", "replicate"]] = pd.DataFrame(
        parsed.tolist(),
        index=working.index,
    )

    summary = (
        working.groupby(["transporter", "ligand"], as_index=False)
        .agg(
            n_structures=("pK_predicted", "size"),
            mean_pK=("pK_predicted", "mean"),
            median_pK=("pK_predicted", "median"),
            std_pK=("pK_predicted", "std"),
            min_pK=("pK_predicted", "min"),
            max_pK=("pK_predicted", "max"),
            mean_prep_s=("t_prep_s", "mean"),
            mean_inf_s=("t_inf_s", "mean"),
        )
        .sort_values(["transporter", "ligand"])
        .reset_index(drop=True)
    )

    return summary
