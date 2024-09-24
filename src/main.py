import flet as ft
from views import login, home

def main(page: ft.Page):
    # Define las rutas
    def route_change(route):
        page.clean() 

        # Ruta de login
        if page.route == "/login":
            login.login_view(page)
        
        # Ruta de home
        elif page.route == "/home":
            home.home_view(page)
        
        page.update()

    # Definir la ruta por defecto al iniciar la aplicación
    page.on_route_change = route_change
    page.go("/login")  # Iniciar en la página de login

ft.app(target=main)
