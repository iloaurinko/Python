import requests

from pprint import pprint


URL = "https://restful-booker.herokuapp.com/booking"
URL_FOR_TOKEN = "https://restful-booker.herokuapp.com/auth"


def get_booking_by_id(id_):
    response = requests.get(URL + f"/{id_}")

    return response

# response = get_booking_by_id(911)
#
# if response.status_code == 200:
#     pprint(response.json())


def get_token():
    info = {
        "username" : "admin",
        "password" : "password123"
    }

    response = requests.post(URL_FOR_TOKEN, json=info)

    return response.json()["token"]

# token = get_token()
# print(token)


def create_booking():
    data = {
    "firstname" : "Aleksandr",
    "lastname" : "Matveev",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }

    response = requests.post(URL, json=data)

    return response


def patch_booking(id_):
    data = {
    "firstname": "James",
    "lastname": "Brown"
    }

    headers = {
        "Cookie": f"token={get_token()}"
    }

    response = requests.patch(URL + f"/{id_}", data=data, headers=headers)

    return response
#

# response = create_booking()
# my_id = response.json()["bookingid"]
#
# response = get_booking_by_id(my_id)
#
# pprint(response.json())
#
# patch_booking(my_id)
#
# response = get_booking_by_id(my_id)
#
# pprint(response.json())






