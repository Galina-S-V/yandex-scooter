# Галина Виноградова, 20-я когорта - Финальный проект. Инженер по тестированию плюс.

import sender_stand_request
import data


# Тест 1. Успешное получение заказа по треку.
# Шаги автотеста:
#   1. Выполнить запрос на создание заказа.
#   2. Сохранить номер трека заказа.
#   3. Выполнить запрос на получения заказа по треку заказа.
#   4. Проверить, что код ответа равен 200.
def test_get_order_by_track_get_success_response():
    new_order_response = sender_stand_request.post_new_order(data.new_order_body)
    track = new_order_response.json()["track"]

    get_order_response = sender_stand_request.get_order_by_track(track)
    assert get_order_response.status_code == 200
