import flet as ft
import importlib 
from App_important_controls import controls
def main_gases(page: ft.Page):
    page.title = "Gases Ideales"

    volumen_inicial = ft.TextField(label='Volumen Inicial')
    volumen_final = ft.TextField(label='Volumen final')
    temperatura_inicial = ft.TextField(label='temperatura Inicial')
    temperatura_final = ft.TextField(label='Temperatura final')
    presion_inicial = ft.TextField(label='Presión inicial')
    presion_final = ft.TextField(label='Presión final')
    moles = ft.TextField(label='moles')

    textfields=ft.Column(
        controls=(
            ft.TextField(label='grupo de textfields'),  
        ),
    )
    Contenido = ft.Container(
        content=textfields
    )
    
    def elegir_formula(e):
        Contenido.visible = False
        if Eleccion_formula.value == 'Boyle':
            textfields.visible(volumen_inicial, volumen_final, presion_inicial, presion_final)
        elif Eleccion_formula.value == 'Lussac':
            ...
        elif Eleccion_formula.value == 'Charles':
            ...
        elif Eleccion_formula.value == 'Combinada':
            ...
        elif Eleccion_formula.value == 'General':
            ...
        else:
            print('no se ha elegido ningún elemento')
    
    
    

    Eleccion_formula = ft.RadioGroup(content=ft.Row([
        ft.Radio(value='Boyle',label="Boyle"),
        ft.Radio(value='Lussac',label="Gay Lussac"),
        ft.Radio(value='Charles',label="Charles"),
        ft.Radio(value='Combinada',label="Combinada"),
        ft.Radio(value='General',label="General"),]), on_change=elegir_formula)
    
    page.add(Eleccion_formula, textfields)
    
ft.app(target=main_gases)