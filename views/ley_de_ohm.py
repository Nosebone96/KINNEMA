import flet as ft
from models.Models import controls

def main_ohm_law(page: ft.Page):
    page.scroll = ft.ScrollMode.HIDDEN

    # Funciones para calcular ley de Ohm
    def calculate_voltage(amper, resistance):
        return amper * resistance

    def calculate_amper(voltage, resistance):
        return voltage / resistance

    def calculate_resistance(amper, voltage):
        return voltage / amper

    # Función para realizar el cálculo según los valores ingresados
    def calcular_ohm(e):
        try:
            if Amper_input.value and Resistance_input.value:
                resistance = float(Resistance_input.value)
                amper = float(Amper_input.value)
                voltage = calculate_voltage(amper, resistance)
                Amper_input.value = f"{amper:.2f}"
                Voltage_input.value = f"{voltage:.2f}"
                Resistance_input.value = f"{resistance:.2f}"
            elif Voltage_input.value and Resistance_input.value:
                resistance = float(Resistance_input.value)
                voltage = float(Voltage_input.value)
                amper = calculate_amper(voltage, resistance)
                Amper_input.value = f"{amper:.2f}"
                Voltage_input.value = f"{voltage:.2f}"
                Resistance_input.value = f"{resistance:.2f}"
            elif Amper_input.value and Voltage_input.value:
                voltage = float(Voltage_input.value)
                amper = float(Amper_input.value)
                resistance = calculate_resistance(amper, voltage)
                Amper_input.value = f"{amper:.2f}"
                Voltage_input.value = f"{voltage:.2f}"
                Resistance_input.value = f"{resistance:.2f}"
            else:
                print("Invalid values")
                return
        except ValueError as e:
            print("Invalid values, failed")
            return

        # Asegurar que los campos se actualicen en la interfaz
        Amper_input.update()
        Voltage_input.update()
        Resistance_input.update()

    # Función para limpiar los campos
    def clean_ohm_law(e):
        Amper_input.value = ""
        Voltage_input.value = ""
        Resistance_input.value = ""
        
        # Actualizar los campos en la interfaz
        Amper_input.update()
        Voltage_input.update()
        Resistance_input.update()

    # Crear campos de entrada y etiquetas
    Amper_input = ft.TextField(label="Corriente (I):", suffix_text='A')
    Voltage_input = ft.TextField(label="Voltaje (V):", suffix_text='V')
    Resistance_input = ft.TextField(label="Resistencia (Ω):", suffix_text='Ω')

    # Contenedor principal
    content_ohm = ft.Container(
        content=ft.Column(
            controls=[
                Amper_input,
                Voltage_input,
                Resistance_input,
                controls.Buttons(Calcular=calcular_ohm, Limpiar= clean_ohm_law, e=ft.Container),
            ]
        ),
        margin=ft.margin.all(20),
        padding=ft.padding.all(30),
    )


    column = ft.Column(
        controls=[
            controls.header_page(page),
            ft.Container(
                content=content_ohm, 
                margin= ft.margin.only(top= 10, left= 0, right=0)
            ),
        ],
        width=page.width,
        height=page.height
    )

    content = ft.Row(
        controls=[
            column
        ],
        scroll=ft.ScrollMode.ALWAYS,  # Permite scroll horizontal
        width=page.width
    )
    

    stack = ft.Stack(
        [
            controls.background(ft.Container),
            controls.containers(page),
            content,
        ],expand=True
    )
    
    def resized(e):
        column.width = page.width
        column.height = page.height
        content.width = page.width
        page.update()
    
    page.on_resized = resized

    return ft.View(
        "/ley_de_ohm",
        [
            stack,
        ],padding = 0,
        
    )
