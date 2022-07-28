from enum import Enum
from typing import Optional

from pydantic import BaseSettings, Field

from conf2env.convert import COLS


def get_settings():
    return [
        simple_settings(),
        simple_settings_case_sensitive(),
        simple_settings_prefix(),
        nested_settings(),
        nested_settings_delimitr(),
    ]


def simple_settings():

    class ExampleEnum(Enum):
        A = 'A'
        B = 'B'

    class SimpleSettings(BaseSettings):
        enum: ExampleEnum
        enum2: ExampleEnum = ExampleEnum.A
        a: str
        b: int = 1
        c: Optional[list] = Field(None, description='c', example=[1, 2, 3])
        d: tuple = Field((1, 2), title='d', description='abc')
        env: str = Field(None, description='env', example='env', env=['test_env', 'env'])

    _table = [
        ['ENUM', '', ExampleEnum, 'Any of: A; B', '-'],
        ['ENUM2', '', ExampleEnum, 'Any of: A; B', 'A'],
        ['A', '', str, '', '-'],
        ['B', '', int, 1, 1],
        ['C', 'c', list, [1, 2, 3], None],
        ['D', 'abc', tuple, (1, 2), (1, 2)],
        ['Any of TEST_ENV; ENV', 'env', str, 'env', None],
    ]
    table = []
    for row in _table:
        table.append(dict(zip(COLS, row)))
    markdown = """
| Name                 | Description | Type        | Example      | Default |
| -------------------- | ----------- | ----------- | ------------ | ------- |
| ENUM                 |             | ExampleEnum | Any of: A; B | -       |
| ENUM2                |             | ExampleEnum | Any of: A; B | A       |
| A                    |             | str         |              | -       |
| B                    |             | int         | 1            | 1       |
| C                    | c           | list        | 1,2,3        | None    |
| D                    | abc         | tuple       | 1,2          | (1, 2)  |
| Any of TEST_ENV; ENV | env         | str         | env          | None    |
"""
    markdown = markdown.lstrip()
    return SimpleSettings, table, markdown

def simple_settings_case_sensitive():

    class SimpleSettings(BaseSettings):
        a: str
        b: int = 1
        C: Optional[list] = Field(None, description='c', example=[1, 2, 3])
        D: tuple = Field((1, 2), title='d', description='abc')
        env: str = Field(None, description='env', example='env', env=['test_env', 'env'])

        class Config:
            case_sensitive = True

    _table = [
        ['a', '', str, '', '-'],
        ['b', '', int, 1, 1],
        ['C', 'c', list, [1, 2, 3], None],
        ['D', 'abc', tuple, (1, 2), (1, 2)],
        ['Any of test_env; env', 'env', str, 'env', None],
    ]
    table = []
    for row in _table:
        table.append(dict(zip(COLS, row)))
    markdown = """
| Name                 | Description | Type  | Example | Default |
| -------------------- | ----------- | ----- | ------- | ------- |
| a                    |             | str   |         | -       |
| b                    |             | int   | 1       | 1       |
| C                    | c           | list  | 1,2,3   | None    |
| D                    | abc         | tuple | 1,2     | (1, 2)  |
| Any of test_env; env | env         | str   | env     | None    |
"""
    markdown = markdown.lstrip()
    return SimpleSettings, table, markdown


