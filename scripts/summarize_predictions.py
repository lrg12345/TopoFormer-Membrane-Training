"""Command-line tool for summarizing TopoFormer prediction CSV files."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from topoformer_membrane.analysis import summarize_predictions


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Aggregate structure-level TopoFormer predictions into "
            "ligand-level summary statistics."
        )
    )
    parser.add_argument(
        "input_csv",
        type=Path,
        help="Path to a raw TopoFormer prediction CSV.",
    )
    parser.add_argument(
        "output_csv",
        type=Path,
        help="Path for the ligand-level summary CSV.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the prediction-summary workflow."""
    args = parse_args()

    predictions = pd.read_csv(args.input_csv)
    summary = summarize_predictions(predictions)

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output_csv, index=False)

    print(f"Read {len(predictions)} structure-level predictions.")
    print(f"Summarized {len(summary)} transporter-ligand pairs.")
    print(f"Wrote summary to: {args.output_csv}")


if __name__ == "__main__":
    main()
