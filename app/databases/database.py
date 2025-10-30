import asyncio
import aiosqlite
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    def __init__(self, db_path):
        self.db_path = db_path
        self.lock = asyncio.Lock()
        self.db = None

    async def __aenter__(self):
        self.db = await aiosqlite.connect(self.db_path)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.db.close()

    @abstractmethod
    async def add_elem(self, *args):
        pass

    @abstractmethod
    async def fetch_elem(self, *args):
        pass


class UserDatabase(DatabaseConnection):
    def __init__(self,db_path):
        super().__init__(db_path)

    async def add_elem(self, user_id: int, name: str, surname: str, mail: str, password: str):
        async with self.lock:
            await self.db.execute('''
                INSERT INTO users (user_id, name, surname, mail, password) VALUES (?,?,?,?,?)
                ''', (user_id, name, surname, mail, password))
            await self.db.commit()

    async def fetch_elem(self, mail: str):
        async with self.lock:
            async with self.db.execute(f'''
                SELECT *
                FROM users
                WHERE mail = ?
                ''', (mail,)) as cursor:
                user_data = await cursor.fetchone()
                if user_data:
                    return user_data
                return ('_error')