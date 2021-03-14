import pytest
from numbersapi_client import __version__
from numbersapi_client.client import NumbersAPIClient
from numbersapi_client.exceptions import InvalidInput
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


def test_min_max_option():
    client = NumbersAPIClient(min=10, max=20)
    response = client.trivia()
    assert 10 <= response.number <= 20


def test_invalid_number(client):
    with pytest.raises(InvalidInput):
        client.trivia("wrong input")


def test_invalid_min():
    with pytest.raises(InvalidInput):
        client = NumbersAPIClient(min="wrong input")
