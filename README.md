# NumbersAPI Client - Python client for numbersapi.com

Python API client to interact with numbersapi.com

## Supported Features

This Python Client supports almost all features from the numbersapi.com JSON API, except batch requests.

Available request types:

* `math`
* `trivia`
* `year`
* `date`

Available query options:

* `fragment`
* `default`
* `min & max`
* `notfound (floor & ceil)`

## Installation

You can install the latest version from PyPI:

```bash
pip install numbersapi-client
```

## Usage Example

```python
>>> from numbersapi_client import NumbersAPIClient

>>> client = NumbersAPIClient()
>>> result = client.trivia()

>>> result
NumberResponse(text='587 is the outgoing port for email message submission.', number=587, found=True, type='trivia')
>>> result.number
587
```