import pytest
from numbersapi_client import __version__
from numbersapi_client.client import NumbersAPIClient
from numbersapi_client.response_types import NumberResponse


@pytest.fixture()
def client():
    return NumbersAPIClient()


@pytest.fixture()
def client_fragment():
    return NumbersAPIClient(fragment=True)


@pytest.fixture()
def client_default():
    return NumbersAPIClient(default="This number is boring")


def test_trivia(client):
    number = 42
    response = client.trivia(number)
    assert response.number == number


def test_number_response(client):
    response = client.trivia()
    assert isinstance(response, NumberResponse)


def test_fragment_option(client_fragment):
    response = client_fragment.trivia()
    text = response.text
    assert isinstance(text[0], str)


def test_default_option(client_default):
    response = client_default.trivia(-999)
    assert response.text == "This number is boring"
