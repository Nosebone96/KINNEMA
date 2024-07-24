from Energia_mecanica import main_energia_mecanica
from Balanceo_estequiometrico import Balaceo_estequiometrico_main
from MRUV import main_MRUV
from valor_resistencia import main_valor_resistencia
from ley_de_snell import ley_de_snell
from mas import main_mas
from Balanceo_estequiometrico import Balaceo_estequiometrico_main
from chempy import balance_stoichiometry
import flet as ft
from plotly.graph_objects import *
from flet.plotly_chart import *
import plotly.io as pio
pio.renderers.default = 'svg'


def main(page: ft.Page) -> ft.Page:
    page.title = 'KINNEMA'
    page.padding = 15
        
    def new_page_Balanceo_Estequiometrico(e):
        page.controls.clear()
        page.go(Balaceo_estequiometrico_main(page))

    def new_page_MRUV(e):
        page.controls.clear()
        page.go(main_MRUV(page))
    
    def new_page_Valor_resistencia(e):
        page.controls.clear()
        page.go(main_valor_resistencia(page))
    
    def new_page_energia_mecanica(e):
        page.controls.clear()
        page.go(main_energia_mecanica(page))
    def new_page_energia_ley_Snell(e):
        page.controls.clear()
        page.go(ley_de_snell(page))
    def new_page_MAS(e):
        page.controls.clear()
        page.go(main_mas(page))
    
    page.add(
        ft.ElevatedButton(
            'ir a Balanceo Estequiometrico',
            on_click= new_page_Balanceo_Estequiometrico
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
        ft.ElevatedButton(
            'Ley de Snell',
            on_click= new_page_energia_ley_Snell
        ),
        ft.ElevatedButton(
            'Movimiento Armonico Simple',
            on_click=new_page_MAS
        )
    )
    

if __name__ == '__main__':
    ft.app(target=main)