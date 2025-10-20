PRODUCT_TEST_CASES = [
    # Позитивные
    {"name": "Валидные данные", "data": {"title": "MacBook Pro", "price": 1999.99, "category": "electronics"}, "expected": 201},
    {"name": "Минимальные данные", "data": {"title": "A", "price": 0.01, "category": "A"}, "expected": 201},
    
    # Негативные
    {"name": "Нет title", "data": {"price": 1999.99, "category": "electronics"}, "expected": 400},
    {"name": "Нет price", "data": {"title": "MacBook Pro", "category": "electronics"}, "expected": 400},
    {"name": "Нет category", "data": {"title": "MacBook Pro", "price": 1999.99}, "expected": 400},
    {"name": "Отрицательная цена", "data": {"title": "MacBook Pro", "price": -100, "category": "electronics"}, "expected": 400},
    {"name": "Нулевая цена", "data": {"title": "Free Item", "price": 0, "category": "freebies"}, "expected": 400},
    {"name": "Очень длинное название", "data": {"title": "A" * 256, "price": 100, "category": "electronics"}, "expected": 400},
    {"name": "Цена как строка", "data": {"title": "Test", "price": "hundred", "category": "electronics"}, "expected": 400},
]