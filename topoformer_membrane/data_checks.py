"""Utilities for checking TopoFormer dataset splits."""

__all__ = ["find_split_overlap"]


def find_split_overlap(train_ids: list[str], test_ids: list[str]) -> set[str]:
    """Return identifiers that occur in both training and test sets.

    Args:
        train_ids: Identifiers assigned to the training set.
        test_ids: Identifiers assigned to the test set.

    Returns:
        Identifiers present in both input collections.
    """
    return set(train_ids) & set(test_ids)