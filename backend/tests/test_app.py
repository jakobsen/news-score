from litestar import Litestar
from litestar.testing import TestClient


def test_successful_result(test_client: TestClient[Litestar]) -> None:
    payload = {
        "measurements": [
            {"type": "TEMP", "value": 39},
            {"type": "HR", "value": 43},
            {"type": "RR", "value": 19},
        ]
    }
    response = test_client.post("/calculate-score", json=payload)
    assert response.status_code == 201
    assert response.json() == {"score": 2}


def test_parsing_error(test_client: TestClient[Litestar]) -> None:
    payload = {"measurements": []}
    response = test_client.post("/calculate-score", json=payload)
    assert response.status_code == 400
