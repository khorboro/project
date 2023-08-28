from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()


@app.get('/healthcheck/')
async def healthcheck():
    return "I'm OK!"


@app.get('/sumofnumbers/')
async def sumofnumbers(num1: int, num2: int):
    return num1 + num2

client = TestClient(app)


def test_healthcheck():
    response = client.get('/healthcheck/')
    assert response.status_code == 200
    assert response.text == '"I\'m OK!"'


def test_sumofnumbers():
    response = client.get('/sumofnumbers/', params={'num1': 5, 'num2': 10})
    assert response.status_code == 200
    assert response.json() == 15
