from dataclasses import dataclass

COLUMNS = ['Name', 'Description', 'Type', 'Example', 'Default']


@dataclass
class Row:
    name: str
    description: str
    type: str
    example: str
    default: str
