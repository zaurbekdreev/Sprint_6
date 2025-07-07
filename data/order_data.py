from datetime import datetime, timedelta

current_date = datetime.now() + timedelta(days=3)
date_formatted = current_date.strftime('%d.%m.%Y')

ORDER_DATA_1 = {
    'first_name': 'Владимир',
    'last_name': 'Путин',
    'address': 'г.Москва, ул. Красная площадь 1',
    'metro_station': 'Охотный ряд',
    'phone_number': '+74950000001',
    'delivery_date': date_formatted,
    'duration': 'сутки',
    'color': 'чёрный жемчуг',
    'comment': 'заказ 1'
}

ORDER_DATA_2 = {
    'first_name': 'Александр',
    'last_name': 'Лукашенко',
    'address': 'г.Москва, ул. Красная площадь 2',
    'metro_station': 'Белорусская',
    'phone_number': '+74950000002',
    'delivery_date': date_formatted,
    'duration': 'двое суток',
    'color': 'серая безысходность',
    'comment': 'заказ 2'
}
