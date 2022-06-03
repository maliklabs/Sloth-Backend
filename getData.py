from dotenv import load_dotenv
import os

load_dotenv()

APCA_API_KEY_ID = os.getenv("APCA-API-KEY-ID")
APCA_API_SECRET_KEY = os.getenv("APCA-API-SECRET-KEY")

print(APCA_API_KEY_ID)
print(APCA_API_SECRET_KEY)