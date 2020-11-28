import requests
import json

METAL = "XAG"
CURRENCY = "USD"


class Tracker:
    def __init__(self):
        self.api_host = "https://www.goldapi.io/"
        self.headers = {
            "x-access-token": "goldapi-e6gsukhz54uyx-io"
        }
        
    def get_price(self, metal, currency):
        """Get the price of the metal.
        
        Args:
            metal (str): Symbol of metal.
                E.g: XAU, XAG, XPT, XPD
            currency (str): Currency in ISO 4217 format.
        
        Returns:
            price (float): Price of the metal.
        """
        url = f"{self.api_host}api/{metal}/{currency}"
        r = requests.get(url, headers=self.headers)
        return r.json()["price"]

if __name__ == "__main__":
    t = Tracker()
    metals = ["XAU", "XAG"]
    currency = "USD"
    for metal in metals:
        price = t.get_price(metal, currency)
        print(f"Price of {metal} is {currency} {price}")
