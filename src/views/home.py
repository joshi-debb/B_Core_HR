import flet as ft

def home_view(page: ft.Page):
    page.title = 'Binaq - Inicio'
    page.window_width = 1200
    page.window_height = 800
    page.window_resizable = False
    page.window_maximizable = False
    page.bgcolor = '#FAF7F0'
    page.window.icon = './images/b_logo.png'

    page.window_center() 

    page.add(
        ft.Text("Bienvenido a la página de inicio", color="black", size=30),
    )

    page.update()

