PRODUCT_TEST_CASES = [
    # ==================== ПОЗИТИВНЫЕ СЦЕНАРИИ ====================
    {
        "name": "Создание ноутбука (полные данные)", 
        "data": {
            "name": "Dell XPS 13",
            "data": {
                "year": 2024,
                "price": 1299.99,
                "CPU model": "Intel Core i7",
                "color": "Silver",
                "RAM": "16GB",
                "storage": "512GB SSD"
            }
        }, 
        "expected": 200
    },
    {
        "name": "Создание с минимальными данными", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": 2024,
                "price": 1.0
            }
        }, 
        "expected": 200
    },
    {
        "name": "Создание с максимально длинным именем", 
        "data": {
            "name": "A" * 50,  # Проверяем длинные имена
            "data": {
                "year": 2024,
                "price": 100.0
            }
        }, 
        "expected": 200
    },
    {
        "name": "Создание с спецсимволами в имени", 
        "data": {
            "name": "Product-123_Test",
            "data": {
                "year": 2024,
                "price": 100.0
            }
        }, 
        "expected": 200
    },
    
    # ==================== НЕГАТИВНЫЕ СЦЕНАРИИ ====================
    {
        "name": "Создание без имени (обязательное поле)", 
        "data": { 
            "data": {
                "year": 2024,
                "price": 999.99
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание с пустым именем", 
        "data": {
            "name": "",
            "data": {
                "year": 2024,
                "price": 100.0
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание без data (обязательное поле)", 
        "data": {
            "name": "Test Product"
        }, 
        "expected": 400
    },
    {
        "name": "Создание с пустым data", 
        "data": {
            "name": "Test Product",
            "data": {}
        }, 
        "expected": 400
    },
    {
        "name": "Создание с отрицательной ценой", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": 2024,
                "price": -100.0
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание с нулевой ценой", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": 2024,
                "price": 0.0
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание с отрицательным годом", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": -2024,
                "price": 100.0
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание с очень большим годом", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": 9999,
                "price": 100.0
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание с ценой как строка", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": 2024,
                "price": "сто рублей"  # Неверный тип
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание с годом как строка", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": "две тысячи двадцать четвертый",
                "price": 100.0
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание с очень длинным именем (>100 символов)", 
        "data": {
            "name": "A" * 150,
            "data": {
                "year": 2024,
                "price": 100.0
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание с SQL инъекцией", 
        "data": {
            "name": "Test'; DROP TABLE products; --",
            "data": {
                "year": 2024,
                "price": 100.0
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание с XSS инъекцией", 
        "data": {
            "name": "<script>alert('xss')</script>",
            "data": {
                "year": 2024,
                "price": 100.0
            }
        }, 
        "expected": 400
    },
    {
        "name": "Создание с null значениями", 
        "data": {
            "name": None,
            "data": {
                "year": 2024,
                "price": 100.0
            }
        }, 
        "expected": 400
    },
    
    # ==================== ГРАНИЧНЫЕ ЗНАЧЕНИЯ ====================
    {
        "name": "Создание с минимальной ценой (0.01)", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": 2024,
                "price": 0.01
            }
        }, 
        "expected": 200
    },
    {
        "name": "Создание с максимальной ценой", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": 2024,
                "price": 999999.99
            }
        }, 
        "expected": 200
    },
    {
        "name": "Создание с текущим годом", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": 2024,
                "price": 100.0
            }
        }, 
        "expected": 200
    },
    {
        "name": "Создание с прошлым годом", 
        "data": {
            "name": "Test Product",
            "data": {
                "year": 2020,
                "price": 100.0
            }
        }, 
        "expected": 200
    }
]