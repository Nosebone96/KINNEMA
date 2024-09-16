import flet as ft
import importlib 
from Models import controls
def main_gases(page: ft.Page) -> ft.View:
    page.title = "Gases Ideales"
    
    def Calcular_boyle(e):
        i = 0
        try:
            volumen_i = float(volumen_inicial_boyle.value)
        except ValueError:
            i+=1
        try:
            volumen_f = float(volumen_final_boyle.value)
        except ValueError:
            i+=1
        try:
            presion_i = float(presion_inicial_boyle.value)
        except ValueError:
            i+=1
        try:
            presion_f = float(presion_final_boyle.value)
        except ValueError:
            i+=1
        if i > 1:
            print('sihola')
            return

        if volumen_inicial_boyle.value == '':
            volumen_inicial_boyle.value = presion_f * volumen_f / presion_i
        if volumen_final_boyle.value == '':
            volumen_final_boyle.value = presion_i * volumen_i / presion_f
        if presion_inicial_boyle.value == '':
            presion_inicial_boyle.value = volumen_f * presion_f / volumen_i
        if presion_final_boyle.value == '':
            presion_final_boyle.value = volumen_i * presion_i / volumen_f
        page.update()
        
    def Limpiar(e):
        pass
    
    volumen_inicial_boyle = ft.TextField(label='Volumen Inicial')
    volumen_final_boyle = ft.TextField(label='Volumen final')
    presion_inicial_boyle = ft.TextField(label='Presión inicial')
    presion_final_boyle= ft.TextField(label='Presión final')
    
    volumen_inicial_charles = ft.TextField(label='Volumen Inicial')
    volumen_final_charles = ft.TextField(label='Volumen final')
    temperatura_inicial_charles = ft.TextField(label='temperatura Inicial')
    temperatura_final_charles = ft.TextField(label='Temperatura final')
    
    presion_inicial_lussac = ft.TextField(label='Presión inicial')
    presion_final_lussac = ft.TextField(label='Presión final')
    temperatura_inicial_lussac = ft.TextField(label='temperatura Inicial')
    temperatura_final_lussac = ft.TextField(label='Temperatura final')
    
    moles = ft.TextField(label='moles')
    
    Ct_boyle = ft.Container(
        content=ft.Column(
            controls=[
                volumen_inicial_boyle, volumen_final_boyle, presion_inicial_boyle, presion_final_boyle,
                controls.Buttons(ft.Container, Calcular=Calcular_boyle, Limpiar=Limpiar),
            ]
        )
    )
    ct_charles = ft.Container(
        content=ft.Column(
            controls=[
                volumen_inicial_charles, volumen_final_charles, temperatura_inicial_charles, temperatura_final_charles
            ]
        )
    )
    ct_lussac = ft.Container(
        content=ft.Column(
            controls=[
                presion_inicial_lussac, presion_final_lussac, temperatura_inicial_lussac, temperatura_final_lussac
            ]
        )
    )


    

    def Volver_main(e):
        page.controls.clear()
        import app
        page.go(app.main(page))

    tabs = ft.Tabs(
        selected_index=0,
        height=500,
        tabs=[
            ft.Tab(text="Boyle", content=Ct_boyle),
            ft.Tab(text="Gay-Lussac", content=ct_lussac),
            ft.Tab(text="Charles", content=ct_charles),
            ft.Tab(text="Combinada"),
            ft.Tab(text="General"),
        ],
    )
    page.add(tabs)
    
    
ft.app(target=main_gases)