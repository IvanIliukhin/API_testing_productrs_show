import requests
import json
from test_data import PRODUCT_TEST_CASES

def test_products_with_validation():
    print("=== ПОЛНОЕ ТЕСТИРОВАНИЕ ВАЛИДАЦИИ ===")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for test in PRODUCT_TEST_CASES:
        print(f"🧪 {test['name']}")
        
        try:
            response = requests.post(
                "https://api.restful-api.dev/objects",
                json=test['data'],
                timeout=10
            )
            
            if response.status_code == test['expected']:
                print(f"   ✅ Успех: {response.status_code}")
                passed += 1
                
                # Дополнительная проверка для успешных запросов
                if response.status_code == 200:
                    data = response.json()
                    if data.get('name') != test['data'].get('name'):
                        print(f"   ⚠️ Имя не совпадает!")
                        
            else:
                print(f"   ❌ Ожидал {test['expected']}, получил {response.status_code}")
                failed += 1
                
        except Exception as e:
            print(f"   ⚠️ Ошибка: {e}")
            failed += 1
    
    print(f"\n📊 Результаты: {passed}/{passed+failed} прошло")
    
    # Анализ покрытия
    total_cases = len(PRODUCT_TEST_CASES)
    coverage = (passed / total_cases) * 100
    print(f"🎯 Покрытие тестами: {coverage:.1f}%")

if __name__ == "__main__":
    test_products_with_validation()