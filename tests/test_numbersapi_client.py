import pytest
from numbersapi_client import __version__
from numbersapi_client.client import NumbersAPIClient
from numbersapi_client.exceptions import *
from numbersapi_client.response_types import NumberResponse


@pytest.fixture()
def client():
    return NumbersAPIClient()


def test_trivia(client):
    number = 42
    response = client.trivia(number)
    assert response.number == number


def test_number_response(client):
    response = client.trivia()
    assert isinstance(response, NumberResponse)


def test_fragment_option():
    client = NumbersAPIClient(fragment=True)
    response = client.trivia()
    assert isinstance(response.text[0], str)


def test_default_option():
    client = NumbersAPIClient(default="This number is boring")
    response = client.trivia(-1000)
    assert response.text == "This number is boring"


def test_min_max_option():
    client = NumbersAPIClient(min=10, max=20)
    response = client.trivia()
    assert 10 <= response.number <= 20


def test_notfound_floor_option():
    client = NumbersAPIClient(notfound="floor")
    response = client.trivia(-1000)
    assert response.number == "-Infinity"


def test_notfound_ceil_option():
    client = NumbersAPIClient(notfound="ceil")
    response = client.trivia(-1000)
    assert response.number == "0"


def test_invalid_number(client):
    with pytest.raises(InvalidInput):
        client.trivia("wrong input")


def test_invalid_min():
    with pytest.raises(InvalidOption):
        client = NumbersAPIClient(min="wrong input")


def test_invalid_notfound_option():
    with pytest.raises(InvalidOption):
        client = NumbersAPIClient(notfound="wrong input")
