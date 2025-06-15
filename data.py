class DataForCourier:
    CREATE_COURIER = {
        "login": "OlkaOK",
        "password": "12345",
        "firstName": "Olka"
    }

class DataForAuth:
    CREATE_ID = {
        "login": "typ",
        "password": "1234"
}

class DataForOrder:
    CREATE_ORDER_BODY = {
        "firstName": "Olga",
        "lastName": "OK",
        "address": "Arial str., 13",
        "metroStation": 4,
        "phone": "+7 912 123 45 67",
        "rentTime": 5,
        "deliveryDate": "2025-06-14",
        "comment": "Brother? where are you?",
        "color": [
            "BLACK"
        ]
    }
class ErrorMessages:
    INSUFFICIENT_DATA_CREATE_MESSAGE = {'message': 'Недостаточно данных для создания учетной записи'}
    LOGIN_ALREADY_USED_MESSAGE = {'message': 'Этот логин уже используется. Попробуйте другой.'}
    NOT_FOUND_MESSAGE = {'message': 'Учетная запись не найдена'}
    INSUFFICIENT_DATA_LOGIN_MESSAGE = {'message':  'Недостаточно данных для входа'}

class OrderData:
    DEFAULT_ORDER_PAYLOAD = {
        "firstName": "Ольга",
        "lastName": "Клен",
        "address": "Кленовая, д. 3",
        "metroStation": 25,
        "phone": "+79991234567",
        "rentTime": 3,
        "deliveryDate": "2025-01-30",
        "comment": "Хочу новую гитару",
    }