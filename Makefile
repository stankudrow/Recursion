ALGO_DIR := algorithms
ALGO_PYTHON_DIR := ${ALGO_DIR}/Python

.PHONY: pycheck pytest

pycheck:
	black ${ALGO_PYTHON_DIR} --line-length=80
	mypy ${ALGO_PYTHON_DIR}
	ruff check ${ALGO_PYTHON_DIR} --fix

pytest:
	python3 -m pytest ${ALGO_PYTHON_DIR} -vvv
