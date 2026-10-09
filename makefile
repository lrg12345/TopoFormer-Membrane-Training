# CMSE Project Commands
#
# Run:
#     make help
#
# after activating your environment.

PACKAGE = topoformer_membrane

help:
	@echo ""
	@echo "Available commands:"
	@echo ""
	@echo "  make init       Create/update environment"
	@echo "  make lint       Check code with Ruff"
	@echo "  make format     Format code with Ruff"
	@echo "  make test       Run tests"
	@echo "  make validate   Run reference workflow validation"
	@echo "  make type       Run MyPy"
	@echo "  make docs       Build documentation"
	@echo "  make check      Run lint and tests"
	@echo "  make clean      Remove generated files"
	@echo ""

init:
	conda env create --prefix=./.envs -f environment.yml || \
	conda env update --prefix=./.envs -f environment.yml --prune

lint:
	ruff check .

format:
	ruff format .

test:
	pytest -v

validate:
	pytest -v topoformer_membrane/tests/test_pytest.py::test_reference_oatp1b3_workflow

type:
	mypy $(PACKAGE)

docs:
	rm -rf docs
	pdoc -o docs $(PACKAGE)

check: lint test

check-full: lint type test

clean:
	rm -rf docs
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +

.PHONY: help init lint format test validate type docs check check-full clean
