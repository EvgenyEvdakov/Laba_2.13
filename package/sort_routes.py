def sort_routes(routes):
    sorted_routes = sorted(routes, key=lambda x: x["number"])
    return sorted_routes