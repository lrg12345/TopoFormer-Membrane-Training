"""Verify reproduced TopoFormer predictions against a reference CSV."""

from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal


def main() -> None:
    """Compare the generated OATP1B3 summary with its reference."""
    reference_path = Path("results/1b3_example_summary.csv")
    reproduced_path = Path("results/1b3_reproduced_summary.csv")

    reference = pd.read_csv(reference_path)
    reproduced = pd.read_csv(reproduced_path)

    assert_frame_equal(
        reproduced,
        reference,
        check_exact=False,
        rtol=1e-10,
        atol=1e-12,
    )

    print("PASS: Reproduced OATP1B3 output matches the reference.")


if __name__ == "__main__":
    main()
