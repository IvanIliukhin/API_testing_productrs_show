import requests
import json
from config import BASE_URL
from test_data import PRODUCT_TEST_CASES

def test_create_products():
    print("=== ТЕСТИРОВАНИЕ СОЗДАНИЯ ПРОДУКТОВ ===\n")
    
    passed = 0
    failed = 0
    bugs = []
    
    for test in PRODUCT_TEST_CASES:
        print(f"Тест: {test['name']}")
        print(f"Данные: {test['data']}")
        
        try:
            response = requests.post(
                f"{BASE_URL}/api/products",
                json=test['data'],
                timeout=10
            )
            
            if response.status_code == test['expected']:
                print(f"✅ Успех: {response.status_code}")
                passed += 1
                
                # Для успешных запросов проверяем структуру ответа
                if response.status_code == 201:
                    data = response.json()
                    if 'id' not in data:
                        bugs.append(f"В успешном ответе нет ID продукта")
                        
            else:
                print(f"❌ Ожидал {test['expected']}, получил {response.status_code}")
                failed += 1
                bugs.append(f"{test['name']}: ожидал {test['expected']}, получил {response.status_code}")
                
        except Exception as e:
            print(f"⚠️ Ошибка: {e}")
            failed += 1
            bugs.append(f"{test['name']}: исключение - {e}")
        
        print("-" * 50)
    
    # Результаты
    print(f"\n📊 РЕЗУЛЬТАТЫ:")
    print(f"✅ Пройдено: {passed}")
    print(f"❌ Не пройдено: {failed}")
    
    if bugs:
        print(f"\n🐛 НАЙДЕННЫЕ БАГИ:")
        for bug in bugs:
            print(f"  - {bug}")
    
    return passed, failed, bugs

if __name__ == "__main__":
    test_create_products()