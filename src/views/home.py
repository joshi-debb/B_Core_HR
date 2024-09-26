import flet as ft

def home_view(page: ft.Page):
    page.title = 'Binaq - Inicio'
    page.window.width = 1150
    page.window.height = 800
    page.window.resizable = False
    page.window.maximizable = False
    page.bgcolor = '#000000'
    page.window.icon = './images/b_logo.png'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.center()

    # Crear la imagen de fondo con opacidad
    background_image = ft.Image(
        src='./images/bg_home.png',
        fit=ft.ImageFit.COVER,
        width=1200,
        opacity=0.8 
    )

    tittle = ft.Text(
        'Departamento de Recursos Humanos - Binarq',
        color='#000000',
        size=42,
        weight=ft.FontWeight.W_900,
    )

    image = ft.Image(
        src='./images/b_logo.png',
        width=80,
        fit=ft.ImageFit.CONTAIN        
    )

    # Lista simulada de empleados
    empleados = [
        {"nombre": f"Empleado {i+1}", "cargo": "Cargo de prueba", "foto": './images/default_p.png'} for i in range(6)
    ]

    def crear_profile_card(empleado):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src=empleado["foto"],  # Usar la foto del empleado
                            width=150,
                            fit=ft.ImageFit.CONTAIN        
                        ),
                        padding=ft.padding.all(10)
                    ),
                    ft.Container(
                        content=ft.Text(
                            f'Nombre: {empleado["nombre"]}',
                            color='#000000',
                            size=14,
                            weight=ft.FontWeight.W_900,
                        ),
                        padding=ft.padding.all(10)
                    ),
                    ft.Container(
                        content=ft.Text(
                            f'Cargo: {empleado["cargo"]}',
                            color='#000000',
                            size=14,
                            weight=ft.FontWeight.W_900,
                        ),
                        padding=ft.padding.all(10)
                    ),
                ],
            ),
            width=200,
            height=400,
            bgcolor='#85FFFFFF',
            border=ft.border.all(1, "#000000"),
            border_radius=10,
            padding=ft.padding.all(10)
        )

    # Crear la lista de tarjetas de perfil
    profile_cards = [crear_profile_card(empleado) for empleado in empleados]

    # Crear un GridView para organizar las tarjetas en forma de matriz
    grid_view = ft.GridView(
        controls=profile_cards,
        runs_count=5,
        max_extent=200,
        child_aspect_ratio=0.5,
        spacing=10,
        run_spacing=10,
        expand=True,
        padding=ft.padding.all(10)
    )

    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Stack(
                    controls=[
                        ft.Container(
                            content=image,
                            left=10,
                            border=ft.border.all(2, "#000000"),
                            border_radius=8
                        ),
                        ft.Container(
                            content=tittle,
                            left=110
                        )
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        padding=ft.padding.all(10),
        height=80,
        bgcolor='#85FFFFFF'
    )

    # Crear el control de la imagen para previsualización
    preview_image = ft.Image(src='./images/default_p.png', width=150, height=150, fit=ft.ImageFit.COVER)
    #preview_image = ft.Image(width=150, height=150, fit=ft.ImageFit.COVER)

    # Crear el FilePicker y añadirlo a la página
    file_picker = ft.FilePicker(
        
        on_result=lambda e: (
            setattr(preview_image, 'src', e.files[0].path) if e.files else None,
            page.update()  # Asegurarse de que la página se actualice después de cambiar la imagen
        )
    )

    # # Agregar el FilePicker a la página (no visible)
    # page.add(file_picker)

    # Función para cerrar el diálogo
    def cerrar_dialogo(dialog):
        preview_image.src = './images/default_p.png' 
        dialog.open = False
        page.update()

    # Función para agregar un empleado
    def agregar_empleado(dialog):
        # Obtener el nombre y cargo del diálogo
        nombre = dialog.content.controls[0].value
        cargo = dialog.content.controls[1].value
        # Lógica para guardar el empleado
        empleados.append({"nombre": nombre, "cargo": cargo, "foto": preview_image.src})  # Usar la imagen de previsualización
        actualizar_tarjetas()  # Actualizar tarjetas después de agregar
        preview_image.src = './images/default_p.png' 
        dialog.open = False
        page.update()

    # Función para mostrar el diálogo de agregar empleado
    def mostrar_dialogo_agregar():
        dialog = ft.AlertDialog(
            title=ft.Text("Agregar Empleado"),
            content=ft.Column(
                controls=[
                    ft.TextField(label="Nombre"),
                    ft.TextField(label="Cargo"),
                    ft.Column(
                        controls=[
                            ft.Text("Selecciona una foto:"),
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton("Cargar Foto", on_click=lambda e: file_picker.pick_files()),  # Muestra el diálogo de archivos
                                    preview_image,  # Control de imagen para previsualización
                                ],
                            )
                        ]
                    )
                ]
            ),
            actions=[
                ft.TextButton("Agregar", on_click=lambda e: agregar_empleado(dialog)),
                ft.TextButton("Cancelar", on_click=lambda e: cerrar_dialogo(dialog)),
            ],
        )

        # Conectar el diálogo a la página y abrirlo
        page.dialog = dialog
        dialog.open = True
        page.update()

    def actualizar_tarjetas():
        # Actualizar las tarjetas de perfil
        profile_cards.clear()
        profile_cards.extend(crear_profile_card(empleado) for empleado in empleados)
        grid_view.controls = profile_cards
        page.update()

    def handle_navigation_change(e):
        if e.control.selected_index == 0:
            print('Ver todos')
        elif e.control.selected_index == 1:
            mostrar_dialogo_agregar()  # Abre el diálogo para agregar
        elif e.control.selected_index == 2:
            print('Editar')
        elif e.control.selected_index == 3:
            print('Eliminar')
        elif e.control.selected_index == 4:
            print('Settings')

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        group_alignment=-0.9,
        bgcolor="#50FFA500",
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.RATE_REVIEW, 
                selected_icon=ft.icons.RATE_REVIEW, 
                label="Ver todos"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.PERSON_ADD),
                selected_icon_content=ft.Icon(ft.icons.PERSON_ADD),
                label="Agregar",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.EDIT),
                selected_icon_content=ft.Icon(ft.icons.EDIT),
                label="Editar",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.DELETE),
                selected_icon_content=ft.Icon(ft.icons.DELETE),
                label="Eliminar",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: handle_navigation_change(e),
    )

    body = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=rail,
                    width=150,
                ),
                ft.Container(
                    content=grid_view,
                    expand=True
                )
            ]
        ),
        bgcolor='#50FADFA1',
        height=635,
    )

    page.add(
        ft.Container(
            content=ft.Stack(
                controls=[
                    ft.Container(
                        content=background_image,
                    ),
                    ft.Container(
                        ft.Column(
                            controls=[header, body, file_picker],
                        ),
                        padding=ft.padding.all(10)
                    )
                ],
            ),
        ),
    )

    def on_logout():
        page.go('/login')
