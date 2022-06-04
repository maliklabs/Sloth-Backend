from dotenv import load_dotenv
import os
import requests

def getLatestPrice(ticker: str) -> float:
    """
    Gets the latest price for the ticker
    \n
    Arguments: 
        ticker: String for stock symbol
    \n
    Returns:
        The latest price as a float
    """
    if type(ticker) != str:
        exit("ERROR IN getLatestPrice => Non-String entered for Ticker variable")
    
    load_dotenv()

    APCA_API_KEY_ID = os.getenv("APCA-API-KEY-ID")
    APCA_API_SECRET_KEY = os.getenv("APCA-API-SECRET-KEY")

    url = f'https://data.alpaca.markets/v2/stocks/{ticker}/bars/latest'

    headers = {
        "APCA-API-KEY-ID": APCA_API_KEY_ID,
        "APCA-API-SECRET-KEY": APCA_API_SECRET_KEY
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()

    if "code" in data and "message" in data:
        exit(f'ERROR IN getLatestPrice => Code {data["code"]}: {data["message"]}')

    return data["bar"]["c"]