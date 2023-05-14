#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from routes_package import *

routes = []
while True:
    route = add_route()
    routes.append(route)
    routes = sort_routes(routes)
    choice = input("Хотите добавить еще один маршрут? (y/n):

if __name__ == '__main__':
    route()