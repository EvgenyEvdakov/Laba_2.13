class Route:
    def __init__(self, start, end, number):
        self.start = start
        self.end = end
        self.number = number

    def __repr__(self):
        return f"Route(start={self.start}, end={self.end}, number={self.number})"


def input_routes():
    routes = []
    while True:
        start = input("Введите начальный пункт маршрута: ")
        end = input("Введите конечный пункт маршрута: ")
        number = int(input("Введите номер маршрута: "))
        route = Route(start, end, number)
        routes.append(route)
        if input("Добавить еще маршрут? (y/n): ").lower() != "y":
            break
    return sorted(routes, key=lambda x: x.number)


def find_route(routes, number):
    for route in routes:
        if route.number == number:
            return route
    return None