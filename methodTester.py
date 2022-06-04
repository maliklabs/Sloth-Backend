from getLatestPrice import getLatestPrice
from getLatestBar import getLatestBar

price = getLatestPrice("amzn")

bars = getLatestBar("amzn")

for bar in bars:
    print(bar)