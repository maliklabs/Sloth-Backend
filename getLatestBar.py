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
        - The dictionary has 'time', 'open', 'high', 'low', and 'close' elements
    """

    if type(ticker) != str:
        exit("ERROR IN getLatestBar => Non-String entered for ticker variable")
    
    if (type(timeframe)) != str:
        exit("ERROR IN getLatestBar => Non-String entered for timeframe variable")

    