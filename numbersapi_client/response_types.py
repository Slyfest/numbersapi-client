from dataclasses import dataclass


@dataclass
class NumberResponse:
    text: str
    number: int
    found: bool
    type: str


@dataclass
class YearResponse(NumberResponse):
    date: str = None
