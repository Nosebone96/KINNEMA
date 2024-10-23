import flet as ft
from models.Models import controls

def main_hooke_law(page: ft.Page) -> ft.View:
    page.scroll = ft.ScrollMode.HIDDEN

    # Funciones para calcular la Ley de Hooke
    def calculate_force(constant, displacement):
        return constant * displacement

    def calculate_constant(force, displacement):
        return force / displacement

    def calculate_displacement(force, constant):
        return force / constant

    # Función para realizar el cálculo según los valores ingresados
    def calcular_hooke(e):
        try:
            if Constante_input.value and Desplazamiento_input.value:
                constant = float(Constante_input.value)
                displacement = float(Desplazamiento_input.value)
                force = calculate_force(constant, displacement)
                Constante_input.value = f"{constant:.2f}"
                Desplazamiento_input.value = f"{displacement:.2f}"
                Fuerza_input.value = f"{force:.2f}"
            elif Fuerza_input.value and Desplazamiento_input.value:
                force = float(Fuerza_input.value)
                displacement = float(Desplazamiento_input.value)
                constant = calculate_constant(force, displacement)
                Constante_input.value = f"{constant:.2f}"
                Desplazamiento_input.value = f"{displacement:.2f}"
                Fuerza_input.value = f"{force:.2f}"
            elif Fuerza_input.value and Constante_input.value:
                force = float(Fuerza_input.value)
                constant = float(Constante_input.value)
                displacement = calculate_displacement(force, constant)
                Constante_input.value = f"{constant:.2f}"
                Desplazamiento_input.value = f"{displacement:.2f}"
                Fuerza_input.value = f"{force:.2f}"
            else:
                print("Valores inválidos")
                return
        except ValueError as e:
            print("Valores inválidos, error")
            return

        # Asegurar que los campos se actualicen en la interfaz
        Constante_input.update()
        Desplazamiento_input.update()
        Fuerza_input.update()

    # Función para limpiar los campos
    def limpiar_hooke(e):
        Constante_input.value = ""
        Desplazamiento_input.value = ""
        Fuerza_input.value = ""
        
        # Actualizar los campos en la interfaz
        Constante_input.update()
        Desplazamiento_input.update()
        Fuerza_input.update()

    # Crear campos de entrada y etiquetas
    Fuerza_input = ft.TextField(label="Fuerza (F) en Newtons:", suffix_text='N')
    Constante_input = ft.TextField(label="Constante (k) en N/m:", suffix_text='N/m')
    Desplazamiento_input = ft.TextField(label="Desplazamiento (x) en metros:", suffix_text='m')

    # Crear botones
    calcular_button = ft.Button(text="Calcular", on_click=calcular_hooke)
    limpiar_button = ft.Button(text="Limpiar", on_click=limpiar_hooke)

    # Contenedor principal
    content_hooke = ft.Container(
        content=ft.Column(
            controls=[
                Fuerza_input,
                Constante_input,
                Desplazamiento_input,
                calcular_button,
                limpiar_button
            ]
        ),
        margin=ft.margin.all(20),
        padding=ft.padding.all(30)
    )

    # Agregar el contenido a la página
    page.add(content_hooke)

    return ft.View(
        "/ley_de_hooke",
        [
            ft.Column(
                controls=[
                    controls.header_page(page),
                    ft.Container(
                        content=content_hooke, 
                        margin= ft.margin.only(top= 10, left= 0, right=0)
                    ),
                ]
            )
        ],scroll=True
        
    )
