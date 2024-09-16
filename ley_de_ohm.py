import flet as ft 

def ley_de_ohm(page: ft.Page) -> ft.View:
    page.title = 'Ley de ohm'
    page.scroll = ft.ScrollMode.ALWAYS
    
    def calculate_resistance(voltage, Amper):
        return voltage / Amper
    def calculate_voltage(Amper, resistance):
        return resistance * Amper
    def calculate_Amper(voltage, resistance):
        return voltage / resistance
    
    def calculate_ohm(e):
        return 0
    
    