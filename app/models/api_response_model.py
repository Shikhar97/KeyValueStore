from typing import Optional
from dataclasses import dataclass


@dataclass
class ApiResponseModel:
    data: Optional[dict]
    status: str
    message: str
