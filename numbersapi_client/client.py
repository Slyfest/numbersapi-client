from typing import Any, Dict

import requests


class NumbersAPIClient:
    BASE_URL = "http://numbersapi.com"
    params = {"json": True}

    def __init__(self) -> None:
        pass

    def __make_request(self, number: str, type: str) -> Dict[str, Any]:
        response = requests.get(f"{self.BASE_URL}/{number}/{type}", params=self.params)
        return response.json()

    def trivia(self, number: int = None) -> Dict[str, Any]:
        if not number:
            number = "random"
        result = self.__make_request(number, type="trivia")
        return result


test_num = 42
numbersapi_client = NumbersAPIClient()

result = numbersapi_client.trivia(test_num)
print(result)

result = numbersapi_client.trivia()
print(result)
