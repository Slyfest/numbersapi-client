from typing import Any, Dict

import requests

from numbersapi_client.enums import NotFoundOption
from numbersapi_client.exceptions import *
from numbersapi_client.response_types import NumberResponse


class NumbersAPIClient:
    BASE_URL = "http://numbersapi.com"
    params = {"json": True}

    def __init__(
        self,
        fragment: bool = False,
        default: str = None,
        min: int = None,
        max: int = None,
        notfound: NotFoundOption = None,
    ) -> None:
        if fragment:
            self.params["fragment"] = True

        if default:
            self.params["default"] = default

        if min:
            if not isinstance(min, int):
                raise InvalidOption(f"min option should be int, got {type(min)}")
            self.params["min"] = min

        if max:
            if not isinstance(max, int):
                raise InvalidOption(f"max option should be int, got {type(max)}")
            self.params["max"] = max

        if notfound:
            try:
                self.params["notfound"] = NotFoundOption(notfound).value
            except ValueError:
                raise InvalidOption(f"notfound option should be floor or ceil, got {notfound}")

    def __make_request(self, number: str, type: str) -> Dict[str, Any]:
        response = requests.get(f"{self.BASE_URL}/{number}/{type}", params=self.params)
        return response.json()

    def trivia(self, number: int = None) -> NumberResponse:
        if not number:
            number = "random"
        elif not isinstance(number, int):
            raise InvalidInput(f"number should be int, got {type(number)}")

        result = self.__make_request(number, type="trivia")
        return NumberResponse(**result)
