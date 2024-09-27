import flet as ft

import datetime


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
        on_click=lambda e: print("Botón de editar presionado")  # Acción al hacer clic
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
        on_click=lambda e: print("Botón de editar presionado")  # Acción al hacer clic
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
                            f'{empleado["firstName"]}',
                            color='#000000',
                            size=14,
                            weight=ft.FontWeight.W_900,
                        ),
                        padding=ft.padding.all(10)
                    ),
                    ft.Container(
                        content=ft.Text(
                            f'{empleado["lastName"]}',
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

    

    # Función para cerrar el diálogo
    def cerrar_dialogo(dialog):
        preview_image.src = './images/default_p.png' 
        dialog.open = False
        page.update()

    # Función para agregar un empleado
    def agregar_empleado(dialog, genero_dropdown):
        # Obtener los valores de los campos y del dropdown de género
        nombre = dialog.content.controls[0].value
        apellido = dialog.content.controls[1].value
        dpi = dialog.content.controls[2].value
        nit = dialog.content.controls[3].value
        telefono = dialog.content.controls[4].value
        correo = dialog.content.controls[5].value
        edad = int(dialog.content.controls[6].value)
        genero = genero_dropdown.value 

        print(nombre, apellido, dpi, nit, telefono, correo, edad, genero)

        # Insertar los datos en la base de datos
        db.insert_personal_data(nombre, apellido, dpi, nit, telefono, correo, edad, genero)

        actualizar_tarjetas()  # Actualizar las tarjetas después de agregar
        preview_image.src = './images/default_p.png'
        dialog.open = False
        page.update()

    def mostrar_dialogo_agregar():
        # Crear el dropdown para el género
        genero_dropdown = ft.Dropdown(
            label="Género", 
            options=[
                ft.dropdown.Option("male", "Masculino"),
                ft.dropdown.Option("female", "Femenino"),
                ft.dropdown.Option("other", "Otro"),
            ],
            width=200,
            value="male"  # Género predeterminado
        )
        
        estado_civil_dropdown = ft.Dropdown(
            label="Estado Civil", 
            options=[
                ft.dropdown.Option("single", "Soltero"),
                ft.dropdown.Option("married", "Casado"),
                ft.dropdown.Option("divorced", "Divorciado"),
                ft.dropdown.Option("widowed", "Viudo"),
            ],
            width=200,
            value="single"  # Género predeterminado
        )

        departamento_dropdown = ft.Dropdown(
            label="Departamento", 
            options=[
                ft.dropdown.Option("altaverapaz", "Alta Verapaz"),
                ft.dropdown.Option("bajaverapaz", "Baja Verapaz"),
                ft.dropdown.Option("chimaltenango", "Chimaltenango"),
                ft.dropdown.Option("chuapas", "Chiapas"),
                ft.dropdown.Option("cobán", "Cobán"),
                ft.dropdown.Option("escolastico", "Escuintla"),
                ft.dropdown.Option("guatemala", "Guatemala"),
                ft.dropdown.Option("huehuetenango", "Huehuetenango"),
                ft.dropdown.Option("izabal", "Izabal"),
                ft.dropdown.Option("jalapa", "Jalapa"),
                ft.dropdown.Option("jenal", "Jutiapa"),
                ft.dropdown.Option("quiche", "Quiché"),
                ft.dropdown.Option("quitzaltenango", "Quetzaltenango"),
                ft.dropdown.Option("sanmarcos", "San Marcos"),
                ft.dropdown.Option("santa", "Santa Rosa"),
                ft.dropdown.Option("solala", "Solalá"),
                ft.dropdown.Option("totonicapan", "Totonicapán"),
                ft.dropdown.Option("verapaz", "Verapaz"),
                ft.dropdown.Option("zacapa", "Zacapa"),
            ],
            width=200,
            value="guatemala"  # Departamento predeterminado
        )

        # Diccionario de municipios por departamento
        municipios = {
            "alta_verapaz": [
                "Cobán", 
                "Santa Cruz Verapaz", 
                "San Cristóbal Verapaz", 
                "Tactic", 
                "Tamahú", 
                "San Miguel Tucurú", 
                "Panzós", 
                "Senahú", 
                "San Pedro Carchá", 
                "San Juan Chamelco", 
                "San Agustín Lanquín", 
                "Santa María Cahabón", 
                "Chisec", 
                "Chahal", 
                "Fray Bartolomé de las Casas", 
                "Santa Catalina La Tinta", 
                "Raxruhá"
            ],

            "baja_verapaz": [
                "Salamá",  # cabecera departamental
                "San Miguel Chicaj",
                "Rabinal",
                "Cubulco",
                "Granados",
                "Santa Cruz el Chol",
                "San Jerónimo",
                "Purulhá"
            ],
            "chimaltenango": [
                "Chimaltenango",  # cabecera departamental
                "San José Poaquil",
                "San Martín Jilotepeque",
                "San Juan Comalapa",
                "Santa Apolonia",
                "Tecpán",
                "Patzún",
                "San Miguel Pochuta",
                "Patzicía",
                "Santa Cruz Balanyá",
                "Acatenango",
                "San Pedro Yepocapa",
                "San Andrés Itzapa",
                "Parramos",
                "Zaragoza",
                "El Tejar"
            ],
            "chiquimula": [
                "Chiquimula",  # cabecera departamental
                "Jocotán",
                "Esquipulas",
                "Camotán",
                "Quezaltepeque",
                "Olopa",
                "Ipala",
                "San Juan Ermita",
                "Concepción Las Minas",
                "San Jacinto",
                "San José la Arada"
            ],
            "peten": [
                "Flores",  # cabecera departamental
                "San José",
                "San Benito",
                "San Andrés",
                "La Libertad",
                "San Francisco",
                "Santa Ana",
                "Dolores",
                "San Luis",
                "Sayaxché",
                "Melchor de Mencos",
                "Poptún"
            ],
            "el_progreso": [
                "El Jícaro",
                "Morazán",
                "San Agustín Acasaguastlán",
                "San Antonio La Paz",
                "San Cristóbal Acasaguastlán",
                "Sanarate",
                "Guastatoya",  # cabecera departamental
                "Sansare"
            ],
            "quiche": [
                "Santa Cruz del Quiché",  # cabecera departamental
                "Chiché",
                "Chinique",
                "Zacualpa",
                "Chajul",
                "Santo Tomás Chichicastenango",
                "Patzité",
                "San Antonio Ilotenango",
                "San Pedro Jocopilas",
                "Cunén",
                "San Juan Cotzal",
                "Santa María Joyabaj",
                "Santa María Nebaj",
                "San Andrés Sajcabajá",
                "Uspantán",
                "Sacapulas",
                "San Bartolomé Jocotenango",
                "Canillá",
                "Chicamán",
                "Ixcán",
                "Pachalum"
            ],

            "escuintla": [
                "Escuintla",  # cabecera departamental
                "Santa Lucía Cotzumalguapa",
                "La Democracia",
                "Siquinalá",
                "Masagua",
                "Tiquisate",
                "La Gomera",
                "Guazacapán",
                "San José",
                "Iztapa",
                "Palín",
                "San Vicente Pacaya",
                "Nueva Concepción"
            ],

            "guatemala": [
                "Santa Catarina Pinula",
                "San José Pinula",
                "Guatemala",  # cabecera departamental
                "San José del Golfo",
                "Palencia",
                "Chinautla",
                "San Pedro Ayampuc",
                "Mixco",
                "San Pedro Sacatapéquez",
                "San Juan Sacatepéquez",
                "Chuarrancho",
                "San Raymundo",
                "Fraijanes",
                "Amatitlán",
                "Villa Nueva",
                "Villa Canales",
                "San Miguel Petapa"
            ],

            "huehuetenango": [
                "Huehuetenango",  # cabecera departamental
                "Chiantla",
                "Malacatancito",
                "Cuilco",
                "Nentón",
                "San Pedro Necta",
                "Jacaltenango",
                "Soloma",
                "Ixtahuacán",
                "Santa Bárbara",
                "La Libertad",
                "La Democracia",
                "San Miguel Acatán",
                "San Rafael La Independencia",
                "Todos Santos Cuchumatán",
                "San Juan Atitlán",
                "Santa Eulalia",
                "San Mateo Ixtatán",
                "Colotenango",
                "San Sebastián Huehuetenango",
                "Tectitán",
                "Concepción Huista",
                "San Juan Ixcoy",
                "San Antonio Huista",
                "Santa Cruz Barillas",
                "San Sebastián Coatán",
                "Aguacatán",
                "San Rafael Petzal",
                "San Gaspar Ixchil",
                "Santiago Chimaltenango",
                "Santa Ana Huista"
            ],
            "izabal": [
                "Morales",
                "Los Amates",
                "Livingston",
                "El Estor",
                "Puerto Barrios"  # cabecera departamental
            ],
            "jalapa": [
                "Jalapa",  # cabecera departamental
                "San Pedro Pinula",
                "San Luis Jilotepeque",
                "San Manuel Chaparrón",
                "San Carlos Alzatate",
                "Monjas",
                "Mataquescuintla"
            ],
            "jutiapa": [
                "Jutiapa",  # cabecera departamental
                "El Progreso",
                "Santa Catarina Mita",
                "Agua Blanca",
                "Asunción Mita",
                "Yupiltepeque",
                "Atescatempa",
                "Jerez",
                "El Adelanto",
                "Zapotitlán",
                "Comapa",
                "Jalpatagua",
                "Conguaco",
                "Moyuta",
                "Pasaco",
                "Quesada"
            ],
            "quetzaltenango": [
                "Quetzaltenango",  # cabecera departamental
                "Salcajá",
                "San Juan Olintepeque",
                "San Carlos Sija",
                "Sibilia",
                "Cabricán",
                "Cajolá",
                "San Miguel Siguilá",
                "San Juan Ostuncalco",
                "San Mateo",
                "Concepción Chiquirichapa",
                "San Martín Sacatepéquez",
                "Almolonga",
                "Cantel",
                "Huitán",
                "Zunil",
                "Colomba Costa Cuca",
                "San Francisco La Unión",
                "El Palmar",
                "Coatepeque",
                "Génova",
                "Flores Costa Cuca",
                "La Esperanza",
                "Palestina de Los Altos"
            ],
            "retalhuleu": [
                "Retalhuleu",  # cabecera departamental
                "San Sebastián",
                "Santa Cruz Muluá",
                "San Martín Zapotitlán",
                "San Felipe",
                "San Andrés Villa Seca",
                "Champerico",
                "Nuevo San Carlos",
                "El Asintal"
            ],
            "sacatepequez": [
                "Antigua Guatemala",  # cabecera departamental
                "Jocotenango",
                "Pastores",
                "Sumpango",
                "Santo Domingo Xenacoj",
                "Santiago Sacatepéquez",
                "San Bartolomé Milpas Altas",
                "San Lucas Sacatepéquez",
                "Santa Lucía Milpas Altas",
                "Magdalena Milpas Altas",
                "Santa María de Jesús",
                "Ciudad Vieja",
                "San Miguel Dueñas",
                "San Juan Alotenango",
                "San Antonio Aguas Calientes",
                "Santa Catarina Barahona"
            ],
            "san_marcos": [
                "San Marcos",  # cabecera departamental
                "Ayutla",
                "Catarina",
                "Comitancillo",
                "Concepción Tutuapa",
                "El Quetzal",
                "El Rodeo",
                "El Tumblador",
                "Ixchiguán",
                "La Reforma",
                "Malacatán",
                "Nuevo Progreso",
                "Ocós",
                "Pajapita",
                "Esquipulas Palo Gordo",
                "San Antonio Sacatepéquez",
                "San Cristóbal Cucho",
                "San José Ojetenam",
                "San Lorenzo",
                "San Miguel Ixtahuacán",
                "San Pablo",
                "San Pedro Sacatepéquez",
                "San Rafael Pie de la Cuesta",
                "Sibinal",
                "Sipacapa",
                "Tacaná",
                "Tajumulco",
                "Tejutla",
                "Río Blanco",
                "La Blanca"
            ],
            "santa_rosa": [
                "Cuilapa",  # cabecera departamental
                "Casillas Santa Rosa",
                "Chiquimulilla",
                "Guazacapán",
                "Nueva Santa Rosa",
                "Oratorio",
                "Pueblo Nuevo Viñas",
                "San Juan Tecuaco",
                "San Rafael Las Flores",
                "Santa Cruz Naranjo",
                "Santa María Ixhuatán",
                "Santa Rosa de Lima",
                "Taxisco",
                "Barberena"
            ],
            "solola": [
                "Sololá",  # cabecera departamental
                "Concepción",
                "Nahualá",
                "Panajachel",
                "San Andrés Semetabaj",
                "San Antonio Palopó",
                "San José Chacayá",
                "San Juan La Laguna",
                "San Lucas Tolimán",
                "San Marcos La Laguna",
                "San Pablo La Laguna",
                "San Pedro La Laguna",
                "Santa Catarina Ixtahuacán",
                "Santa Catarina Palopó",
                "Santa Clara La Laguna",
                "Santa Cruz La Laguna",
                "Santa Lucía Utatlán",
                "Santa María Visitación",
                "Santiago Atitlán"
            ],
            "suchitepequez": [
                "Mazatenango",  # cabecera departamental
                "Cuyotenango",
                "San Francisco Zapotitlán",
                "San Bernardino",
                "San José El Ídolo",
                "Santo Domingo Suchitépequez",
                "San Lorenzo",
                "Samayac",
                "San Pablo Jocopilas",
                "San Antonio Suchitépequez",
                "San Miguel Panán",
                "San Gabriel",
                "Chicacao",
                "Patulul",
                "Santa Bárbara",
                "San Juan Bautista",
                "Santo Tomás La Unión",
                "Zunilito",
                "Pueblo Nuevo",
                "Río Bravo"
            ],
            "totonicapan": [
                "Totonicapán",  # cabecera departamental
                "San Cristóbal Totonicapán",
                "San Francisco El Alto",
                "San Andrés Xecul",
                "Momostenango",
                "Santa María Chiquimula",
                "Santa Lucía La Reforma",
                "San Bartolo"
            ],
            "zacapa": [
                "Zacapa",  # cabecera departamental
                "Cabañas",
                "Estanzuela",
                "Gualán",
                "Huité",
                "La Unión",
                "Río Hondo",
                "San Jorge",
                "San Diego",
                "Teculután",
                "Usumatlán"
            ],

        }

        # Dropdown de departamentos
        departamento_dropdown = ft.Dropdown(
            label="Departamento", 
            options=[
                ft.dropdown.Option("alta_verapaz", "Alta Verapaz"),
                ft.dropdown.Option("baja_verapaz", "Baja Verapaz"),
                ft.dropdown.Option("chimaltenango", "Chimaltenango"),
                ft.dropdown.Option("chuapas", "Chiapas"),
                ft.dropdown.Option("coban", "Cobán"),
                ft.dropdown.Option("escolastico", "Escuintla"),
                ft.dropdown.Option("guatemala", "Guatemala"),
                ft.dropdown.Option("huehuetenango", "Huehuetenango"),
                ft.dropdown.Option("izabal", "Izabal"),
                ft.dropdown.Option("jalapa", "Jalapa"),
                ft.dropdown.Option("jutiapa", "Jutiapa"),
                ft.dropdown.Option("quiche", "Quiché"),
                ft.dropdown.Option("quetzaltenango", "Quetzaltenango"),
                ft.dropdown.Option("san_marcos", "San Marcos"),
                ft.dropdown.Option("santa_rosa", "Santa Rosa"),
                ft.dropdown.Option("solala", "Solalá"),
                ft.dropdown.Option("totonicapan", "Totonicapán"),
                ft.dropdown.Option("verapaz", "Verapaz"),
                ft.dropdown.Option("zacapa", "Zacapa"),
            ],
            width=200,
            value="guatemala",  # Departamento predeterminado
        )
        
        # Dropdown de municipios
        municipio_dropdown = ft.Dropdown(
            label="Municipio", 
            options=[],
            width=200
        )

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

        # Agrega los dropdowns a la página
        # page.add(departamento_dropdown, municipio_dropdown)

        # DatePicker configuración
        datepicker = ft.DatePicker(
            first_date=datetime.datetime(1960, 1, 1),
            last_date=datetime.datetime(2030, 12, 31),
            on_change=lambda e: update_birthday_label(e, page)
        )

        selected_date_label = ft.Text("Cumpleaños no seleccionado", height=5)

        

        def open_date_picker(e):
            # Asegurarse de que el DatePicker está en la página antes de abrirlo
            if datepicker not in page.overlay:
                page.overlay.append(datepicker)
                page.update()  # Asegurarse de que el control está actualizado
            datepicker.pick_date()  # Abre el DatePicker

        def update_birthday_label(e, page):
            print(datepicker.value.strftime("%d/%m/%Y"))
            selected_date_label.value = datepicker.value.strftime("%d/%m/%Y")
            page.update()

        
        calendar_button = ft.ElevatedButton(
            "Fecha Cumpleaños",
            icon=ft.icons.CALENDAR_MONTH,  # Cambia el ícono según tu preferencia
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN,  # Cambia el color de fondo del botón
                color=ft.colors.WHITE,     # Cambia el color del texto
                shape=ft.RoundedRectangleBorder(radius=8),  # Bordes redondeados
            ),
            width=200,  # Ancho del botón
            height=40,  # Alto del botón
            on_click=open_date_picker
        )

        fecha_inicio_button = ft.ElevatedButton(
            "Fecha Inicia",
            icon=ft.icons.CALENDAR_MONTH,  # Cambia el ícono según tu preferencia
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN,  # Cambia el color de fondo del botón
                color=ft.colors.WHITE,     # Cambia el color del texto
                shape=ft.RoundedRectangleBorder(radius=8),  # Bordes redondeados
            ),
            width=200,  # Ancho del botón
            height=40,  # Alto del botón
            on_click=open_date_picker
        )

        fecha_final_button = ft.ElevatedButton(
            "Fecha Finaliza",
            icon=ft.icons.CALENDAR_MONTH,  # Cambia el ícono según tu preferencia
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN,  # Cambia el color de fondo del botón
                color=ft.colors.WHITE,     # Cambia el color del texto
                shape=ft.RoundedRectangleBorder(radius=8),  # Bordes redondeados
            ),
            width=200,  # Ancho del botón
            height=40,  # Alto del botón
            on_click=open_date_picker
        )

        # Crear el diálogo con varias columnas
        dialog = ft.AlertDialog(
            title=ft.Text("Agregar Empleado", weight=ft.FontWeight.W_900, selectable=True),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Row(  # Usa ListView para permitir el desplazamiento
                                controls=[
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Text("Información Personal", size=30, weight=ft.FontWeight.W_900, selectable=True),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Column(
                                                                        controls=[
                                                                            preview_image,
                                                                            ft.Text("Selecciona una foto:"),
                                                                            ft.ElevatedButton("Cargar Foto", on_click=lambda e: file_picker.pick_files()),
                                                                            
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
                                                                    ft.TextField(label="Codigo", width=200),
                                                                    ft.TextField(label="Nombres", width=200),
                                                                    ft.TextField(label="Apellidos", width=200),
                                                                    ft.TextField(label="DPI/Pasaporte", width=200),
                                                                    
                                                                ]
                                                            )
                                                            
                                                        ),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label="NIT", width=200),
                                                                    ft.TextField(label="Teléfono", width=200),
                                                                    ft.TextField(label="Correo", width=200),
                                                                    genero_dropdown,
                                                                    
                                                                    
                                                                ]
                                                            )
                                                            
                                                        ),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label="Edad", width=200),
                                                                    ft.Container(
                                                                        content=calendar_button,
                                                                        padding=ft.padding.only(top=3),
                                                                    ),
                                                                    ft.Container(
                                                                        content=estado_civil_dropdown,
                                                                        padding=ft.padding.only(top=5),
                                                                    ),
                                                                    ft.TextField(label="Asegurado ?", width=200),
                                                                    
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
                                                ft.Text("Residencia", size=30, weight=ft.FontWeight.W_900, selectable=True),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label="Nacionalidad", width=200),
                                                                    departamento_dropdown,
                                                                    municipio_dropdown,
                                                                    ft.TextField(label="Direccion", width=200),
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
                                                ft.Text("Información Laboral", size=30, weight=ft.FontWeight.W_900, selectable=True),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label="Profesion", width=200),
                                                                    ft.TextField(label="Puesto", width=200),
                                                                    ft.TextField(label="Departamento", width=200),
                                                                    ft.TextField(label="Proyecto", width=200),
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
                                                                    ft.TextField(label="Salario inicial", width=200),
                                                                    ft.TextField(label="Salario Actual", width=200),
                                                                ]
                                                            )
                                                            
                                                        ),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label="Bonificacion", width=200),
                                                                    ft.TextField(label="Otros bonos", width=200),
                                                                    ft.TextField(label="Igss", width=200),
                                                                    ft.TextField(label="Prestaciones", width=200)
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
                                                ft.Text("Adicional", size=30, weight=ft.FontWeight.W_900, selectable=True),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label="Enfermedad", width=200),
                                                                    ft.TextField(label="Medicamento", width=200),
                                                                    ft.TextField(label="Alergias", width=200),
                                                                    ft.TextField(label="Tipo de Sangre", width=200),
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
                                                ft.Text("Emergencia", size=30, weight=ft.FontWeight.W_900, selectable=True),
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.TextField(label="Nombre", width=200),
                                                                    ft.TextField(label="No. Telefono", width=200),
                                                                    ft.TextField(label="Nombre", width=200),
                                                                    ft.TextField(label="No. Telefono", width=200)
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
                ft.TextButton("Agregar", on_click=lambda e: agregar_empleado(dialog, genero_dropdown)),
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
