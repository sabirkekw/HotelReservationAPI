import uvicorn
from app.core.config import settings
from app.api.v1.dependencies.dependencies import lifespan
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api.v1.endpoints.auth import router as auth_router

app = FastAPI(title=settings.app_name,lifespan=lifespan)
app.include_router(auth_router)

@app.get('/api/v1')
async def root():
    return JSONResponse({'message': 'Hotel Reservation API version 1.0'},status_code=200)

if __name__ == "__main__":
    uvicorn.run(app,
                host='127.0.0.1',
                port=8080)