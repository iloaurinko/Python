#Сайт: https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBookings
import functions as func
# 1 GET
# - Создайте тест для получения списка всех id всех бронирований на сайте.
# - Тест считается пройденным, если status code ответа равен 200.

def test_get_all_bookings():
    response = func.get_all_bookings()

    assert response.status_code == 200, "Код статуса не равен 200!"

#2 POST

#Создайте тест, который включает в себя следующие шаги:
#- Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
#- Шаг 2. C помощью id вашего созданного бронирования получите
#информацию о вашем бронировании (через эндпоинт booking/{id}).
#- Тест считается пройденным, если имя и фамилия в вашем созданном
#бронировании (Шаг 1) совпадают с теми данными, которые вы получили (Шаг 2).
def test_create_booking():
    data = {
        "firstname": "Jack",
        "lastname": "London",
        "totalprice": 90,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-02-02"
        },
        "additionalneeds": "Breakfast"
    }

    # Создаем бронирование и получаем его id из ответа
    created_booking = func.create_booking(data)
    id_ = created_booking.json()["bookingid"]

    # Получаем наше бронирование по его id
    response = func.get_booking_by_id(id_)
    response_data = response.json()

    assert response_data["firstname"] == data["firstname"]
    assert response_data["lastname"] == data["lastname"]

# 3 PATCH
# Создайте тест, который включает в себя следующие шаги:
# - Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
# - Шаг 2. Создайте токен авторизации.
# - Шаг 3. Измените имя и фамилию в вашей брони через метод PATCH. (не
# забудьте передать в заголовке токен авторизации)
# - Шаг 4. C помощью id вашего созданного бронирования получите
# информацию о вашем бронировании.
# - Тест считается пройденным, если имя и фамилия в вашем измененном
# бронировании (Шаг 3) совпадают с теми данными, которые вы получили.

def test_create_and_update_booking_via_patch():
    data = {
        "firstname": "Jules",
        "lastname": "Verne",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-03-03",
            "checkout": "2025-04-04"
        },
        "additionalneeds": "Breakfast"
    }

    created_booking = func.create_booking(data)
    id_ = created_booking.json()["bookingid"]

    # Изменили имя и фамилию в нашем бронировании
    headers = {
        "Cookie": f"token={func.get_token()}"
    }
    new_data = {
        "firstname": "Mike",
        "lastname": "Wazowski"
    }
    func.patch_booking_by_id(new_data, headers, id_)

    # Получили наше бронирование по его id
    patched_booking = func.get_booking_by_id(id_)
    response_data = patched_booking.json()

    assert response_data["firstname"] == new_data["firstname"]
    assert response_data["lastname"] == new_data["lastname"]

# 4 DELETE
#
# Создайте тест, который включает в себя следующие шаги:
# - Шаг 1. Создайте новое бронирование на сайте используя ваши данные.
# - Шаг 2. Создайте токен авторизации.
# - Шаг 3. Удалите ваше бронирование по его id через метод DELETE. (не
# забудьте передать в заголовке токен авторизации)
# - Тест считается пройденным, если попытка получения информации о вашей
# брони по ее id возвращает статус 404 (Not Found).

def test_delete_booking():
    data = {
        "firstname": "Jules",
        "lastname": "Verne",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-03-03",
            "checkout": "2025-04-04"
        },
        "additionalneeds": "Breakfast"
    }

    created_booking = func.create_booking(data)
    id_ = created_booking.json()["bookingid"]

    # Удаляем наше бронирование
    headers = {
        "Cookie": f"token={func.get_token()}"
    }
    func.delete_booking_by_id(headers, id_)

    # Пробуем получить наше удаленное бронирование
    booking = func.get_booking_by_id(id_)

    assert booking.status_code == 404 # 404 - ресурс не найден
