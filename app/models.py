from enum import Enum
from pydantic import BaseModel, Field


class Status(str, Enum):
    completed = "completed"
    pending = "pending"
    canceled = "canceled"


class Criterion(str, Enum):
    completed = "completed"
    pending = "pending"
    canceled = "canceled"
    all = "all"


class Order(BaseModel):
    id: int
    item: str
    quantity: int = Field(gt=0, description="The quantity must be greater than zero")
    price: float = Field(gt=0, description="The price must be greater than zero")
    status: Status
