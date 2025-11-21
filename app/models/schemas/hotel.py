from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Hotel(BaseModel):
    _id: Optional[str]
    name: str
    address: str
    city: str
    rating: float
    amenities: list
    description: str

class Room(BaseModel):
    _id: Optional[str]
    _hotel_id: str
    number: int
    type: str
    price: int
    amenities: list
    is_available: bool
    description: str

class Booking(BaseModel):
    _id: Optional[str]
    _hotel_id: str
    _room_id: str
    user_mail: str
    time_start: datetime
    time_end: datetime
    