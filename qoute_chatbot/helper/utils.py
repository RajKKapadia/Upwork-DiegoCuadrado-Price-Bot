import json

import requests

from config import config

def get_price(location: str) -> dict:
    try:
        payload = ""
        response = requests.request("GET", config.BACKEND_URL, data=payload)
        response = json.loads(response.text)
        price = 0.0
        for r in response:
            if r['ciudad'] == location:
                price += float(r['precio'])
        
        if price == 0.0:
            return f"We don't have price for the {location}."
        else:
            return f'The price of the location {location} is {round(price, 2)}.'
    except:
        return 'We are facing a technical issue at this time.'
    