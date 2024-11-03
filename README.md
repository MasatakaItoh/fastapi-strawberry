# fastapi-strawberry

## Run

```
docker-compose up
```

API Documentation: http://localhost:8000/docs

## Format Code

```
make format
```

use: https://docs.astral.sh/ruff/

## Migration

```
poetry run alembic revision --autogenerate -m "message"
poetry run alembic upgrade head
```