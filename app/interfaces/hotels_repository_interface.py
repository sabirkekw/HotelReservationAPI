from abc import ABC, abstractmethod

class HotelsRepository(ABC):
    @abstractmethod
    async def get_hotel():
        pass

    async def get_hotels():
        pass
    