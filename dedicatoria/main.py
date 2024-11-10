import math
import flet as ft
from views import home


def main(page: ft.Page):
    page.window.width = 1080/2
    page.window.height = 1980/2
    page.title = "Nosso App"
    page.adaptive = True

    def route_change(route):
        page.views.clear()
        if page.route == "/home":
            page.views.append(home.home_page(page))
        page.update()
        
    page.on_route_change = route_change
    page.go("/home")
    page.update()
ft.app(target=main, assets_dir="./")