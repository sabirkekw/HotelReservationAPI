from abc import ABC, abstractmethod

class RoomsRepository(ABC):

    @abstractmethod
    async def get_room():
        pass

    @abstractmethod
    async def get_rooms():
        pass