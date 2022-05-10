from pydantic import BaseSettings


class Settings(BaseSettings):
    test: str
    test2: str = '123'
