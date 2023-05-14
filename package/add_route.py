def add_route():
    start = input("Введите начальный пункт маршрута: ")
    end = input("Введите конечный пункт маршрута: ")
    number = input("Введите номер маршрута: ")
    route = {
        "start": start,
        "end": end,
        "number": number
    }
    return route