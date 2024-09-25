import flet as ft

def login_view(page: ft.Page):
    page.title = 'Binaq - Inicio de Sesión'
    page.icon = 'icons.CONNECTED_TV'
    page.window.width = 600
    page.window.height = 485
    page.window.resizable = False
    page.window.maximizable = False
    page.bgcolor = '#000000'
    page.window.icon = './images/b_logo.png'
    page.window.center()

    # Crear la imagen de fondo con opacidad
    background_image = ft.Image(
        src='./images/b_logo.png',
        fit=ft.ImageFit.COVER,
        width=600,
        opacity=0.8  # Ajusta este valor para cambiar la transparencia (0.0 a 1.0)
    )

    # Crear campos de entrada para el usuario y la contraseña
    username_tf = ft.TextField(
        hint_text='Nombre de usuario',
        width=250,
        bgcolor="#FFFFFF",  # Fondo blanco y opaco
        border_color="#000000",  # Color del borde
        color="#000000",  # Color del texto
        opacity=0.9  # Ajusta este valor para cambiar la transparencia (0.0 a 1.0)
        
    )
    
    password_tf = ft.TextField(
        hint_text='Contraseña',
        password=True,
        width=250,
        bgcolor="#FFFFFF",  # Fondo blanco y opaco
        border_color="#000000",  # Color del borde
        color="#000000",  # Color del texto
        opacity=0.9  # Ajusta este valor para cambiar la transparencia (0.0 a 1.0)
    )

    # Crear un botón personalizado
    login_button = ft.ElevatedButton(
        'Iniciar Sesión',
        on_click=lambda e: on_login(username_tf, password_tf),
        bgcolor="#227B94",  # Color de fondo personalizado (azul)
        color="#FFFFFF",  # Color del texto (blanco)
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),  # Bordes redondeados
            padding=ft.padding.all(12),  # Espaciado interno
            elevation=5,  # Sombra del botón
        ),
        width=150,  # Ancho del botón
        height=40,  # Alto del botón
    )

    # Usar un contenedor para la imagen de fondo
    page.add(
        ft.Container(
            content=ft.Stack(
                controls=[
                    ft.Container(
                        content=background_image,  # Asegúrate de que la imagen esté en un contenedor
                        # padding=ft.padding.only(top=0)  # Padding superior para la imagen de fondo
                    ),
                    ft.Column(
                        # alignment=ft.MainAxisAlignment.CENTER,  # Centrar verticalmente
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar horizontalmente
                        controls=[
                            ft.Container(
                                content=username_tf,
                                padding=ft.padding.only(top=60)  # Padding superior para el TextField de usuario
                            ),
                            ft.Container(
                                content=password_tf,
                                padding=ft.padding.only(top=0)  # Padding superior para el TextField de contraseña
                            ),
                            ft.Container(
                                content=login_button,
                                padding=ft.padding.only(top=0)  # Padding superior para el botón
                            ),
                        ],
                        spacing=20  # Espacio entre los controles
                    )
                ],
                alignment=ft.alignment.center,  # Alinear todo el contenido del Stack al centro
            ),
        )
    )

    page.update()

    def show_error_dialog():
        alert_dialog = ft.AlertDialog(
            title=ft.Text("Error"),
            content=ft.Text("Usuario o contraseña incorrectos"),
            actions=[
                ft.TextButton("Aceptar", on_click=lambda e: close_dialog())
            ],
        )
        page.dialog = alert_dialog
        alert_dialog.open = True
        page.update()

    def close_dialog():
        page.dialog.open = False  # Cerrar el diálogo
        page.update()


    def on_login(username_tf, password_tf):

        if (username_tf.value == '' or password_tf.value == ''):
            print('Por favor, complete todos los campos')
            return

        elif (username_tf.value == '1' and password_tf.value == '1'):
            page.go("/home")

        else:
            show_error_dialog()
            return
        




