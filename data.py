# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# Данные для создания нового заказа в системе
# Станция метро с id=5 это Красносельская
new_order_body = {
    "firstName": "Агния",
    "lastName": "Барто",
    "address": "Ленина 33",
    "metroStation": 5,
    "phone": "+7 800 555 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-09-01",
    "comment": "Прямо у метро оставь, брат",
    "color": ["BLACK"]
}
