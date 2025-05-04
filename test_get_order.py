import sender_requests


def test_create_order_get_order():
    #Создаем заказ
    print("Отправляем запрос на создание заказа")
    response_create = sender_requests.create_order()
    assert response_create.status_code == 201, "Ошибка при создании заказа"
    print("Заказ создан")

    #Сохраняем трек-номер заказа
    print("Сохраняем трек-номер заказа из ответа")
    track_id = response_create.json()["track"]
    assert track_id != None, "Трек-номер не найден"
    print(f"Трек-номер заказа: {track_id}")

    #Получаем данные о заказе по трек-номеру
    print("Отправляем запрос на полученние данных о заказе по его трек-номеру")
    response_track = sender_requests.track_order(track_id)

    #Проверяем, что код овтета 200
    print("Проверка статус-кода")
    assert response_track.status_code == 200, f"Не удалось получить заказ по трек-номеру {track_id}"
    print("Заказ успешно найден")
