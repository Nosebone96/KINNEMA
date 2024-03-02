import flet as ft
import importlib

def main(page: ft.Page):
    page.title = 'KINNEMA'
    page.padding = 40
    
    def new_page_MRU(e):
        page.controls.clear()
        page.go(importlib.import_module('MRU').main_MRU(page))
        
    def new_page_Balanceo_Estequiometrico(e):
        page.controls.clear()
        page.go(importlib.import_module('Balanceo_estequiometrico').main(page))

    def new_page_Gases_Ideales(e):
        page.controls.clear()
        page.go(importlib.import_module('Gases_Ideales').main_gases(page))
        
    def new_page_MRUV(e):
        page.controls.clear()
        page.go(importlib.import_module('MRUV').main_MRUV(page))
    
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
    

if __name__ == '__main__':
    ft.app(target=main)