from MRU import main_MRU
from Balanceo_estequiometrico import Balaceo_estequiometrico_main
from MRUV import main_MRUV
from Gases_Ideales import main_gases
import flet as ft


def main(page: ft.Page) -> ft.Page:
    page.title = 'KINNEMA'
    page.padding = 40
    
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
    )
    
from Balanceo_estequiometrico import Balaceo_estequiometrico_main
if __name__ == '__main__':
    ft.app(target=main)