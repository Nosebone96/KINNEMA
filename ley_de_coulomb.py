import flet as ft
import math as m
from App_important_controls import controls

def ley_de_coulomb(page: ft.Page) -> ft.Page:
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))

    def calculate_coulomb_law(q1, q2, r):
        """Calcula la fuerza entre dos cargas"""
        Ke = 8.99 * 10**9
        return Ke * ((q1 * q2) / r**2)

    def calculate_charge_2(q1, r, f):
        """Calcula la carga 2"""
        Ke = 8.99 * 10**9
        return f * r**2 / (Ke * q1)

    def calculate_charge_1(q2, r, f):
        """Calcula la carga 1"""
        Ke = 8.99 * 10**9
        return f * r**2 / (Ke * q2)

    def calculate_distance(q1, q2, f):
        """Calcula la distancia entre las cargas"""
        Ke = 8.99 * 10**9
        return m.sqrt(Ke * abs(q1 * q2) / f)

    def clean_cl(e):
        """Limpia los campos de texto"""
        Charge1.value = ""
        Charge2.value = ""
        Distance.value = ""
        Force.value = ""
        page.update()

    def calculate_cl(e):
        try:
            if Charge1.value and Charge2.value and Distance.value:
                q1 = float(Charge1.value.replace('×10^', 'e'))
                q2 = float(Charge2.value.replace('×10^', 'e'))
                r = float(Distance.value.replace('×10^', 'e'))
                f = calculate_coulomb_law(q1, q2, r)
                Charge1.value = "{:.2e}".format(q1).replace('e', '×10^')
                Charge2.value = "{:.2e}".format(q2).replace('e', '×10^')
                Distance.value = "{:.2e}".format(r).replace('e', '×10^')
                Force.value = "{:.2e}".format(f).replace('e', '×10^') + " N"
            elif Charge1.value and Distance.value and Force.value:
                q1 = float(Charge1.value.replace('×10^', 'e'))
                r = float(Distance.value.replace('×10^', 'e'))
                f = float(Force.value.replace('×10^', 'e').replace(' N', ''))
                q2 = calculate_charge_2(q1, r, f)
                Charge1.value = "{:.2e}".format(q1).replace('e', '×10^')
                Charge2.value = "{:.2e}".format(q2).replace('e', '×10^')
                Distance.value = "{:.2e}".format(r).replace('e', '×10^')
                Force.value = "{:.2e}".format(f).replace('e', '×10^') + " N"
            elif Charge2.value and Distance.value and Force.value:
                q2 = float(Charge2.value.replace('×10^', 'e'))
                r = float(Distance.value.replace('×10^', 'e'))
                f = float(Force.value.replace('×10^', 'e').replace(' N', ''))
                q1 = calculate_charge_1(q2, r, f)
                Charge1.value = "{:.2e}".format(q1).replace('e', '×10^')
                Charge2.value = "{:.2e}".format(q2).replace('e', '×10^')
                Distance.value = "{:.2e}".format(r).replace('e', '×10^')
                Force.value = "{:.2e}".format(f).replace('e', '×10^') + " N"
            elif Charge1.value and Charge2.value and Force.value:
                q1 = float(Charge1.value.replace('×10^', 'e'))
                q2 = float(Charge2.value.replace('×10^', 'e'))
                f = float(Force.value.replace('×10^', 'e').replace(' N', ''))
                r = calculate_distance(q1, q2, f)
                Charge1.value = "{:.2e}".format(q1).replace('e', '×10^')
                Charge2.value = "{:.2e}".format(q2).replace('e', '×10^')
                Distance.value = "{:.2e}".format(r).replace('e', '×10^')
                Force.value = "{:.2e}".format(f).replace('e', '×10^') + " N"
            page.update()
        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los valores sean números"))
            page.snack_bar.open = True
            page.update()

    Charge1 = ft.TextField(label="Carga 1 (C)",)
    Charge2 = ft.TextField(label="Carga 2 (C)",)
    Distance = ft.TextField(label="Distancia (m)",)
    Force = ft.TextField(label="Fuerza (N)",)

    content_coulomb = ft.Container(
        content=ft.Column(
            controls=[
                Charge1,
                Charge2,
                Distance,
                Force,
                controls.Buttons(Calcular=calculate_cl, Limpiar=clean_cl, e=ft.Container),
            ]
        ),
        margin=20,
        padding=30
    )

    page.add(
        ft.Column(
            controls=[
                controls.header_page(Volver_main=Volver_main, e=ft.Container),
                ft.Container(
                    content=content_coulomb, 
                    margin= ft.margin.only(top= 10, left= 0, right=0)
                ),
            ]
        )
    )

if __name__ == '__main__': 
 ft.app(target=ley_de_coulomb)