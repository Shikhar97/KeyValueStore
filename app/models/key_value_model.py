from pydantic import BaseModel, validator


class KeyValueModel(BaseModel):
    key: str
    value: str

