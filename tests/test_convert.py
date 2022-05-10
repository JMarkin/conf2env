from io import StringIO

import pytest

from conf2env import pydantic_settings_to_table, table_to_markdown

from .conftest import get_settings


@pytest.mark.parametrize("settings", get_settings())
def test_pydantic_to_dict(settings):
    _setting, valid_table, markdown = settings
    _t = pydantic_settings_to_table(_setting)
    assert valid_table == _t

    return _t


@pytest.mark.parametrize("settings", get_settings())
def test_table_to_markdown(settings):

    _setting, valid_table, markdown = settings
    _t = pydantic_settings_to_table(_setting)

    mark = StringIO()
    table_to_markdown(_t, buffer=mark)
    s = mark.getvalue()
    print(s)
    print(markdown)
    assert markdown == s
