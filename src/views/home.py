import flet as ft

def home_view(page: ft.Page):
    page.title = 'Binaq - Inicio'
    page.window.width = 1150
    page.window.height = 800
    page.window.resizable = False
    page.window.maximizable = False
    # page.window.maximized = True
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
        width= 80,
        fit=ft.ImageFit.CONTAIN        
    )

    # Crear un botón personalizado
    logout_button = ft.ElevatedButton(
        'Iniciar Sesión',
        on_click=lambda e: on_logout(),
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

    profile_card = ft.Container(
        content=ft.Column(
            controls=[                    
                    ft.Container(
                        content=ft.Image(
                            src='./images/default_p.png',
                            width= 150,
                            fit=ft.ImageFit.CONTAIN        
                        ),
                        padding=ft.padding.all(10)
                    ),
                    ft.Container(
                        content=ft.Text(
                            'Nombre: Juan Perez',
                            color='#000000',
                            size=14,
                            weight=ft.FontWeight.W_900,
                        ),
                        padding=ft.padding.all(10)
                    ),
                    ft.Container(
                        content=ft.Text(
                            'Cargo: Gerente de Recursos Humanos',
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
        # border=ft.border.all(1, "#000000"),
        # border_radius=10,
        bgcolor='#85FFFFFF'
    )


    def handle_navigation_change(e):
        if e.control.selected_index == 0:
            print('Ver todos')
        elif e.control.selected_index == 1:
            print('Agregar')
        elif e.control.selected_index == 2:
            print('Editar')
        elif e.control.selected_index == 3:
            print('Eliminar')
        elif e.control.selected_index == 4:
            print('Settings')
        elif e.control.selected_index == 5:
            print('Settings')
    
    # Crear el NavigationRail
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
                ft.Stack(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=rail,
                                    width=150
                                ),
                                ft.Container(
                                    content= profile_card,
                                    
                                )
                            ]
                        )
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        bgcolor='#50FADFA1',
        height=635,
        # padding=ft.padding.all(10),
        # border=ft.border.all(1, "#000000"),
        # border_radius=10,
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
                            controls=[
                                header,
                                body
                            ],
                        ),
                        padding=ft.padding.all(10)
                    )
                    
                ],
                # alignment=ft.alignment.center, 
            ),
        ),
        
    )


    def on_logout():
        page.go('/login')



    


