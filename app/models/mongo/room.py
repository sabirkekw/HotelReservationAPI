from odmantic import Model, Field, EmbeddedModel
from typing import List

class Room(Model):
    id: int = Field(key_name="_id", primary_field=True)
    hotel_id: int = Field(key_name="_hotel_id")
    room_number: str
    room_type: str
    price_per_night: float
    is_available: bool 