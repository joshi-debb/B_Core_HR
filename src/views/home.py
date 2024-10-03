import flet as ft

import datetime

from controllers.listas import municipios

from services import db

def home_view(page: ft.Page):
    page.title = 'Binaq - Inicio'
    page.window.width = 1200
    page.window.height = 800
    page.window.resizable = False
    # page.window.maximized = True
    page.window.maximizable = False
    page.bgcolor = '#000000'
    page.window.icon = './images/b_logo.png'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.center()

    # Crear la imagen de fondo con opacidad
    background_image = ft.Image(
        src='./images/bg_home.png',
        fit=ft.ImageFit.COVER,
        height=740,
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

    # Crear el control de la imagen para previsualización
    preview_image = ft.Image(src='./images/default_p.png', width=113, height=150, fit=ft.ImageFit.COVER)
    #preview_image = ft.Image(width=150, height=150, fit=ft.ImageFit.COVER)

    # Crear el FilePicker y añadirlo a la página
    file_picker = ft.FilePicker(
        
        on_result=lambda e: (
            setattr(preview_image, 'src', e.files[0].path) if e.files else None,
            page.update()  # Asegurarse de que la página se actualice después de cambiar la imagen
        )
    )

    edit_button = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(name=ft.icons.EDIT, color=ft.colors.WHITE),  # Ícono con color personalizado
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Alineación centrada del ícono
            ),
            alignment=ft.alignment.center,  # Alineación centrada en el contenedor
            width=15,  # Cambiar el ancho del contenedor
            height=30,  # Cambiar la altura del contenedor
        ),
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE,  # Cambiar el color de fondo del botón
            shape=ft.RoundedRectangleBorder(radius=8),  # Bordes redondeados (opcional)
        ),
        on_click=lambda e: print('Botón de editar presionado')  # Acción al hacer clic
    )

    delete_button = ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.icons.DELETE, color=ft.colors.WHITE),  # Ícono con color personalizado
            ],
            alignment=ft.MainAxisAlignment.CENTER  # Alineación centrada del ícono
        ),
        style=ft.ButtonStyle(
            bgcolor=ft.colors.RED,  # Cambiar el color de fondo del botón
            shape=ft.RoundedRectangleBorder(radius=8),  # Bordes redondeados (opcional)
        ),
        on_click=lambda e: print('Botón de editar presionado')  # Acción al hacer clic
    )

    # Lista simulada de empleados
    empleados = db.get_empleados()

    def crear_profile_card(empleado):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src=preview_image.src,  # Usar la foto del empleado
                            width=150,
                            fit=ft.ImageFit.CONTAIN        
                        ),
                        padding=ft.padding.all(10)
                    ),
                    ft.Container(
                        content=ft.Text(
                            f'{empleado['firstName']}',
                            color='#000000',
                            size=14,
                            weight=ft.FontWeight.W_900,
                        ),
                        padding=ft.padding.all(10)
                    ),
                    ft.Container(
                        content=ft.Text(
                            f'{empleado['lastName']}',
                            color='#000000',
                            size=14,
                            weight=ft.FontWeight.W_900,
                        ),
                        # padding=ft.padding.all(10)
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                edit_button, delete_button
                            ],
                            alignment=ft.MainAxisAlignment.START
                        ),
                        # padding=ft.padding.all(10)
                    ),
                ],
            ),
            width=200,
            height=400,
            bgcolor='#85FFFFFF',
            border=ft.border.all(1, '#000000'),
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
                            border=ft.border.all(2, '#000000'),
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

    

    def mostrar_dialogo_agregar():

        codigo_field = ft.Ref[ft.TextField]()
        nombres_field = ft.Ref[ft.TextField]()
        apellidos_field = ft.Ref[ft.TextField]()
        doc_field = ft.Ref[ft.TextField]()

        nit_field = ft.Ref[ft.TextField]()
        telefono_field = ft.Ref[ft.TextField]()
        correo_field = ft.Ref[ft.TextField]()

        genero_dropdown = ft.Dropdown(
            label='Género', 
            options=[
                ft.dropdown.Option('male', 'Masculino'),
                ft.dropdown.Option('female', 'Femenino'),
                ft.dropdown.Option('other', 'Otro'),
            ],
            width=200,
            value='male'
        )

        edad_field = ft.Ref[ft.TextField]()

        datepicker = ft.DatePicker(
            first_date=datetime.datetime(1960, 1, 1),
            last_date=datetime.datetime(2030, 12, 31),
            on_change=lambda e: update_birthday_label(e, page)
        )

        def open_date_picker(e):
            if datepicker not in page.overlay:
                page.overlay.append(datepicker)
                page.update()
            datepicker.pick_date()

        birth_day_label = ft.Text('', height=5)

        def update_birthday_label(e, page):
            birth_day_label.value = datepicker.value.strftime('%d/%m/%Y')
            page.update()

        calendar_button = ft.ElevatedButton(
            'Fecha Cumpleaños',
            icon=ft.icons.CALENDAR_MONTH,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
            width=200,
            height=40,
            on_click=open_date_picker
        )
        
        estado_civil_dropdown = ft.Dropdown(
            label='Estado Civil', 
            options=[
                ft.dropdown.Option('single', 'Soltero'),
                ft.dropdown.Option('married', 'Casado'),
                ft.dropdown.Option('divorced', 'Divorciado'),
                ft.dropdown.Option('widowed', 'Viudo'),
            ],
            width=200,
            value='single'
        )

        check_seguro = ft.Checkbox(label='Posee Seguro', value=False)

        nacionalidad_field = ft.Ref[ft.TextField]()

        departamento_dropdown = ft.Dropdown(
            label='Departamento', 
            options=[
                ft.dropdown.Option('alta_verapaz', 'Alta Verapaz'),
                ft.dropdown.Option('baja_verapaz', 'Baja Verapaz'),
                ft.dropdown.Option('chimaltenango', 'Chimaltenango'),
                ft.dropdown.Option('chuapas', 'Chiapas'),
                ft.dropdown.Option('coban', 'Cobán'),
                ft.dropdown.Option('escolastico', 'Escuintla'),
                ft.dropdown.Option('guatemala', 'Guatemala'),
                ft.dropdown.Option('huehuetenango', 'Huehuetenango'),
                ft.dropdown.Option('izabal', 'Izabal'),
                ft.dropdown.Option('jalapa', 'Jalapa'),
                ft.dropdown.Option('jutiapa', 'Jutiapa'),
                ft.dropdown.Option('quiche', 'Quiché'),
                ft.dropdown.Option('quetzaltenango', 'Quetzaltenango'),
                ft.dropdown.Option('san_marcos', 'San Marcos'),
                ft.dropdown.Option('santa_rosa', 'Santa Rosa'),
                ft.dropdown.Option('solala', 'Solalá'),
                ft.dropdown.Option('totonicapan', 'Totonicapán'),
                ft.dropdown.Option('verapaz', 'Verapaz'),
                ft.dropdown.Option('zacapa', 'Zacapa'),
            ],
            width=200,
            value='guatemala',
        )
        
        municipio_dropdown = ft.Dropdown(
            label='Municipio', 
            options=[],
            width=200
        )

        direccion_field = ft.Ref[ft.TextField]()

        profesion_field = ft.Ref[ft.TextField]()
        puesto_field = ft.Ref[ft.TextField]()
        departamento_field = ft.Ref[ft.TextField]()
        proyecto_field = ft.Ref[ft.TextField]()


        datepicker2 = ft.DatePicker(
            first_date=datetime.datetime(1960, 1, 1),
            last_date=datetime.datetime(2030, 12, 31),
            on_change=lambda e: update_init_day_label(e, page)
        )

        def open_date_picker2(e):
            if datepicker2 not in page.overlay:
                page.overlay.append(datepicker2)
                page.update()
            datepicker2.pick_date()

        init_day_label = ft.Text('', height=5)

        def update_init_day_label(e, page):
            init_day_label.value = datepicker2.value.strftime('%d/%m/%Y')
            page.update()

        fecha_inicio_button = ft.ElevatedButton(
            'Fecha Inicia',
            icon=ft.icons.CALENDAR_MONTH,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
            width=200,
            height=40,
            on_click=open_date_picker2
        )

        datepicker3 = ft.DatePicker(
            first_date=datetime.datetime(1960, 1, 1),
            last_date=datetime.datetime(2030, 12, 31),
            on_change=lambda e: update_end_day_label(e, page)
        )

        def open_date_picker3(e):
            if datepicker3 not in page.overlay:
                page.overlay.append(datepicker3)
                page.update()
            datepicker3.pick_date()

        end_day_label = ft.Text('', height=5)

        def update_end_day_label(e, page):
            end_day_label.value = datepicker3.value.strftime('%d/%m/%Y')
            page.update()

        fecha_final_button = ft.ElevatedButton(
            'Fecha Finaliza',
            icon=ft.icons.CALENDAR_MONTH,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
            width=200,
            height=40,
            on_click=open_date_picker3
        )

        salario_inicial_field = ft.Ref[ft.TextField]()
        salario_actual_field = ft.Ref[ft.TextField]()

        bonificacion_field = ft.Ref[ft.TextField]()
        otros_bonos_field = ft.Ref[ft.TextField]()
        igss_field = ft.Ref[ft.TextField]()
        check_prestaciones = ft.Checkbox(label='Prestaciones Laborales', value=False)

        enfermedad_field = ft.Ref[ft.TextField]()
        medicamento_field = ft.Ref[ft.TextField]()
        alergias_field = ft.Ref[ft.TextField]()

        tipo_sangre_dropdown = ft.Dropdown(
            label='Tipo de Sangre', 
            options=[
                ft.dropdown.Option('A+', 'A+'),
                ft.dropdown.Option('A-', 'A-'),
                ft.dropdown.Option('B+', 'B+'),
                ft.dropdown.Option('B-', 'B-'),
                ft.dropdown.Option('AB+', 'AB+'),
                ft.dropdown.Option('AB-', 'AB-'),
                ft.dropdown.Option('O+', 'O+'),
                ft.dropdown.Option('O-', 'O-'),
                ft.dropdown.Option('Desconocido', 'Desconocido'),
            ],
            width=200,
            value='Desconocido'  # Valor predeterminado
        )

        nombre_emergencia_field = ft.Ref[ft.TextField]()
        telefono_emergencia_field = ft.Ref[ft.TextField]()
        nombre_emergencia2_field = ft.Ref[ft.TextField]()
        telefono_emergencia2_field = ft.Ref[ft.TextField]()

        

        # Función para actualizar municipios según el departamento seleccionado
        def on_departamento_change(e):
            selected_departamento = e.control.value
            municipio_dropdown.options = [
                ft.dropdown.Option(municipio, municipio) for municipio in municipios.get(selected_departamento, [])
            ]
            municipio_dropdown.value = None  # Reinicia el municipio seleccionado
            page.update()

        # Evento de cambio en el dropdown de departamento
        departamento_dropdown.on_change = on_departamento_change

        # Crear el diálogo con varias columnas
        dialog = ft.AlertDialog(
            title=ft.Text('Agregar Empleado', weight=ft.FontWeight.W_900, selectable=True),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Row(  # Usa ListView para permitir el desplazamiento
                                controls=[
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Text('Información Personal', size=30, weight=ft.FontWeight.W_900, selectable=True),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Column(
                                                                        controls=[
                                                                            preview_image,
                                                                            ft.Text('Selecciona una foto:'),
                                                                            ft.ElevatedButton('Cargar Foto', on_click=lambda e: file_picker.pick_files()),
                                                                            
                                                                        ],
                                                                        
                                                                        
                                                                    ),
                                                                ],
                                                                #alienar horizontalmente al centro
                                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                                                
                                                            ),
                                                            width=200

                                                        ),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label='Codigo', width=200, ref=codigo_field),
                                                                    ft.TextField(label='Nombres', width=200, ref=nombres_field),
                                                                    ft.TextField(label='Apellidos', width=200, ref=apellidos_field),
                                                                    ft.TextField(label='DPI/Pasaporte', width=200, ref=doc_field),
                                                                    
                                                                ]
                                                            )
                                                            
                                                        ),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label='NIT', width=200, ref=nit_field),
                                                                    ft.TextField(label='Teléfono', width=200, ref=telefono_field),
                                                                    ft.TextField(label='Correo', width=200, ref=correo_field),
                                                                    genero_dropdown,
                                                                    
                                                                    
                                                                ]
                                                            )
                                                            
                                                        ),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label='Edad', width=200, ref=edad_field),
                                                                    ft.Container(
                                                                        content=calendar_button,
                                                                        padding=ft.padding.only(top=3),
                                                                    ),
                                                                    ft.Container(
                                                                        content=estado_civil_dropdown,
                                                                        padding=ft.padding.only(top=5),
                                                                    ),
                                                                    ft.Container(
                                                                        content=check_seguro,
                                                                        padding=ft.padding.only(top=10, bottom=5),
                                                                    ),
                                                                    # ft.TextField(label='Asegurado ?', width=200),
                                                                    
                                                                ],
                                                                
                                                            )
                                                            
                                                        )
                                                    ],
                                                  
                                                    expand=True
                                                ),

                                            ]
                                        )
                                        

                                    ),
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Text('Residencia', size=30, weight=ft.FontWeight.W_900, selectable=True),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label='Nacionalidad', width=200, ref=nacionalidad_field),
                                                                    departamento_dropdown,
                                                                    municipio_dropdown,
                                                                    ft.TextField(label='Direccion', width=200, ref=direccion_field),
                                                                ]
                                                            )
                                                            
                                                        ),
                                                        
                                                    ],
                                                    expand=True
                                                ),

                                            ]

                                        )
                                    )
                                    
                                ],
                                expand=True,  # Permite que el ListView ocupe todo el espacio
                            ),
                        ),
                        ft.Container(
                            content=ft.Row(  # Usa ListView para permitir el desplazamiento
                                controls=[
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Text('Información Laboral', size=30, weight=ft.FontWeight.W_900, selectable=True),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label='Profesion', width=200, ref=profesion_field, value='N/E'),
                                                                    ft.TextField(label='Puesto', width=200, ref=puesto_field),
                                                                    ft.TextField(label='Departamento', width=200, ref=departamento_field),
                                                                    ft.TextField(label='Proyecto', width=200, ref=proyecto_field),
                                                                ]
                                                            )
                                                            
                                                        ),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Container(
                                                                        content=fecha_inicio_button,
                                                                        padding=ft.padding.only(top=3, bottom=3),
                                                                    ),
                                                                    ft.Container(
                                                                        content=fecha_final_button,
                                                                        padding=ft.padding.only(top=3, bottom=6),
                                                                    ),
                                                                    ft.TextField(label='Salario inicial', width=200, ref=salario_inicial_field),
                                                                    ft.TextField(label='Salario Actual', width=200, ref=salario_actual_field),
                                                                ]
                                                            )
                                                            
                                                        ),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label='Bonificacion', width=200, ref=bonificacion_field),
                                                                    ft.TextField(label='Otros bonos', width=200, ref=otros_bonos_field),
                                                                    ft.TextField(label='Igss', width=200, ref=igss_field),
                                                                    ft.Container(
                                                                        content=check_prestaciones,
                                                                        padding=ft.padding.only(top=9, bottom=5),
                                                                    ),
                                                                    
                                                                    # ft.TextField(label='Prestaciones', width=200)
                                                                ]
                                                            )
                                                            
                                                        )
                                                    ],
                                                    expand=True
                                                ),

                                            ]

                                        )
                                    ),
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Text('Adicional', size=30, weight=ft.FontWeight.W_900, selectable=True),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label='Enfermedad', width=200, ref=enfermedad_field),
                                                                    ft.TextField(label='Medicamento', width=200, ref=medicamento_field),
                                                                    ft.TextField(label='Alergias', width=200, ref=alergias_field),
                                                                    tipo_sangre_dropdown,
                                                                    # ft.TextField(label='Tipo de Sangre', width=200),
                                                                ]
                                                            )
                                                            
                                                        ),
                                                        
                                                    ],
                                                    expand=True
                                                ),

                                            ]

                                        )
                                    ),
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Text('Emergencia', size=30, weight=ft.FontWeight.W_900, selectable=True),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label='Nombre', width=200, ref=nombre_emergencia_field),
                                                                    ft.TextField(label='No. Telefono', width=200, ref=telefono_emergencia_field),
                                                                    ft.TextField(label='Nombre', width=200, ref=nombre_emergencia2_field),
                                                                    ft.TextField(label='No. Telefono', width=200, ref=telefono_emergencia2_field),
                                                                ]
                                                            )
                                                            
                                                        )
                                                    ],
                                                    expand=True
                                                ),

                                            ]

                                        )
                                    ),
                                    
                                ],
                                expand=True,  # Permite que el ListView ocupe todo el espacio
                            ),
                        )
                    ]
                ),

                padding=ft.padding.all(10),
                width=1050,
                height=600,
            ),
            actions=[
                ft.TextButton('Agregar', on_click=lambda e: agregar_empleado(dialog)),
                ft.TextButton('Cancelar', on_click=lambda e: cerrar_dialogo(dialog)),
            ],
        )

        # Conectar el diálogo a la página y abrirlo
        page.dialog = dialog
        dialog.open = True
        page.update()

        # Función para cerrar el diálogo
        def cerrar_dialogo(dialog):
            preview_image.src = './images/default_p.png' 
            dialog.open = False
            page.update()

        # Función para agregar un empleado
        def agregar_empleado(dialog):
            codigo = codigo_field.current.value
            nombre = nombres_field.current.value
            apellido = apellidos_field.current.value
            documento = doc_field.current.value

            nit = nit_field.current.value
            telefono = telefono_field.current.value
            correo = correo_field.current.value
            genero = genero_dropdown.value

            edad = edad_field.current.value
            b_day = birth_day_label.value
            estado_civil = estado_civil_dropdown.value
            seguro = check_seguro.value

            nacionalidad = nacionalidad_field.current.value
            departamento = departamento_dropdown.value
            municipio = municipio_dropdown.value
            direccion = direccion_field.current.value

            profesion = profesion_field.current.value
            puesto = puesto_field.current.value
            deptmet = departamento_field.current.value
            proyecto = proyecto_field.current.value

            fecha_inicia = init_day_label.value
            fecha_finaliza = end_day_label.value
            salario_inicial = salario_inicial_field.current.value
            salario_actual = salario_actual_field.current.value

            bonificacion = bonificacion_field.current.value
            otros_bonos = otros_bonos_field.current.value
            igss = igss_field.current.value
            prestaciones = check_prestaciones.value

            enfermedad = enfermedad_field.current.value
            medicamento = medicamento_field.current.value
            alergias = alergias_field.current.value
            tipo_sangre = tipo_sangre_dropdown.value

            nombre_emergencia = nombre_emergencia_field.current.value
            telefono_emergencia = telefono_emergencia_field.current.value
            nombre_emergencia2 = nombre_emergencia2_field.current.value
            telefono_emergencia2 = telefono_emergencia2_field.current.value

            print('Personal Data', codigo, nombre, apellido, documento, nit, telefono, correo, genero, edad, b_day, estado_civil, seguro)
            print('Residencia', nacionalidad, departamento, municipio, direccion)
            print('Laboral', profesion, puesto, deptmet, proyecto, fecha_inicia, fecha_finaliza, salario_inicial, salario_actual, bonificacion, otros_bonos, igss, prestaciones)
            print('Adicional', enfermedad, medicamento, alergias, tipo_sangre)
            print('Emergencia', nombre_emergencia, telefono_emergencia, nombre_emergencia2, telefono_emergencia2)


            actualizar_tarjetas()  # Actualizar las tarjetas después de agregar
            preview_image.src = './images/default_p.png'
            dialog.open = False
            page.update()

    def actualizar_tarjetas():
        # Actualizar las tarjetas de perfil
        profile_cards.clear()
        empleados = db.get_empleados()
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
        bgcolor='#50FFA500',
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.RATE_REVIEW, 
                selected_icon=ft.icons.RATE_REVIEW, 
                label='Ver todos'
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.PERSON_ADD),
                selected_icon_content=ft.Icon(ft.icons.PERSON_ADD),
                label='Agregar',
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.EDIT),
                selected_icon_content=ft.Icon(ft.icons.EDIT),
                label='Editar',
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.DELETE),
                selected_icon_content=ft.Icon(ft.icons.DELETE),
                label='Eliminar',
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text('Settings'),
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
