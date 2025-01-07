from models.candy import Candy
from services.gift_service import GiftService
from utils.json_handler import read_json, write_json

CANDIES_FILE = 'data/candies.json'
RESULT_FILE = 'data/result.json'


def display_menu():
    print("\nМеню:")
    print("1. Создать новогодний подарок")
    print("2. Добавить конфету")
    print("3. Удалить конфету")
    print("4. Показать все конфеты")
    print("0. Выйти")


def add_candy():
    name = input("Введите название конфеты: ")
    weight = int(input("Введите вес конфеты (в граммах): "))
    sugar_content = int(input("Введите содержание сахара (в граммах): "))
    candy = Candy(name, weight, sugar_content)

    candies_data = read_json(CANDIES_FILE)
    candies_data.append(candy.to_dict())
    write_json(CANDIES_FILE, candies_data)

    print(f"Конфета '{name}' успешно добавлена!")


def delete_candy():
    candies_data = read_json(CANDIES_FILE)
    print("\nСписок конфет:")
    for idx, candy in enumerate(candies_data, start=1):
        print(f"{idx}. {candy['name']} (Вес: {candy['weight']} г, Сахар: {candy['sugar_content']} г)")

    try:
        choice = int(input("\nВведите номер конфеты для удаления: ")) - 1
        if 0 <= choice < len(candies_data):
            removed_candy = candies_data.pop(choice)
            write_json(CANDIES_FILE, candies_data)
            print(f"Конфета '{removed_candy['name']}' успешно удалена!")
        else:
            print("Некорректный выбор. Попробуйте снова.")
    except ValueError:
        print("Ошибка: пожалуйста, введите корректный номер конфеты.")



def show_candies():
    candies_data = read_json(CANDIES_FILE)
    if not candies_data:
        print("Список конфет пуст.")
    else:
        print("\nСписок конфет:")
        for candy in candies_data:
            print(f"- {candy['name']} (Вес: {candy['weight']} г, Сахар: {candy['sugar_content']} г)")


def main():
    while True:
        display_menu()
        choice = input("\nВведите номер действия: ")

        if choice == "1":
            candies_data = read_json(CANDIES_FILE)
            candies = [Candy.from_dict(candy) for candy in candies_data]
            gift_service = GiftService(candies)

            try:
                target_weight = int(input("Введите желаемый вес подарка (целое число): "))
                gift = gift_service.create_gift(target_weight)

                if gift is None:
                    print("Невозможно собрать подарок на заданный вес. Попробуйте снова.")
                    continue

                print("Подарок успешно собран!")
                gift_dict = [candy.to_dict() for candy in gift]

                write_json(RESULT_FILE, gift_dict)
                print(f"Результат сохранен в {RESULT_FILE}")

                print("\nСортировка по общему весу конфет:")
                sorted_by_weight = gift_service.sort_by_total_weight(gift)
                for candy in sorted_by_weight:
                    print(f"{candy.name} - {candy.weight} г")

                print("\nСортировка по количеству конфет каждого типа:")
                sorted_by_count = gift_service.sort_by_count(gift)
                for candy in sorted_by_count:
                    print(f"{candy.name} - {candy.weight} г")

                min_sugar = int(input("\nВведите минимальное содержание сахара: "))
                max_sugar = int(input("Введите максимальное содержание сахара: "))
                filtered_gift = gift_service.filter_by_sugar_range(gift, min_sugar, max_sugar)

                print("\nКонфеты в заданном диапазоне содержания сахара:")
                for candy in filtered_gift:
                    print(f"{candy.name} - {candy.sugar_content} г сахара")

            except ValueError:
                print("Пожалуйста, введите корректное значение.")

        elif choice == "2":
            add_candy()

        elif choice == "3":
            delete_candy()

        elif choice == "4":
            show_candies()

        elif choice == "0":
            print("Выход из программы. Удачи!")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
