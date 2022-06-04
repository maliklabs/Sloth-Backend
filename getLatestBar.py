from dotenv import load_dotenv
import os
import requests

def getLatestBar(ticker: str, timeframe: str = "1Hour") -> list:
    """
    Gets todays bar data in the timeframe for the ticker
    \n
    Arguments:
        - ticker: String for stock symbol
        - timeframe (optional): Timeframe for each bar. Set to '1Hour' by default
    \n
    Returns:
        - A list of dictionaries for each bar
        - The dictionary has 'index', 'open', 'high', 'low', and 'close' elements
    """

    if type(ticker) != str:
        exit("ERROR IN getLatestBar => Non-String entered for ticker variable")
    
    if (type(timeframe)) != str:
        exit("ERROR IN getLatestBar => Non-String entered for timeframe variable")

    load_dotenv()

    APCA_API_KEY_ID = os.getenv("APCA-API-KEY-ID")
    APCA_API_SECRET_KEY = os.getenv("APCA-API-SECRET-KEY")

    url = f'https://data.alpaca.markets/v2/stocks/{ticker}/bars'

    querystring = {"start":"2022-06-02T09:00:00-05:00","end":"2022-06-02T16:00:00-05:00","timeframe":timeframe}

    headers = {
        "APCA-API-KEY-ID": APCA_API_KEY_ID,
        "APCA-API-SECRET-KEY": APCA_API_SECRET_KEY
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    if "code" in data and "message" in data:
        exit(f'ERROR IN getLatestBar => Code {data["code"]}: {data["message"]}')

    simplified_data = []

    index = 0
    for data in data["bars"]:
        simplified_data.append({
            "index": index,
            "open": data["o"],
            "high": data["h"],
            "low": data["l"],
            "close": data["c"]
        })
        index += 1

    return simplified_data