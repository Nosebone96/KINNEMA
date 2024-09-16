import flet as ft
from Models import controls

def Carga_electrica(page: ft.Page) -> ft.View:
    page.title = 'Carga electrica'
    
    def calculate_electrical_charge(N, elc=1.602e-19): 
        return N * elc 
    
    def calculate_electron_number(Q, elc=1.602e-19):
        return abs(Q) / elc
    
    def calculate_EC(e):
        try:
            if Number_electrons.value:
                N = float(Number_electrons.value)
                Q = calculate_electrical_charge(N)
                Number_electrons.value = f"{N:.2f}"
                Electrical_charge.value = f"{Q:.2e}"
            elif Electrical_charge.value: 
                Q = float(Electrical_charge.value)
                N = calculate_electron_number(Q)
                Electrical_charge.value = f"{Q:.2e}"
                Number_electrons.value = f"{N:.2f}"
            page.update()
        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los valores sean números"))
            page.snack_bar.open = True
            page.update()

    def clean_EC(e):
        Number_electrons.value = ""
        Electrical_charge.value = ""
        page.update()

    Number_electrons = ft.TextField(label="Número de electrones (e)")
    Electrical_charge = ft.TextField(label="Carga eléctrica (C)")

    content_electrical = ft.Container(
         content=ft.Column(
            controls=[
                Number_electrons,
                Electrical_charge,
                controls.Buttons(Calcular=calculate_EC, Limpiar=clean_EC, e=ft.Container),
            ]
        ),
        margin=20,
        padding=30
    )
    return ft.View(
        "/Carga_electrica",
        [
            ft.Column(
                controls=[
                    controls.header_page(page),
                    ft.Container(
                        content=content_electrical, 
                        margin= ft.margin.only(top= 10, left= 0, right=0)
                    ),
                ]
            )
        ],scroll=True
        
    )