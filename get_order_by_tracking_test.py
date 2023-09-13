# Сурая Бахышзаде, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import pytest
import requests
import sender_stand_request  # Импортируйте модуль с функцией create_order_and_extract_tracker
import configuration

# Тестовая функция для проверки запроса на получение заказа по треку
def test_get_order_by_tracker():

    # Создание заказа и извлечение номера трека
    tracker_id = sender_stand_request.create_order_and_extract_tracker()

    # Проверка, что номер трека был успешно извлечен
    assert tracker_id is not None, "Не удалось создать заказ и извлечь номер трека"

    # Выполнение запроса на получение заказа по треку
    response = requests.get(
        f"{configuration.URL_SERVICE}/api/v1/orders/track?t={tracker_id}")

    # Проверка кода ответа
    assert response.status_code == 200, f"Код ответа не равен 200, был получен {response.status_code}"

if __name__ == "__main__":
    pytest.main()
