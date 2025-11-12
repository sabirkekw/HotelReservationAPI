from app.core.errors import NotFoundError

class HotelsService():
    def __init__(self, session, hotels_repo):
        self.session = session
        self.hotels_repo = hotels_repo

    async def get_all_hotels(self):
        hotels = await self.hotels_repo.get_hotels(self.session)
        if len(hotels) == 0:
            raise NotFoundError("Отели не найдены!")
        return hotels
    
    async def get_hotel_info(self, hotel_id: int):
        hotel = await self.hotels_repo.get_hotel(hotel_id, self.session)
        if not hotel:
            raise NotFoundError(f"Отель не найден!")
        return hotel