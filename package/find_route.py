def find_route(routes):
    number = input("Введите номер маршрута для поиска: ")
    found = False
    for route in routes:
        if route["number"] == number:
            print("Начальный пункт маршрута:", route["start"])
            print("Конечный пункт маршрута:", route["end"])
            found = True
            break
    if not found:
        print("Маршрут с таким номером не найден.")