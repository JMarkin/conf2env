"""Module for convert from project settings to markdown table of
environments."""
from sys import stdout
from typing import Iterable

from .common import COLUMNS, Row

MARKDOWN_TEMPLATE = " {: <%s} |"
BREAK_TEMPLATE = " {:-<%s} |"


def table_to_markdown(
    table: list[Row],
    cols: list[str] = COLUMNS,
    buffer=stdout,
) -> str:
    max_in_column = dict(zip(cols, [len(col) for col in cols]))

    for row in table:
        if isinstance(row.example, Iterable) and\
            not isinstance(row.example, str):
            row.example = ','.join([f'{v}' for v in row.example])
        for k in cols:
            k = k.lower()
            size = len(getattr(row, k, ''))
            if size > max_in_column[k]:
                max_in_column[k] = size

    maxes = tuple(max_in_column[k] for k in cols)
    row_template = f'|{MARKDOWN_TEMPLATE * len(cols)}' % maxes

    # HEADER
    print(row_template.format(*cols), file=buffer)
    # BREAK
    print((f'|{BREAK_TEMPLATE*len(cols)}' %
           maxes).format(*['' for _ in range(len(cols))]),
          file=buffer)

    # ROWS
    for row in table:
        print(row_template.format(*[row[k] for k in cols]), file=buffer)
