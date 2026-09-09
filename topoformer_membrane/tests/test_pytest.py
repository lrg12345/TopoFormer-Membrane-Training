"""Tests for TopoFormer membrane-training utilities."""

from topoformer_membrane import find_split_overlap


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