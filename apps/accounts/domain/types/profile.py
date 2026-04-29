from typing import TypedDict


class CreateProfileInput(TypedDict):
    username: str
    first_name: str
    last_name: str
    gender: str
    email: str
    nationality: str
    birth_date: str | None
    phone_number: str | None
    skills: list[str]
    password: str
    linkedIn: str | None
    github: str | None