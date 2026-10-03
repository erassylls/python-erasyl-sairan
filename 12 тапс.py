class Vehicle:
    def __init__(self, brand, max_speed):
        if not brand.strip():
            raise ValueError("Марка транспорта не может быть пустой")

        if max_speed <= 0:
            raise ValueError("Скорость должна быть больше 0")

        self.brand = brand
        self.max_speed = max_speed

    def move(self):
        print("Транспортное средство движется")


class Car(Vehicle):
    def move(self):
        print(f"Машина {self.brand} едет по дороге")


class Bicycle(Vehicle):
    def move(self):
        print(f"Велосипед {self.brand} едет по дороге")


class Airplane(Vehicle):
    def move(self):
        print(f"Самолет {self.brand} летит в небе")


vehicles = []

while True:
    try:
        print("\n--- МЕНЮ ---")
        print("1. Добавить машину")
        print("2. Добавить велосипед")
        print("3. Добавить самолет")
        print("4. Показать транспорт")
        print("5. Движение")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            brand = input("Введите марку машины: ")

            try:
                speed = int(input("Введите максимальную скорость: "))
                vehicles.append(Car(brand, speed))
                print("Машина добавлена!")

            except ValueError as error:
                print("Ошибка:", error)

        elif choice == "2":
            brand = input("Введите марку велосипеда: ")

            try:
                speed = int(input("Введите максимальную скорость: "))
                vehicles.append(Bicycle(brand, speed))
                print("Велосипед добавлен!")

            except ValueError as error:
                print("Ошибка:", error)

        elif choice == "3":
            brand = input("Введите марку самолета: ")

            try:
                speed = int(input("Введите максимальную скорость: "))
                vehicles.append(Airplane(brand, speed))
                print("Самолет добавлен!")

            except ValueError as error:
                print("Ошибка:", error)

        elif choice == "4":
            if len(vehicles) == 0:
                print("Транспорт пока не добавлен")
            else:
                for vehicle in vehicles:
                    print(f"{vehicle.brand} — {vehicle.max_speed} км/ч")

        elif choice == "5":
            if len(vehicles) == 0:
                print("Транспорт пока не добавлен")
            else:
                for vehicle in vehicles:
                    vehicle.move()

        elif choice == "0":
            print("Программа завершена")
            break

        else:
            print("Неверный выбор!")

    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем")
        break

    except EOFError:
        print("\nВвод завершен. Программа закрыта")
        break