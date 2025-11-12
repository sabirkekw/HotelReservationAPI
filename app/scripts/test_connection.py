import asyncio
from app.core.mongo_config import database, engine
from app.models.mongo.hotel import Hotel

async def test_connection():
    try:
        print("Testing MongoDB connection...")
        session = database.session
        
        # Try to fetch hotels
        print("Attempting to fetch hotels...")
        hotels = await session.find(Hotel)
        hotels_list = [hotel async for hotel in hotels]
        
        print(f"Connection successful!")
        print(f"Found {len(hotels_list)} hotels in the database")
        for hotel in hotels_list:
            print(f"Hotel: {hotel.name}")
            
    except Exception as e:
        print(f"Error connecting to database: {str(e)}")
    finally:
        await engine.client.close()

if __name__ == "__main__":
    asyncio.run(test_connection())