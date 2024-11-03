.PHONY: format

format:
	poetry run black .
	poetry run ruff check . --fix
