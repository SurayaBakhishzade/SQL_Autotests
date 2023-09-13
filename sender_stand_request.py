import configuration
import requests
import data
# Функция для создания заказа и извлечения номера трека
def create_order_and_extract_tracker():
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=data.order_body)

    if response.status_code == 201:
        order_data = response.json()
        tracker_id = order_data.get("track")
        if tracker_id is not None:
            return tracker_id

    # Если номер трека не был извлечен, вернем None
    return None
# Вызов функции create_order_and_extract_tracker() и сохранение номера трека
tracker_id = create_order_and_extract_tracker()

# Вывод номера трека (если он был извлечен)
if tracker_id is not None:
    print(f"Номер трека заказа: {tracker_id}")
else:
    print("Номер трека не был извлечен.")
