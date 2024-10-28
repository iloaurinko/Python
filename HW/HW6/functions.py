import requests


URL = "https://restful-booker.herokuapp.com/booking"
URL_AUTH = "https://restful-booker.herokuapp.com/auth"


def get_all_bookings():
    """
    Делает GET запрос и возвращает id всех бронирований.

    :return: Response, объект с ответом сервера
    """

    return requests.get(URL)


def create_booking(data):
    """
    Делает POST запрос и создает новое бронирование.

    :param data: dict, словарь с данными для создания бронирования
    :return: Response, объект с ответом сервера
    """

    return requests.post(URL, json=data)


def get_booking_by_id(id_):
    """
    Делает GET запрос и возвращает бронирование по его id.

    :param id_: int, id бронирования
    :return: Response, объект с ответом сервера
    """

    return requests.get(URL + f"/{id_}")


def patch_booking_by_id(data, headers, id_):
    """
    Делает PATCH запрос и изменяет бронирование по его id.

    :param data: dict, словарь с новыми данными для бронирования
    :param headers: dict, словарь с заголовками {"Cookie": "token=..."}
    :param id_: int, id бронирования
    :return: Response, объект с ответом сервера
    """

    return requests.patch(URL + f"/{id_}", json=data, headers=headers)


def delete_booking_by_id(headers, id_):
    """
    Делает DELETE запрос и удаляет бронирование по его id.

    :param headers: dict, словарь с заголовками {"Cookie": "token=..."}
    :param id_: int, id бронирования
    :return: Response, объект с ответом сервера
    """

    return requests.delete(URL + f"/{id_}", headers=headers)


def get_token():
    """
    Делает POST запрос и возвращает созданный токен аутентификации.

    :return: str, токен аутентификации
    """

    data = {
        "username": "admin",
        "password": "password123"
    }

    return requests.post(URL_AUTH, json=data).json()["token"]