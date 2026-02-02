# ApiGeniALE

Le repo de la database générale du club étudiant brassicole GéniALE.

La GeneralDB est la base de donnée général de GéniALE.
La PLCDB est la base de donnée du PLC.

## Installation de uv et des technologie utilisé

### 1. Installer uv

[uv](https://docs.astral.sh/uv/getting-started/installation/)

#### Sous Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

#### Sous windows

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Installation des technologies utilisé

- `uv sync`

## Technologies utilisées

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pytest](https://docs.pytest.org/)
