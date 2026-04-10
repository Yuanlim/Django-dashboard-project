from typing import TypedDict


class CreateProfileInput(TypedDict):
    first_name: str
    middle_name: str | None
    last_name: str
    gender: str
    nationality: str
    birth_date: str | None
    phone_number: str | None
    skills: list[str]