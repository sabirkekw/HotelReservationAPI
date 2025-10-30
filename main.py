import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.auth.auth import router as auth_router

app = FastAPI()

@app.get('/api/v1')
async def root():
    return JSONResponse({'message': 'Hotel Reservation API version 1.0'},status_code=200)

app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run(app,
                host='127.0.0.1',
                port=8080)