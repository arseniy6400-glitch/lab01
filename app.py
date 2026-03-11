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

def viewNumberList(data):
    if not data:
        print("\nСписок пуст")
    else:
        print("\nСписок сохраненных чисел:")
        for num in data:
            print(num)

def addNumber():
    number = int(input("\nВведите число: "))
    data.append(number)


if __name__ == "__main__":
    
    data = loadData()
    run = True

    while run:
        print("\n                ---МЕНЮ---")
        print("1. Список чисел  2. Добавить число 3. Выход")
        
        choice = input("\nВыбирите действие: ")
        
        if choice == "1":
            viewNumberList(data)
        elif choice == "2":
            addNumber()
        elif choice == "3":
            run = False
        else:
            print("\nТакого действия нет")

    saveData(data)    
