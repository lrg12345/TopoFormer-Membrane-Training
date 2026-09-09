"""Top-level package exports for TopoFormer membrane-training utilities."""

from importlib.metadata import PackageNotFoundError, version

from . import data_checks as _api
from .data_checks import *  # noqa: F401,F403

__all__ = list(_api.__all__)

try:
    __version__ = version("topoformer_membrane")
except PackageNotFoundError:
    __version__ = "0.0.0"