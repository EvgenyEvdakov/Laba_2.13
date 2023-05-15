# Функция добавления маршрута в список
def add_route(route_list):
    route = {}
    route['start'] = input("Введите начальный пункт маршрута: ")
    route['end'] = input("Введите конечный пункт маршрута: ")
    route['number'] = int(input("Введите номер маршрута: "))

    # Определяем индекс, на котором нужно вставить маршрут в список
    index = 0
    for i in range(len(route_list)):
        if route['number'] > route_list[i]['number']:
            index = i + 1
        else:
            break

    # Добавляем маршрут в список
    route_list.insert(index, route)
    print("Маршрут добавлен.")


# Функция вывода списка маршрутов на экран
def print_route(route_list):
    print("Список маршрутов:")
    for route in route_list:
        print(f"{route['number']}. {route['start']} - {route['end']}")


# Функция поиска маршрута по номеру
def get_route(route_list):
    number = int(input("Введите номер маршрута: "))
    for route in route_list:
        if route['number'] == number:
            print(f"Маршрут {number}: {route['start']} - {route['end']}")
            return
    print("Маршрут не найден.")
