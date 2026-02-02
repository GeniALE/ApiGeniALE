"""Pytest configuration and fixtures."""

import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    """Fournit un client TestClient pour les tests."""
    return TestClient(app)


@pytest.fixture
def override_dependencies():
    """Fixture pour les dépendances à surcharger."""
    pass
