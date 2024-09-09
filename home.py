import flet as ft
from App_important_controls import controls as ct

def home(page: ft.Page) -> ft.View:
    page.title = 'Home'
    page.scroll = ft.ScrollMode.ALWAYS
    
    
    Contenido = ft.Column(
        [
            ft.ElevatedButton(
                'Movimiento Armonico Simple',
                on_click= lambda e: page.go('/MAS')
            ),
            ft.ElevatedButton(
                'ir a Balanceo Estequiometrico',
                on_click= lambda e: page.go('/Balanceo_estequiometrico')
            ),
            ft.ElevatedButton(
                'ir a MRUV (cinematica)',
                on_click=lambda e: page.go('/MRUV')
            ),
            ft.ElevatedButton(
                'valor de una resistencia',
                on_click= lambda e: page.go('/Valor_resistencia')
            ),
            ft.ElevatedButton(
                'Energía mecanica',
                on_click= lambda e: page.go('/Energia_mecanica')
            ),
            ft.ElevatedButton(
                'Ley de Snell',
                on_click= lambda e: page.go('/Ley_de_snell')
            ),
            ft.ElevatedButton(
                'Carga electrica',
                on_click= lambda e: page.go('/Carga_electrica')
            ),
            ft.ElevatedButton(
                'Ley de Coulomb',
                on_click= lambda e: page.go('/ley_de_coulomb')
            ),
            ft.ElevatedButton(
                'Triangulo',
                on_click= lambda e: page.go('/Triangulo')
            ),
            ft.ElevatedButton(
                'porcentaje de error',
                on_click=lambda e: page.go('/Porcentaje_error')
            ),
        ],alignment=ft.MainAxisAlignment.CENTER,
    )
    
    stack = ft.Stack(
        [
            ct.background(ft.Container),
            Contenido,
        ],expand=True
    )
    
    return ft.View(
        '/',
        [
            stack
        ],padding=0
    )