import flet as ft
from chempy import balance_stoichiometry
from App_important_controls import controls


def Balaceo_estequiometrico_main(page: ft.Page) -> ft.Page:
    page.title = "Balanceo de ecuaciones estequiométricas"
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))
    
    input_reactivos = ft.Ref[ft.TextField]()
    input_productos = ft.Ref[ft.TextField]()
    ecuacion_balanceada = ft.Ref[ft.Text]()
    reactivos_resultado = ft.Ref[ft.Text]()
    productos_resultado = ft.Ref[ft.Text]()
    
    
    
    def balancear_click(e):
        reactivos = input_reactivos.current.value.split(',')
        productos = input_productos.current.value.split(',')

        try:
            reac, prod = balance_stoichiometry(set(reactivos), set(productos))
            ecuacion_balanceada.current.value = format_ecuacion_balanceada(reac, prod)
            reactivos_resultado.current.value = format_formula(reac)
            productos_resultado.current.value = format_formula(prod)
        except Exception as error:
            ecuacion_balanceada.current.value = f"Error: {error}"
            reactivos_resultado.current.value = ""
            productos_resultado.current.value = ""

        page.update()

    def limpiar_click(e):
        input_reactivos.current.value = ""
        input_productos.current.value = ""
        ecuacion_balanceada.current.value = ""
        reactivos_resultado.current.value = ""
        productos_resultado.current.value = ""
        page.update()

    def format_ecuacion_balanceada(reactivos, productos):
        reactivo_str = ' + '.join([f"{value}{key}" if value != 1 else f"{key}" for key, value in reactivos.items()])
        producto_str = ' + '.join([f"{value}{key}" if value != 1 else f"{key}" for key, value in productos.items()])
        return f"Ecuación balanceada: {reactivo_str} -> {producto_str}"

    def format_formula(formula_dict):
        formatted_parts = []
        for key, value in formula_dict.items():
            if value == 1:
                formatted_parts.append(key)
            else:
                formatted_parts.append(f"{value}{key}")

        return ' + '.join(formatted_parts)

    page.add(
        controls.header_page(Volver_main=Volver_main, e=ft.Container),
        ft.TextField(ref=input_reactivos, label="Reactivos"),
        ft.TextField(ref=input_productos, label="Productos"),
        controls.Buttons(ft.Container, Calcular=balancear_click, Limpiar=limpiar_click),
        ft.Text(ref=ecuacion_balanceada),
        ft.Text("Reactivos:"),
        ft.Text(ref=reactivos_resultado),
        ft.Text("Productos:"),
        ft.Text(ref=productos_resultado),
    )