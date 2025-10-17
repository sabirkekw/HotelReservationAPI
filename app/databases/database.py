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
    async def create_database(self,query):
        pass

    @abstractmethod
    async def add_elem(self, *args):
        pass

    @abstractmethod
    async def fetch_elem(self, *args):
        pass


class SQLDatabase(DatabaseConnection):
    def __init__(self,db_path):
        super().__init__(db_path)
    
    async def create_database(self, db_query):
        async with self.lock:
            await self.db.execute(db_query)
            await self.db.commit()

    async def add_elem(self, user_id: int, name: str, surname: str, mail: str, password: str):
        async with self.lock:
            await self.db.execute('''
                INSERT INTO users (user_id, name, surname, mail, password) VALUES (?,?,?,?,?)
                ''', (user_id, name, surname, mail, password))
            await self.db.commit()

    async def fetch_elem(self, mail: str, password: str):
        async with self.lock:
            async with self.db.execute(f'''
                SELECT mail, password
                FROM users
                WHERE mail = ? AND password = ?
                ''', (mail,password,)) as cursor:
                user_data = await cursor.fetchone()
                return bool(user_data)