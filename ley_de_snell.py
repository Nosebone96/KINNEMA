import math 
import flet as ft 
from App_important_controls import controls
def ley_de_snell(page: ft.Page) -> ft.Page:
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))
    Indice_1 = ft.TextField(label="Indice de refracción 1:", on_change=controls.cambio_Textfield,suffix_text='i')
    Indice_2 = ft.TextField(label="Indice de refracción 2:", on_change=controls.cambio_Textfield,suffix_text='r')
    Angulo_1 = ft.TextField(label="Angulo incidente:", on_change=controls.cambio_Textfield,suffix_text='θ')
    Angulo_2 = ft.TextField(label="Angulo de refracción:", on_change=controls.cambio_Textfield,suffix_text='θ')
    textfields = ft.Container(
        content= ft.Column(
            controls=(
                Indice_1,Indice_2,Angulo_1,Angulo_2
            )
        )
    )
         
    def calcular_ley_snell(e):
        i = 0
        try:
            I_1 = float(Indice_1.value)
        except ValueError:
            i += 1
        try:
            I_2 = float(Indice_2.value)
        except ValueError:
            i+=1
        try:
            A_1 = float(Angulo_1.value)
        except ValueError:
            i+=1
        try:
            A_2 = float(Angulo_2.value)
        except ValueError:
            i+=1
            
        if i >= 2:
            return
        if Angulo_1.value != "":
            An_1 = (A_1)
        if Angulo_2.value != "":
            An_2 = math.radians(A_2)
        if Indice_1.value == '':
            Indice_1.value = f'{math.radians((I_2*math.sin(An_2))/math.sin(An_1))}'
        if Indice_2.value == '':
            Indice_2.value = f'{(I_1*math.sin(An_1))/math.sin(An_2)}'
        if Angulo_2.value == '':
            Angulo_2.value = f'{math.asin((I_1*math.sin(An_1))/I_2)}'
        if Angulo_1.value == '':
            Angulo_1.value = f'{math.asin((I_2*math.sin(An_2))/I_1)}'
        page.update()
        
    def limpiar_ley(e):
        Indice_1.value = ''
        Indice_2.value = ''
        Angulo_1.value= ''
        Angulo_2.value = ''
        page.update() 
        
    page.add(
        controls.header_page(Volver_main=Volver_main, e=ft.Container),
        textfields,
        controls.Buttons(ft.Container, Calcular=calcular_ley_snell, Limpiar=limpiar_ley)
    )

