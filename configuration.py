# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
# Значение нужно заменить после запуска сервера.
URL_SERVICE = "https://6b1d4d96-1435-4338-8f79-0ecbc37d53c6.serverhub.praktikum-services.ru"

# CREATE_ORDER_PATH содержит путь к методу создания заказа.
# Этот путь используется для формирования полного URL пути к эндпоинту,
# добавляя его к базовому URL сервиса.
# В результате получится что-то вроде "https://{id}.serverhub.praktikum-services.ru/api/v1/orders"
CREATE_ORDER_PATH = "/api/v1/orders"

# GET_ORDER_BY_TRACK_PATH содержит путь к методу получения заказа по его трек-номеру.
GET_ORDER_BY_TRACK_PATH = "/api/v1/orders/track"
