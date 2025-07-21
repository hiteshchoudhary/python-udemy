from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Hitesh Choudhary"
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000
    )


class User(BaseModel):
    email: str = Field(...,regex=r'')
    phone: str = Field(..., regex=r'')
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )
