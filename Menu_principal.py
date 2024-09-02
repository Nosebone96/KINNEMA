import flet as ft

import home
import Energia_mecanica
import Balanceo_estequiometrico 
import MRUV 
import valor_resistencia 
import ley_de_snell 
import mas 
import Balanceo_estequiometrico 
import ley_de_coulomb 
import Carga_electrica 
import Triangulo

import plotly.io as pio
pio.renderers.default = 'svg'
from plotly.graph_objects import *
from flet.plotly_chart import *



def main(page: ft.Page) -> ft.Page:
    page.title = 'KINNEMA'
    page.scroll = ft.ScrollMode.ALWAYS
    page.padding = 15
    #page.views.scroll = True
    page.window_bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT
    
    def change_route(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(home.home(page))
        elif page.route == "/Valor_resistencia":
            page.views.append(valor_resistencia.main_valor_resistencia(page))
        elif page.route == "/MRUV":
            page.views.append(MRUV.main_MRUV(page)) 
        elif page.route == "/MAS":
            page.views.append(mas.main_mas(page)) 
        elif page.route == "/Ley_de_snell":
            page.views.append(ley_de_snell.ley_de_snell(page)) 
        elif page.route == "/ley_de_coulomb":
            page.views.append(ley_de_coulomb.ley_de_coulomb(page)) 
        elif page.route == "/Energia_mecanica":
            page.views.append(Energia_mecanica.main_energia_mecanica(page)) 
        elif page.route == "/Carga_electrica":
            page.views.append(Carga_electrica.Carga_electrica(page)) 
        elif page.route == "/Balanceo_estequiometrico":
            page.views.append(Balanceo_estequiometrico.Balaceo_estequiometrico_main(page))
        elif page.route == "/Triangulo":
            page.views.append(Triangulo.main_triangulo(page))
        page.update()
            
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
        
    page.on_route_change = change_route
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)
    


