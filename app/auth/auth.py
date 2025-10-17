from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse, Response
from app.databases import database
from app.models.validation_models import User, LoginData

create_user_query = '''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    name TEXT,
                    surname TEXT,
                    mail TEXT,
                    password TEXT
                )
                '''

db_path = "app/databases/users.db"      

router = APIRouter(prefix='/api/v1/auth')

@router.post("/register")
async def register(data: User):
    async with database.SQLDatabase(db_path) as db:
        await db.create_database(create_user_query)

        user_exists = await db.fetch_elem(data.mail, data.password)
        if user_exists:
            return JSONResponse({'message': f'Такой аккаунт уже существует!'}, status_code = 400)
        
        await db.add_elem(data.id, data.name, data.surname, data.mail, data.password)

    return JSONResponse({'message': f'Вы зарегистрированы! Ваш id: {data.id}'})

@router.post("/login")
async def login(data: LoginData):
    async with database.SQLDatabase(db_path) as db:
        user_exists = await db.fetch_elem(data.mail, data.password)
        if user_exists:
            return JSONResponse({'message': f'Вы успешно вошли в свой аккаунт!'})
        
        return JSONResponse({'message': f'Неверный логин/пароль!'}, status_code = 400)