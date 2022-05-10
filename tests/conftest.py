from enum import Enum
from typing import Optional

from pydantic import BaseSettings, Field

from conf2env import COLS


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

    _table = [
        ['ENUM', '', ExampleEnum, 'A; B', '-'],
        ['ENUM2', '', ExampleEnum, 'A; B', 'A'],
        ['A', '', str, '', '-'],
        ['B', '', int, 1, 1],
        ['C', 'c', list, [1, 2, 3], None],
        ['D', 'abc', tuple, (1, 2), (1, 2)],
    ]
    table = []
    for row in _table:
        table.append(dict(zip(COLS, row)))
    markdown = """
| Name  | Description | Type        | Example | Default |
| ----- | ----------- | ----------- | ------- | ------- |
| ENUM  |             | ExampleEnum | A; B    | -       |
| ENUM2 |             | ExampleEnum | A; B    | A       |
| A     |             | str         |         | -       |
| B     |             | int         | 1       | 1       |
| C     | c           | list        | 1,2,3   | None    |
| D     | abc         | tuple       | 1,2     | (1, 2)  |
"""
    markdown = markdown.lstrip()
    return SimpleSettings, table, markdown


def simple_settings_case_sensitive():

    class SimpleSettings(BaseSettings):
        a: str
        b: int = 1
        C: Optional[list] = Field(None, description='c', example=[1, 2, 3])
        D: tuple = Field((1, 2), title='d', description='abc')

        class Config:
            case_sensitive = True

    _table = [
        ['a', '', str, '', '-'],
        ['b', '', int, 1, 1],
        ['C', 'c', list, [1, 2, 3], None],
        ['D', 'abc', tuple, (1, 2), (1, 2)],
    ]
    table = []
    for row in _table:
        table.append(dict(zip(COLS, row)))
    markdown = """
| Name | Description | Type  | Example | Default |
| ---- | ----------- | ----- | ------- | ------- |
| a    |             | str   |         | -       |
| b    |             | int   | 1       | 1       |
| C    | c           | list  | 1,2,3   | None    |
| D    | abc         | tuple | 1,2     | (1, 2)  |
"""
    markdown = markdown.lstrip()
    return SimpleSettings, table, markdown


def simple_settings_prefix():

    class SimpleSettings(BaseSettings):
        a: str
        b: int = 1
        c: Optional[list] = Field(None, description='c', example=[1, 2, 3])
        d: tuple = Field((1, 2), title='d', description='abc')

        class Config:
            env_prefix = 'TEST_'

    _table = [
        ['TEST_A', '', str, '', '-'],
        ['TEST_B', '', int, 1, 1],
        ['TEST_C', 'c', list, [1, 2, 3], None],
        ['TEST_D', 'abc', tuple, (1, 2), (1, 2)],
    ]
    table = []
    for row in _table:
        table.append(dict(zip(COLS, row)))
    markdown = """
| Name   | Description | Type  | Example | Default |
| ------ | ----------- | ----- | ------- | ------- |
| TEST_A |             | str   |         | -       |
| TEST_B |             | int   | 1       | 1       |
| TEST_C | c           | list  | 1,2,3   | None    |
| TEST_D | abc         | tuple | 1,2     | (1, 2)  |
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

    _table = [
        ['A', '', str, '', '-'],
        ['B', '', int, 1, 1],
        ['C', 'c', list, [1, 2, 3], None],
        ['D', 'abc', tuple, (1, 2), (1, 2)],
        ['E', '', str, '', '-'],
        ['F', 'f', list, [1, 2, 3], None],
    ]
    table = []
    for row in _table:
        table.append(dict(zip(COLS, row)))
    markdown = """
| Name | Description | Type  | Example | Default |
| ---- | ----------- | ----- | ------- | ------- |
| A    |             | str   |         | -       |
| B    |             | int   | 1       | 1       |
| C    | c           | list  | 1,2,3   | None    |
| D    | abc         | tuple | 1,2     | (1, 2)  |
| E    |             | str   |         | -       |
| F    | f           | list  | 1,2,3   | None    |
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

        class Config:
            env_nested_delimiter = "_"

    _table = [
        ['A', '', str, '', '-'],
        ['B', '', int, 1, 1],
        ['C', 'c', list, [1, 2, 3], None],
        ['D', 'abc', tuple, (1, 2), (1, 2)],
        ['NESTED_E', '', str, '', '-'],
        ['NESTED_F', 'f', list, [1, 2, 3], None],
    ]
    table = []
    for row in _table:
        table.append(dict(zip(COLS, row)))
    markdown = """
| Name     | Description | Type  | Example | Default |
| -------- | ----------- | ----- | ------- | ------- |
| A        |             | str   |         | -       |
| B        |             | int   | 1       | 1       |
| C        | c           | list  | 1,2,3   | None    |
| D        | abc         | tuple | 1,2     | (1, 2)  |
| NESTED_E |             | str   |         | -       |
| NESTED_F | f           | list  | 1,2,3   | None    |
"""
    markdown = markdown.lstrip()
    return SimpleSettings, table, markdown
