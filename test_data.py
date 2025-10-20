PRODUCT_TEST_CASES = [
    {
        "name": "Создание ноутбука", 
        "data": {
            "name": "Dell XPS 13",
            "data": {
                "year": 2024,
                "price": 1299.99,
                "CPU model": "Intel Core i7"
            }
        }, 
        "expected": 201
    },
    {
        "name": "Создание без имени", 
        "data": { # Отсутствует обязательное поле "name"
            "data": {
                "price": 999.99
            }
        }, 
        "expected": 400
    },
]