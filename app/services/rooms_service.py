from app.core.errors import NotFoundError

class RoomsService():
    def __init__(self, session, hotels_repo, rooms_repo):
        self.session = session
        self.hotels_repo = hotels_repo
        self.rooms_repo = rooms_repo

    async def get_room(self, room_id: int, hotel_id: int):
        room = await self.rooms_repo.get_room(room_id, hotel_id, self.session)
        if room == None:
            raise NotFoundError("Комната не найдена!")
        return room
    
    async def get_rooms(self, hotel_id: int):
        rooms = await self.rooms_repo.get_rooms(hotel_id, self.session)
        if len(rooms) == 0:
            raise NotFoundError("Комнаты не найдены!")
        return rooms

    def book_room(self, jwt): # should be in a book_service
        pass
    