from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_existing_participant():
    response = client.delete(
        "/activities/Chess Club/unregister?email=michael@mergington.edu"
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Unregistered michael@mergington.edu from Chess Club"
    }
    assert "michael@mergington.edu" not in client.get("/activities").json()["Chess Club"]["participants"]


def test_unregister_missing_participant_returns_404():
    response = client.delete(
        "/activities/Chess Club/unregister?email=missing@mergington.edu"
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found"}
