from MRU import main_MRU
from Energia_mecanica import main_energia_mecanica
from Balanceo_estequiometrico import Balaceo_estequiometrico_main
from MRUV import main_MRUV
from Gases_Ideales import main_gases
from valor_resistencia import main_valor_resistencia
import flet as ft


def main(page: ft.Page) -> ft.Page:
    page.title = 'KINNEMA'
    page.scroll = ft.ScrollMode.ALWAYS
    page.padding = 15
    
    def new_page_MRU(e):
        page.controls.clear()
        page.go(main_MRU(page))
        
    def new_page_Balanceo_Estequiometrico(e):
        page.controls.clear()
        page.go(Balaceo_estequiometrico_main(page))

    def new_page_Gases_Ideales(e):
        page.controls.clear()
        page.go(main_gases(page))
        
    def new_page_MRUV(e):
        page.controls.clear()
        page.go(main_MRUV(page))
    
    def new_page_Valor_resistencia(e):
        page.controls.clear()
        page.go(main_valor_resistencia(page))
    
    def new_page_energia_mecanica(e):
        page.controls.clear()
        page.go(main_energia_mecanica(page))
    
    page.add(
        ft.ElevatedButton(
            'ir a movimiento Rectilíneo Uniforme',
            on_click=new_page_MRU,
        ),
        ft.ElevatedButton(
            'ir a Balanceo Estequiometrico',
            on_click= new_page_Balanceo_Estequiometrico
        ),
        ft.ElevatedButton(
            'ir a Gases Ideales',
            on_click= new_page_Gases_Ideales
        ),
        ft.ElevatedButton(
            'ir a MRUV (cinematica)',
            on_click=new_page_MRUV
        ),
        ft.ElevatedButton(
            'valor de una resistencia',
            on_click=new_page_Valor_resistencia
        ),
        ft.ElevatedButton(
            'Energía mecanica',
            on_click= new_page_energia_mecanica
        ),
    )
    
from Balanceo_estequiometrico import Balaceo_estequiometrico_main
if __name__ == '__main__':
    ft.app(target=main)