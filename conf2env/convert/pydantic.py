from enum import Enum

from pydantic import BaseModel, BaseSettings
from pydantic.fields import ModelField, UndefinedType
from pydantic.main import ModelMetaclass

from conf2env.common import Row


def pydantic_settings_to_table(obj: BaseSettings | BaseModel,
                               prefix: str = '',
                               merge_env: bool = True,
                               config=None) -> dict:
    """From pydantic to table.

    Args:
        obj (BaseSettings): pydantic settings class

    Returns:
        list: table for markdown
    """
    if not config:
        config = obj.Config
    _table = []
    for _, field in obj.__fields__.items():
        field: ModelField = field

        env_names = field.field_info.extra.get('env_names', None)
        if env_names is None:
            env_names = [field.name]
        else:
            env_names = list(env_names)

        if isinstance(field.type_, ModelMetaclass):
            for env_name in env_names:
                _prefix = ''
                if getattr(config, 'env_nested_delimiter', False):
                    _prefix = f'{env_name}{config.env_nested_delimiter}'

                if not getattr(config, 'case_sensitive', False):
                    _prefix = _prefix.upper()
                _ttable = pydantic_settings_to_table(field.type_,
                                                     prefix=_prefix,
                                                     config=config)
                _table.extend(_ttable)
            continue

        if merge_env:
            env_name = '; '.join(
                [f'{prefix}{env_name}' for env_name in env_names])
            if len(env_names) > 1:
                env_name = f'Any of {env_name}'

        if not getattr(config, 'case_sensitive', False):
            env_name = env_name.upper()

        default = None
        if not isinstance(field.default, UndefinedType):
            default = field.default

        if isinstance(default, Enum):
            default = default.value

        example = default or ''
        if 'example' in field.field_info.extra:
            example = field.field_info.extra['example']

        if field.required:
            default = '-'

        if merge_env:
            row = Row(
                name=env_name,
                description=field.field_info.description or '',
                type=field.type_.__name__,
                example=example,
                default=default,
            )
            _table.append(row)
        else:
            for env_name in env_names:
                row = Row(
                    name=env_name,
                    description=field.field_info.description or '',
                    type=field.type_.__name__,
                    example=example,
                    default=default,
                )
                _table.append(row)
    return _table
