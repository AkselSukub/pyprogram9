#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    flights_list = []

    # Ввод данных с клавиатуры и создание списка словарей
    num_flights = int(input("Введите количество рейсов: "))
    for _ in range(num_flights):
        destination = input("Введите пункт назначения рейса: ")
        flight_number = int(input("Введите номер рейса: "))
        plane_type = input("Введите тип самолета: ")

        flight_info = {"destination": destination, "flight_number": flight_number, "plane_type": plane_type}
        flights_list.append(flight_info)

    # Сортировка списка по возрастанию номера рейса
    flights_list.sort(key=lambda x: x["flight_number"])

    # Вывод на экран номеров рейсов и типов самолетов для выбранного пункта назначения
    search_destination = input("Введите название пункта назначения: ")
    found_flights = [flight for flight in flights_list if flight["destination"] == search_destination]

    if found_flights:
        print("Найденные рейсы:")
        for flight in found_flights:
            print(f"Номер рейса: {flight['flight_number']}, Тип самолета: {flight['plane_type']}")
    else:
        print("Рейсы в указанный пункт назначения не найдены.")

if __name__ == "__main__":
    main()