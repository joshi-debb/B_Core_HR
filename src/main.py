import flet as ft

class Employee:
    def __init__(self, name, position, base_salary, deductions=0, bonuses=0):
        self.name = name
        self.position = position
        self.base_salary = base_salary
        self.deductions = deductions
        self.bonuses = bonuses

    def net_salary(self):
        return self.base_salary - self.deductions + self.bonuses


def main(page: ft.Page):
    # Establecer el tamaño de la ventana
    page.window.width = 800
    page.window.height = 600
    page.title = "ERP Recursos Humanos"
    page.bgcolor = ft.colors.GREY_200

    # Centrar la ventana
    page.window.center()

    # Lista para almacenar los empleados
    global employees
    employees = []

    # Definir la barra de navegación para los módulos
    def appbar(current_route):
        return ft.AppBar(
            title=ft.Text("ERP - Recursos Humanos"),
            center_title=True,
            bgcolor=ft.colors.BLUE_GREY_900,
            actions=[
                ft.IconButton(
                    icon=ft.icons.PEOPLE,
                    icon_color=ft.colors.YELLOW,
                    tooltip="Gestión de Empleados",
                    on_click=lambda _: navigate_to("/employees"),
                    icon_size=30
                ),
                ft.IconButton(
                    icon=ft.icons.SCHEDULE,
                    icon_color=ft.colors.LIGHT_GREEN_500,
                    tooltip="Control de Asistencias",
                    on_click=lambda _: navigate_to("/attendance"),
                    icon_size=30
                ),
                ft.IconButton(
                    icon=ft.icons.PAID,
                    icon_color=ft.colors.ORANGE,
                    tooltip="Nómina",
                    on_click=lambda _: navigate_to("/payroll"),
                    icon_size=30
                ),
                ft.IconButton(
                    icon=ft.icons.ASSESSMENT,
                    icon_color=ft.colors.RED,
                    tooltip="Evaluaciones de Desempeño",
                    on_click=lambda _: navigate_to("/performance"),
                    icon_size=30
                ),
            ]
        )

    # Definir la función para navegar entre módulos
    def navigate_to(route):
        page.views.clear()
        if route == "/employees":
            page.views.append(
                ft.View(
                    "/employees",
                    [
                        ft.Text("Gestión de Empleados", size=30),
                        # Aquí puedes agregar la lógica para gestionar empleados
                    ],
                    appbar=appbar(route)
                )
            )
        elif route == "/attendance":
            page.views.append(
                ft.View(
                    "/attendance",
                    [
                        ft.Text("Control de Asistencias", size=30),
                        # Aquí puedes agregar la lógica para gestionar asistencias
                    ],
                    appbar=appbar(route)
                )
            )
        elif route == "/payroll":
            page.views.append(
                ft.View(
                    "/payroll",
                    [
                        ft.Text("Gestión de Nómina", size=30),
                        # Aquí llamamos a la función que crea la interfaz de nómina
                        payroll_page(),
                    ],
                    appbar=appbar(route)
                )
            )
        elif route == "/performance":
            page.views.append(
                ft.View(
                    "/performance",
                    [
                        ft.Text("Evaluaciones de Desempeño", size=30),
                        # Aquí puedes agregar la lógica para evaluaciones de desempeño
                    ],
                    appbar=appbar(route)
                )
            )
        page.update()

    # Función para la interfaz de la página de nómina
    def payroll_page():
        # Contenedor para mostrar la nómina calculada
        payroll_container = ft.Column()

        # Función para agregar un nuevo empleado a la nómina
        def add_employee(e):
            # Recoger los valores del formulario
            name = name_input.value
            position = position_input.value
            base_salary = float(salary_input.value)
            deductions = float(deductions_input.value or 0)
            bonuses = float(bonuses_input.value or 0)

            # Crear un nuevo empleado
            new_employee = Employee(name, position, base_salary, deductions, bonuses)
            employees.append(new_employee)

            # Mostrar los empleados actualizados
            update_payroll_display()

            # Limpiar los inputs
            name_input.value = ""
            position_input.value = ""
            salary_input.value = ""
            deductions_input.value = ""
            bonuses_input.value = ""
            page.update()

        # Función para actualizar la visualización de la nómina
        def update_payroll_display():
            payroll_container.controls.clear()

            # Mostrar cada empleado con su salario neto
            for emp in employees:
                payroll_container.controls.append(
                    ft.Text(f"Empleado: {emp.name} | Cargo: {emp.position} | Salario Neto: ${emp.net_salary():.2f}")
                )
            page.update()

        # Inputs para el formulario de nómina
        name_input = ft.TextField(label="Nombre del Empleado")
        position_input = ft.TextField(label="Cargo del Empleado")
        salary_input = ft.TextField(label="Salario Base", keyboard_type="number")
        deductions_input = ft.TextField(label="Deducciones", keyboard_type="number")
        bonuses_input = ft.TextField(label="Bonificaciones", keyboard_type="number")

        # Botón para agregar empleados
        add_button = ft.ElevatedButton("Agregar Empleado", on_click=add_employee)

        # Layout para la página de nómina
        return ft.Column(
            [
                name_input,
                position_input,
                salary_input,
                deductions_input,
                bonuses_input,
                add_button,
                ft.Divider(),
                ft.Text("Lista de Empleados y Salarios Netos:", size=20),
                payroll_container,
            ],
            scroll=True
        )

    # Inicializar la vista con el dashboard general
    def load_dashboard():
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Text("Dashboard de Recursos Humanos", size=30),
                    # Aquí puedes mostrar estadísticas generales
                ],
                appbar=appbar("/")
            )
        )
        page.update()

    load_dashboard()  # Cargar el dashboard por defecto

# Ejecutar la aplicación
ft.app(target=main)