def simple_settings_prefix():

    class SimpleSettings(BaseSettings):
        a: str
        b: int = 1
        c: Optional[list] = Field(None, description='c', example=[1, 2, 3])
        d: tuple = Field((1, 2), title='d', description='abc')
        env: str = Field(None, description='env', example='env', env=['test_env', 'env'])

        class Config:
            env_prefix = 'TEST_'

    _table = [
        ['TEST_A', '', str, '', '-'],
        ['TEST_B', '', int, 1, 1],
        ['TEST_C', 'c', list, [1, 2, 3], None],
        ['TEST_D', 'abc', tuple, (1, 2), (1, 2)],
        ['Any of TEST_ENV; ENV', 'env', str, 'env', None],
    ]
    table = []
    for row in _table:
        table.append(dict(zip(COLS, row)))
    markdown = """
| Name                 | Description | Type  | Example | Default |
| -------------------- | ----------- | ----- | ------- | ------- |
| TEST_A               |             | str   |         | -       |
| TEST_B               |             | int   | 1       | 1       |
| TEST_C               | c           | list  | 1,2,3   | None    |
| TEST_D               | abc         | tuple | 1,2     | (1, 2)  |
| Any of TEST_ENV; ENV | env         | str   | env     | None    |
"""
    markdown = markdown.lstrip()
    return SimpleSettings, table, markdown


def nested_settings():

    class NestedSettings(BaseSettings):
        e: str
        f: Optional[list] = Field(None, description='f', example=[1, 2, 3])

    class SimpleSettings(BaseSettings):
        a: str
        b: int = 1
        c: Optional[list] = Field(None, description='c', example=[1, 2, 3])
        d: tuple = Field((1, 2), title='d', description='abc')
        nested: NestedSettings
        env: str = Field(None, description='env', example='env', env=['test_env', 'env'])

    _table = [
        ['A', '', str, '', '-'],
        ['B', '', int, 1, 1],
        ['C', 'c', list, [1, 2, 3], None],
        ['D', 'abc', tuple, (1, 2), (1, 2)],
        ['E', '', str, '', '-'],
        ['F', 'f', list, [1, 2, 3], None],
        ['Any of TEST_ENV; ENV', 'env', str, 'env', None],
    ]
    table = []
    for row in _table:
        table.append(dict(zip(COLS, row)))
    markdown = """
| Name                 | Description | Type  | Example | Default |
| -------------------- | ----------- | ----- | ------- | ------- |
| A                    |             | str   |         | -       |
| B                    |             | int   | 1       | 1       |
| C                    | c           | list  | 1,2,3   | None    |
| D                    | abc         | tuple | 1,2     | (1, 2)  |
| E                    |             | str   |         | -       |
| F                    | f           | list  | 1,2,3   | None    |
| Any of TEST_ENV; ENV | env         | str   | env     | None    |
"""
    markdown = markdown.lstrip()
    return SimpleSettings, table, markdown


def nested_settings_delimitr():

    class NestedSettings(BaseSettings):
        e: str
        f: Optional[list] = Field(None, description='f', example=[1, 2, 3])

    class SimpleSettings(BaseSettings):
        a: str
        b: int = 1
        c: Optional[list] = Field(None, description='c', example=[1, 2, 3])
        d: tuple = Field((1, 2), title='d', description='abc')
        nested: NestedSettings
        env: str = Field(None, description='env', example='env', env=['test_env', 'env'])

        class Config:
            env_nested_delimiter = "_"

    _table = [
        ['A', '', str, '', '-'],
        ['B', '', int, 1, 1],
        ['C', 'c', list, [1, 2, 3], None],
        ['D', 'abc', tuple, (1, 2), (1, 2)],
        ['NESTED_E', '', str, '', '-'],
        ['NESTED_F', 'f', list, [1, 2, 3], None],
        ['Any of TEST_ENV; ENV', 'env', str, 'env', None],
    ]
    table = []
    for row in _table:
        table.append(dict(zip(COLS, row)))
    markdown = """
| Name                 | Description | Type  | Example | Default |
| -------------------- | ----------- | ----- | ------- | ------- |
| A                    |             | str   |         | -       |
| B                    |             | int   | 1       | 1       |
| C                    | c           | list  | 1,2,3   | None    |
| D                    | abc         | tuple | 1,2     | (1, 2)  |
| NESTED_E             |             | str   |         | -       |
| NESTED_F             | f           | list  | 1,2,3   | None    |
| Any of TEST_ENV; ENV | env         | str   | env     | None    |
"""
    markdown = markdown.lstrip()
    return SimpleSettings, table, markdown
