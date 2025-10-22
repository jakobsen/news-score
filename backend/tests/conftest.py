from typing import Iterator

import pytest
from litestar import Litestar
from litestar.testing import TestClient

from app.app import app

app.debug = True


@pytest.fixture
def test_client() -> Iterator[TestClient[Litestar]]:
    with TestClient(app=app) as client:
        yield client
