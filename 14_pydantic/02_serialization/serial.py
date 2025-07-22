from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name="Hitesh",
    email="h@hitesh.ai",
    createdAt=datetime(2024, 3, 15, 14, 30,),
    address=Address(
        street="Something",
        city="Jaipur",
        zip_code="009988"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict)

json_str = user.model_dump_json()
print("="*30)
print(json_str)