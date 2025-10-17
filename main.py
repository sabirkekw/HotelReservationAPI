import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from databases import database
from models.validation_models import User, LoginData

create_user_query = '''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    name TEXT,
                    surname TEXT,
                    mail TEXT,
                    password TEXT
                )
                '''

db_path = "./databases/users.db"          

app = FastAPI()

@app.post("/api/v1/auth/register")
async def register(data: User):
    async with database.SQLDatabase(db_path) as db:
        await db.create_database(create_user_query)

        user_exists = db.fetch_elem(data.mail, data.password)
        if user_exists:
            return JSONResponse({'message': f'Такой аккаунт уже существует!'})
        
        await db.add_elem(data.id, data.name, data.surname, data.mail, data.password)

    return JSONResponse({'message': f'Вы зарегистрированы! Ваш id: {data.id}'})

@app.post("/api/v1/auth/login")
async def login(data: LoginData):
    async with database.SQLDatabase(db_path) as db:
        user_exists = await db.fetch_elem(data.mail, data.password)
        if user_exists:
            return JSONResponse({'message': f'Вы успешно вошли в свой аккаунт!'})
        
        return JSONResponse({'message': f'Неверный логин/пароль!'})
    
if __name__ == "__main__":
    uvicorn.run(app,
                host='127.0.0.1',
                port=8080)