"""Test module for members routes."""

import pytest
from fastapi.testclient import TestClient


@pytest.mark.usefixtures("override_dependencies")
class TestMembersRoutes:
    """Tests pour les routes des membres."""

    def test_get_members(self, client : TestClient):
        """Test de la récupération de tous les membres."""
        response = client.get("/members/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        for member in data:
            assert "id_membre" in member
            assert "id_geniALE" in member
            assert "id_departement" in member

