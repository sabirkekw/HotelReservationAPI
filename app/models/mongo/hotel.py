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
    
class Room(Model):
    id: int = Field(key_name="_id", primary_field=True)
    hotel_id: int = Field(key_name="_hotel_id")
    room_number: str
    room_type: str
    price_per_night: float
    is_available: bool 