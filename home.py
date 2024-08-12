import flet as ft

def home(page: ft.Page) -> ft.View:
    page.title = 'Home'
    return ft.View(
        '/',
        [
            ft.ElevatedButton(
            'ir a Balanceo Estequiometrico',
            on_click= lambda e: page.go('/Balanceo_Estequiometrico')
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
                on_click= lambda e: page.go('/energia_mecanica')
            ),
            ft.ElevatedButton(
                'Ley de Snell',
                on_click= lambda e: page.go('/energia_ley_Snell')
            ),
            ft.ElevatedButton(
                'Movimiento Armonico Simple',
                on_click= lambda e: page.go('/MAS')
            ),
            ft.ElevatedButton(
                'Carga electrica',
                on_click= lambda e: page.go('/Carga_electrica')
            ),
            ft.ElevatedButton(
                'Ley de Coulomb',
                on_click= lambda e: page.go('/ley_de_coulomb')
            ),
        ]
    )