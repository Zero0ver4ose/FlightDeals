import requests
from pprint import pprint

sheety_get_endpoint = "https://api.sheety.co/78a2a1b4863d7ebc63f06cc972340b6c/flightDeals/prices"
sheety_user_endpoint = "https://api.sheety.co/78a2a1b4863d7ebc63f06cc972340b6c/flightDeals/users"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}


    def get_destination_data(self):
        response = requests.get(url=sheety_get_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_get_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = sheety_user_endpoint
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data