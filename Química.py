import flet as ft
from chempy import balance_stoichiometry

def main(page):
    input_reactivos = ft.Ref[ft.TextField]()
    input_productos = ft.Ref[ft.TextField]()
    ecuacion_balanceada = ft.Ref[ft.Text]()

    def balancear_click(e):
        reactivos = input_reactivos.current.value.split(',')
        productos = input_productos.current.value.split(',')

        try:
            reac, prod = balance_stoichiometry(set(reactivos), set(productos))
            ecuacion_balanceada.current.value = (
                f"Ecuación Balanceada:\nReactivos: {format_formula(reac)}\nProductos: {format_formula(prod)}"
            )
        except Exception as error:
            ecuacion_balanceada.current.value = f"Error: {error}"

        page.update()

    def format_formula(formula_dict):
        formatted_parts = []
        for key, value in formula_dict.items():
            if value == 1:
                formatted_parts.append(key)
            else:
                formatted_parts.append(f"{value}{key}")

        return ' + '.join(formatted_parts)

    page.add(
        ft.TextField(ref=input_reactivos, label="Reactivos"),
        ft.TextField(ref=input_productos, label="Productos"),
        ft.ElevatedButton("Balancear Ecuación", on_click=balancear_click),
        ft.Text(ref=ecuacion_balanceada),
    )

ft.app(target=main)
