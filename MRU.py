import flet as ft
import importlib


def main_MRU(page):
    page.title = 'Movimiento Rectilíneo Uniforme'
    distancia = ft.TextField(label='DISTANCIA')
    velocidad = ft.TextField(label='VELOCIDAD')
    tiempo = ft.TextField(label='TIEMPO')
    TextFields = ft.Column([distancia, velocidad, tiempo,], expand= True, spacing=40)
    
    def Volver_main(e):
        page.controls.clear()
        page.go(importlib.import_module('Menu_principal').main(page))
    
    def limpiar(e):
        distancia.value = ''
        velocidad.value = ''
        tiempo.value = ''
        page.update()

    def verificar_formato(e):
        i = 0
        D = V = T = 0
        try:
            D = float(distancia.value)
        except ValueError:
            i += 1
        try:
            T = float(tiempo.value)
        except ValueError:
            i += 1
        try:
            V = float(velocidad.value)
        except ValueError:
            i += 1  
        if i > 1:
            return
        else:
            if distancia.value == '':
                distancia.value = f'{T * V}m'
            elif velocidad.value == '':
                velocidad.value = f'{D / T}m/s'
            else:
                tiempo.value = f'{D / V}s'
        page.update()
    page.add(
        importlib.import_module('App_important_controls').header_page(ft.Container, Volver_main),
        ft.Container(TextFields, padding=80),
        ft.Row([
            ft.ElevatedButton(
                'calcular',
                on_click=verificar_formato,                
                icon=ft.icons.CALCULATE,
                style= ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30),),
                icon_color='green',
                height= 50,
                width= 150,
                ),
            ft.ElevatedButton('limpiar',
                on_click=limpiar,
                icon= ft.icons.CLEANING_SERVICES,
                style= ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30),),
                height= 50,
                width= 150,
                icon_color="red",
                ),
            ], alignment= ft.MainAxisAlignment.CENTER, vertical_alignment= ft.CrossAxisAlignment.START, height=50,)
    )

