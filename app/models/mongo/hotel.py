from odmantic import Model, Field, EmbeddedModel
from typing import List

class Hotel(Model):
    id: int = Field(key_name="_id", primary_field=True)
    name: str
    address: str
    city: str
    rating: float
    amenities: List[str]
    description: str