import json
import os

def loadData():
    if not os.path.exists("db.json"):
        return []
    
    try:
        with open("db.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Ошибка: Файл базы данных поврежден. Создан новый")
        return []
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        return []

def saveData(data):
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
if __name__ == "__main__":
    data = loadData()

    print("Список сохраненных чисел:")
    for num in data:
        print(num)

    number = int(input("\nВведите число: "))
    data.append(number)

    print("\nОбновленный список:")
    for num in data:
        print(num)

    saveData(data)

    input("\nНажмите любую кнопку чтобы выйти...")