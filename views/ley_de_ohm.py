import flet as ft
from models.Models import controls 

def main_ohm_law(page: ft.Page):
    page.scroll = ft.ScrollMode.HIDDEN

    # Funciones para calcular ley de Ohm
    def calculate_voltage(amper, resistance):
        return amper * resistance

    def calculate_amper(voltage, resistance):
        if resistance == 0:
            print("La resistencia no puede ser cero.")
            return None
        return voltage / resistance

    def calculate_resistance(amper, voltage):
        if amper == 0:
            print("La corriente no puede ser cero.")
            return None
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
                if amper is None:
                    return
                Amper_input.value = f"{amper:.2f}"
                Voltage_input.value = f"{voltage:.2f}"
                Resistance_input.value = f"{resistance:.2f}"
            elif Amper_input.value and Voltage_input.value:
                voltage = float(Voltage_input.value)
                amper = float(Amper_input.value)
                resistance = calculate_resistance(amper, voltage)
                if resistance is None:
                    return
                Amper_input.value = f"{amper:.2f}"
                Voltage_input.value = f"{voltage:.2f}"
                Resistance_input.value = f"{resistance:.2f}"
            else:
                print("Valores inválidos")
                return
        except ValueError as e:
            print(f"Valores inválidos, error: {e}")
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
                ft.ElevatedButton(text="Calcular", on_click=calcular_ohm),
                ft.ElevatedButton(text="Limpiar", on_click=clean_ohm_law)
            ]
        ),
        margin=ft.margin.all(20),
        padding=ft.padding.all(30)
    )

    # Agregar el contenido a la página
    page.add(content_ohm)
    return ft.View(
        "/ley_de_ohm.py",
        [
            ft.Column(
                controls=[
                    controls.header_page(page),
                    ft.Container(
                        content=content_ohm, 
                        margin= ft.margin.only(top= 10, left= 0, right=0)
                    ),
                ]
            )
        ],scroll=True
        
    )
