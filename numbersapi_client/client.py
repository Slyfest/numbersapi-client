from typing import Any, Dict

import requests

from numbersapi_client.response_types import NumberResponse


class NumbersAPIClient:
    BASE_URL = "http://numbersapi.com"
    params = {"json": True}

    def __init__(self, fragment: bool = False, default: str = None) -> None:
        if fragment:
            self.params["fragment"] = True

        if default:
            self.params["default"] = default

    def __make_request(self, number: str, type: str) -> Dict[str, Any]:
        response = requests.get(f"{self.BASE_URL}/{number}/{type}", params=self.params)
        return response.json()

    def trivia(self, number: int = None) -> NumberResponse:
        if not number:
            number = "random"
        result = self.__make_request(number, type="trivia")
        return NumberResponse(**result)
