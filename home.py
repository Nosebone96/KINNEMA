import flet as ft
from App_important_controls import controls as ct

def home(page: ft.Page) -> ft.View:
    page.title = 'Home'
    page.scroll = ft.ScrollMode.ALWAYS
    
    Contenido = ft.Column(
        [
            ft.OutlinedButton(
                on_click= lambda e: page.go('/MAS'),
                content=ft.Row(
                    controls=[
                        ft.Icon(name=ft.icons.DIRECTIONS_CAR_OUTLINED, color='white'),
                        ft.Text(value='Movimiento Armonico Simple'),   
                    ]
                )
            ),
            ft.OutlinedButton(
                'ir a Balanceo Estequiometrico',
                on_click= lambda e: page.go('/Balanceo_estequiometrico')
            ),
            ft.OutlinedButton(
                'ir a MRUV (cinematica)',
                on_click=lambda e: page.go('/MRUV')
            ),
            ft.OutlinedButton(
                'valor de una resistencia',
                on_click= lambda e: page.go('/Valor_resistencia')
            ),
            ft.OutlinedButton(
                'Energía mecanica',
                on_click= lambda e: page.go('/Energia_mecanica')
            ),
            ft.OutlinedButton(
                'Ley de Snell',
                on_click= lambda e: page.go('/Ley_de_snell')
            ),
            ft.OutlinedButton(
                'Carga electrica',
                on_click= lambda e: page.go('/Carga_electrica')
            ),
            ft.OutlinedButton(
                'Ley de Coulomb',
                on_click= lambda e: page.go('/ley_de_coulomb')
            ),
            ft.OutlinedButton(
                'Triangulo',
                on_click= lambda e: page.go('/Triangulo')
            ),
            ft.OutlinedButton(
                'porcentaje de error',
                on_click=lambda e: page.go('/Porcentaje_error'),
                
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