from typing import Optional

from pydantic import BaseModel, BaseSettings, Field


class NestedSettings(BaseSettings):
    e: str
    f: Optional[list] = Field(None, description='f', example=[1, 2, 3])

class NestedModel(BaseModel):
    t: str

    class Config:
        env_prefix = "MODEL_"


class SimpleSettings(BaseSettings):
    a: str
    b: int = 1
    c: Optional[list] = Field(None, description='c', example=[1, 2, 3])
    d: tuple = Field((1, 2), title='d', description='abc')
    nested: NestedSettings
    env: str = Field(None,
                     description='env',
                     example='env',
                     env=['test_env', 'env'])

