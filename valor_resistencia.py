import flet as ft
from flet import colors
from App_important_controls import controls

def main_valor_resistencia(page: ft.Page) -> ft.Page:
    
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))
    
    color_map = {
        'negro': colors.BLACK,
        'marron': colors.BROWN,
        'rojo': colors.RED,
        'naranja': colors.ORANGE,
        'amarillo': colors.YELLOW,
        'verde': colors.GREEN,
        'azul': colors.BLUE,
        'violeta': colors.PURPLE,
        'gris': colors.GREY,
        'blanco': colors.WHITE,
        'dorado': colors.AMBER,
        'plateado': colors.BROWN_200
    }
    
    resistance_values = {
        'negro': 0,
        'marron': 1,
        'rojo': 2,
        'naranja': 3,
        'amarillo': 4,
        'verde': 5,
        'azul': 6,
        'violeta': 7,
        'gris': 8,
        'blanco': 9,
    }
    
    Dropdown_options = [
        ft.dropdown.Option('negro'),
        ft.dropdown.Option('marron'),
        ft.dropdown.Option('rojo'),
        ft.dropdown.Option('naranja'),
        ft.dropdown.Option('amarillo'),
        ft.dropdown.Option('verde'),
        ft.dropdown.Option('azul'),
        ft.dropdown.Option('violeta'),
        ft.dropdown.Option('gris'),
        ft.dropdown.Option('blanco'),
    ]
    tolerance_options =[
        ft.dropdown.Option('plateado'),
        ft.dropdown.Option('dorado'),
        ft.dropdown.Option('marron'),
        ft.dropdown.Option('rojo'),
        ft.dropdown.Option('verde'),
        ft.dropdown.Option('azul'),
        ft.dropdown.Option('violeta'),
    ]
    
    
    def dropdown_changed(e):
        dropdown = e.control
        container = dropdowns_to_containers[dropdown]
        container.bgcolor = color_map[dropdown.value]
        page.update()
    
    def calcular(e):
        try:
            resistance_value_1 = resistance_values[banda1.value]
            resistance_value_2 = resistance_values[banda2.value]
            multiplicador_value = resistance_values[multiplicador.value]
            #tolerancia_value = resistance_values[tolerancia.value]

            # Calculate the resistance value based on the selected options
            resistance_value = resistance_value_1 * 10 + resistance_value_2
            resistance_value *= 10 ** multiplicador_value
            # Display the resistance value
            resultado.value = f"el valor de la resistencia es: {resistance_value}Ω"
            porcentaje_tolerancia: float
            if tolerancia.value == 'plateado':
                porcentaje_tolerancia = 10
            elif tolerancia.value == 'dorado':
                porcentaje_tolerancia = 5
            elif tolerancia.value == 'marron':
                porcentaje_tolerancia = 1
            elif tolerancia.value == 'rojo':
                porcentaje_tolerancia = 5
            elif tolerancia.value == 'verde':
                porcentaje_tolerancia = 0.5
            elif tolerancia.value == 'azul':
                porcentaje_tolerancia = 0.25
            elif tolerancia.value == 'violeta':
                porcentaje_tolerancia = 0.1
            valor_tolerancia.value = f'la tolerancia (±{porcentaje_tolerancia}%) va desde {resistance_value - resistance_value * (porcentaje_tolerancia / 100)}Ω hasta {resistance_value + resistance_value * (porcentaje_tolerancia / 100)}Ω'
        except ValueError:
            print('ha ocurrido un error en el formato de las bandas :(')
        page.update()
    def limpiar(e):
        color_banda_1.bgcolor = colors.BROWN_200
        color_banda_2.bgcolor = colors.BROWN_200
        color_multiplicador.bgcolor = colors.BROWN_200
        color_tolerancia.bgcolor = colors.BROWN_200
        banda1.value = ''
        banda2.value = ''
        multiplicador.value = ''
        tolerancia.value = ''
        valor_tolerancia.value = ''
        resultado.value = ''
        page.update()
    
    color_banda_1 = ft.Container(
        width=10,
        bgcolor=colors.BROWN_200,
        margin = ft.margin.only(right=10, left=60)
    )
    color_banda_2 = ft.Container(
        width= 1,
        bgcolor=colors.BROWN_200,
        margin = ft.margin.symmetric(horizontal=35)
    )
    
    color_multiplicador = ft.Container(
        width=10,
        bgcolor=colors.BROWN_200,
        margin = ft.margin.symmetric(horizontal=35)
    )
    color_tolerancia = ft.Container(
        width=10,
        bgcolor=colors.BROWN_200,
        margin = ft.margin.only(right=60, left=10)
    )
    resultado = ft.Text(size=20, color= colors.CYAN_ACCENT_200)
    valor_tolerancia = ft.Text(size=20, color= colors.CYAN_ACCENT_200)
    pata_resistencia = ft.Container(height=10, width=40, bgcolor=colors.BROWN_200,)
    Color_1 = ft.Container(bgcolor=colors.BROWN_50, width=100, height=150, border_radius= ft.border_radius.horizontal(left=40, right=10),content=color_banda_1)
    Color_2 = ft.Container(bgcolor=colors.BROWN_50, width=100, height=130, border_radius= ft.border_radius.horizontal(left=1), content=color_banda_2)
    Color_4 = ft.Container(bgcolor=colors.BROWN_50, width=100, height=130, border_radius= ft.border_radius.horizontal(right=1), content= color_multiplicador)
    Color_5 = ft.Container(bgcolor=colors.BROWN_50, width=100, height=150, border_radius= ft.border_radius.horizontal(left=10, right=40), content=color_tolerancia)
    banda1 = ft.Dropdown(options=Dropdown_options, width=100, label= 'banda 1', expand= True, on_change=dropdown_changed)
    banda2= ft.Dropdown(options=Dropdown_options, width=100, label='banda 2', expand= True, on_change=dropdown_changed)
    multiplicador = ft.Dropdown(options=Dropdown_options, width=150,label='multiplicador', expand= True, on_change=dropdown_changed)
    tolerancia = ft.Dropdown(options=tolerance_options, width=100, label='tolerancia', expand= True, on_change=dropdown_changed)
    dropdowns = ft.Row(
        controls=[banda1, banda2, multiplicador, tolerancia],
    )
    draw_resistance = ft.Row(
        controls=[
            pata_resistencia, Color_1, Color_2, Color_4, Color_5, pata_resistencia
        ],spacing=0, alignment= 'CENTER'
    )     
    
    dropdowns_to_containers = {
        banda1: color_banda_1,
        banda2: color_banda_2,
        multiplicador: color_multiplicador,
        tolerancia: color_tolerancia,
    }
    
    page.add(
        controls.header_page(Volver_main=Volver_main, e=ft.Container),
        dropdowns,
        ft.Divider(height=50, thickness=0),
        draw_resistance,
        ft.Divider(height=50, thickness=0),
        controls.Buttons(ft.Container, Calcular=calcular, Limpiar=limpiar),
        resultado,
        valor_tolerancia
    )