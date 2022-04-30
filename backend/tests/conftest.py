import os
import sys

import pytest
from fastapi.testclient import TestClient

# this is to include backend dir in sys.path so that we can import from main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
from main import app

# Read more about fixtures: https://docs.pytest.org/en/6.2.x/fixture.html


@pytest.fixture()
def client():
    return TestClient(app)
