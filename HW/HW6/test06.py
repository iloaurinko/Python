# Сайт: https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-
# GetBookings
from http import HTTPStatus
from requests import Response

class Urls:
    URL_AUTH = "https://restful-booker.herokuapp.com/auth"
    URL = "https://restful-booker.herokuapp.com/booking"
urls = Urls()

class Assertions:

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        actual_status_code = response.status_code
        assert actual_status_code == HTTPStatus.OK, f"Unexpected status code: {expected_status_code}, but got {actual_status_code}"

    @staticmethod
    def assert_last_first_name(lst, lst1):
        assert lst == lst1, f"Unexpected full name: {lst1}, but got {lst}"
assertions = Assertions()

# 1 GET
# - Создайте тест для получения списка всех id всех бронирований на сайте.
# - Тест считается пройденным, если status code ответа равен 200.
def get_all_bookings():
    """
    Делает GET запрос и возвращает id всех бронирований.
    :return: Response, объект с ответом сервера
    """
    return requests.get(URL)

def test_get_all_bookings():
    response = get_all_bookings()
    assert response.status_code == 200, "Код статуса не равен 200!"

# 2 POST
# Создайте тест, который включает в себя следующие шаги:
# - Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
# - Шаг 2. C помощью id вашего созданного бронирования получите
# информацию о вашем бронировании (через эндпоинт booking/{id}).
# - Тест считается пройденным, если имя и фамилия в вашем созданном
# бронировании (Шаг 1) совпадают с теми данными, которые вы получили.
# (Шаг 2)
#
# 3 PATCH
#
# Создайте тест, который включает в себя следующие шаги:
# - Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
# - Шаг 2. Создайте токен авторизации.
# - Шаг 3. Измените имя и фамилию в вашей брони через метод PATCH. (не
# забудьте передать в заголовке токен авторизации)
# - Шаг 4. C помощью id вашего созданного бронирования получите
# информацию о вашем бронировании.
#
# - Тест считается пройденным, если имя и фамилия в вашем измененном
# бронировании (Шаг 3) совпадают с теми данными, которые вы получили.
# (Шаг 4)
#
# 4 DELETE
#
# Создайте тест, который включает в себя следующие шаги:
# - Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
# - Шаг 2. Создайте токен авторизации.
# - Шаг 3. Удалите ваше бронирование по его id через метод DELETE. (не
# забудьте передать в заголовке токен авторизации)
#
# - Тест считается пройденным, если попытка получения информации о вашей
# брони по ее id возвращает статус 404 (Not Found).
# Повторение прошлого материала.
#
# Ответьте на следующие вопросы:
# 1. Что такое итерируемый объект? Какие итерируемые объекты вы знаете?
# 2. Что такое изменяемый или неизменяемый объект? Строка - это изменяемый
# или неизменяемый объект?
# 3. Что такое “генератор”? Как можно сгенерировать список?
#
# 1 Калькулятор
#
# - Создайте класс Calculator с методами add(), mul(), div(), которые
# выполняют сложение, умножение, деление двух чисел и возвращающих
# результат.
# - Калькулятор должен “запоминать” все совершенные операции. Например,
# если был вызван метод add(1, 2), то калькулятор должен запомнить это в
# виде строки “1 + 2 = 3” и тд.
# - Создайте метод show_operations(), который выводит на экран все
# совершенные раннее операции.
# - Создайте метод clear(), который “чистит память” калькулятора и удаляет
# историю операций.
# Например, такой код:
# calc = Calculator()
# calc.add(1, 3)
# calc.add(2, 10)
# calc.mul(100, 12.2)
# calc.show_operations()
#
# Должен вывести:
# 1 + 3 = 4
# 2 + 10 = 12
# 100 * 12.2 = 1220.0

import requests

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
