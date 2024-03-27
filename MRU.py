import flet as ft
from App_important_controls import header_page, Buttons, cambio_Textfield

def main_MRU(page) -> ft.Page:
    page.title = 'Movimiento Rectilíneo Uniforme'
    distancia = ft.TextField(label='DISTANCIA', suffix_text='m', on_change=cambio_Textfield)
    velocidad = ft.TextField(label='VELOCIDAD', suffix_text='m/s', on_change=cambio_Textfield)
    tiempo = ft.TextField(label='TIEMPO', suffix_text='s',on_change=cambio_Textfield)
    TextFields = ft.Column([distancia, velocidad, tiempo,], expand= True, spacing=40)
    
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))
    
    def Limpiar(e):
        distancia.value = ''
        velocidad.value = ''
        tiempo.value = ''
        page.update()

    def Calcular(e):
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
                distancia.value = f'{T * V}'
            elif velocidad.value == '':
                velocidad.value = f'{D / T}'
            else:
                tiempo.value = f'{D / V}'
        page.update()
    page.add(
        header_page(Volver_main=Volver_main, e=ft.Container),
        ft.Container(TextFields, padding=80),
        Buttons(ft.Container, Calcular=Calcular, Limpiar=Limpiar)
    )

