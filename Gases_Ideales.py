import flet as ft
import importlib 

def main_gases(page):
    page.title = "Gases Ideales"
    P1 = ft.TextField(label='Presión 1')
    P2 = ft.TextField(label="Presión 2")
    V1 = ft.TextField(label="Volumen 1")
    V2 = ft.TextField(label="Volumen 2")
    T1 = ft.TextField(label="Temperatura 1")
    T2 = ft.TextField(label="Temperatura 2")
    n = ft.TextField(label="Moles")
    TextFields = ft.Column([P1, P2, V1, V2, T1, T2, n], expand= True, spacing=30)
    def Volver_main(e):
        page.controls.clear()
        page.go(importlib.import_module('Menu_principal').main(page))

    def limpiar(e):
        P1.value = ''
        P2.value = ''
        V1.value = ''
        V2.value = ''
        T1.value = ''
        T2.value = ''
        n.value = ''

    def calcular(e):
        i = 0
        try:
            p1 = float(P1.value)
        except ValueError:
            i += 1
        try:
            p2 = float(P2.value)
        except ValueError:
            i += 1
        try:
            v1 = float(V1.value)
        except ValueError:
            i += 1
        try:
            v2 = float(V2.value)
        except ValueError:
            i += 1
        try:
            t1 = float(T1.value)
        except ValueError:
            i += 1
        try:
            t2 = float(T2.value)
        except ValueError:
            i += 1
        try:
            N = float(n.value)
        except ValueError:
            i += 1

        if i > 1:
            return
        else:
            # Ley de Boyle
            if P1.value != '' and V1.value != '' and P2.value == '' and V2.value != '':
                P2.value = f'{(p1 * v1) / v2} atm'
            elif P1.value == '' and V1.value != '' and P2.value != '' and V2.value != '':
                P1.value = f'{(p2 * v2) / v1} atm'
            elif P1.value != '' and V1.value == '' and P2.value != '' and V2.value != '':
                V1.value = f'{(p2 * v2) / p1} L'
            elif P1.value != '' and V1.value != '' and P2.value != '' and V2.value == '':
                V2.value = f'{(p1 * v1) / p2} L'
            
            # Ley de Charles
            elif V1.value != '' and T1.value != '' and V2.value == '' and T2.value != '':
                V2.value = f'{(v1 * t2) / t1} L'
            elif V1.value == '' and T1.value != '' and V2.value != '' and T2.value != '':
                V1.value = f'{(v2 * t1) / t2} L'
            elif V1.value != '' and T1.value == '' and V2.value != '' and T2.value != '':
                T1.value = f'{(v1 * t2) / v2} K'
            elif V1.value != '' and T1.value != '' and V2.value != '' and T2.value == '':
                T2.value = f'{(v2 * t1) / v1} K'

            # Ley de Gay-Lussac
            elif P1.value != '' and T1.value != '' and P2.value == '' and T2.value != '':
                P2.value = f'{(p1 * t2) / t1} atm'
            elif P1.value == '' and T1.value != '' and P2.value != '' and T2.value != '':
                P1.value = f'{(p2 * t1) / t2} atm'
            elif P1.value != '' and T1.value == '' and P2.value != '' and T2.value != '':
                T1.value = f'{(p1 * t2) / p2} K'
            elif P1.value != '' and T1.value != '' and P2.value != '' and T2.value == '':
                T2.value = f'{(p2 * t1) / p1} K'

             # Ley combinada de los gases
            elif P1.value != '' and V1.value != '' and T1.value != '' and P2.value == '' and V2.value != '' and T2.value != '':
                P2.value = f'{(p1 * v1 * t2) / (v2 * t1)} atm'
            elif P1.value == '' and V1.value != '' and T1.value != '' and P2.value != '' and V2.value != '' and T2.value != '':
                P1.value = f'{(p2 * v2 * t1) / (v1 * t2)} atm'
            elif P1.value != '' and V1.value == '' and T1.value != '' and P2.value != '' and V2.value != '' and T2.value != '':
                V1.value = f'{(p2 * v2 * t1) / (p1 * t2)} L'
            elif P1.value != '' and V1.value != '' and T1.value == '' and P2.value != '' and V2.value != '' and T2.value != '':
                T1.value = f'{(p2 * v2 * t1) / (p1 * v1)} K°'
            elif P1.value != '' and V1.value != '' and T1.value != '' and P2.value != '' and V2.value == '' and T2.value != '':
                V2.value = f'{(p1 * v1 * t2) / (p2 * t1)} L'
            elif P1.value != '' and V1.value != '' and T1.value != '' and P2.value != '' and V2.value != '' and T2.value == '':
                T2.value = f'{(p1 * v1 * t2) / (p2 * v2)} K°'

            #Ley general o ecuación de estado: P*V = n*R*T
            R = 0.0821  
        if P1.value == '' and V1.value != '' and n.value != '' and T1.value != '':
            P1.value = f'{(N * R * t1) / v1} atm'
        elif P1.value != '' and V1.value == '' and n.value != '' and T1.value != '':
            V1.value = f'{(N * R * t1) / p1} L'
        elif P1.value != '' and V1.value != '' and n.value == '' and T1.value != '':
            n.value = f'{(p1 * v1) / (R * t1)} moles'
        elif P1.value != '' and V1.value != '' and n.value != '' and T1.value == '':
            T1.value = f'{(p1 * v1) / (N * R)} K'
                
    page.update()

    page.add(
    importlib.import_module('App_important_controls').header_page(ft.Container, Volver_main),
    ft.Container(TextFields, padding=80),
    ft.Row([
        ft.ElevatedButton(
            'calcular',
            on_click=calcular,                
            icon=ft.icons.CALCULATE,
            style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)),
            icon_color='green',
            height=50,
            width=150,
        ),
        ft.ElevatedButton(
            'limpiar',
            on_click=limpiar,
            icon=ft.icons.CLEANING_SERVICES,
            style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)),
            height=50,
            width=150,
            icon_color="red",
        ),
    ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START, height=50)
)