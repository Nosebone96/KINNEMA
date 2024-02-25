import flet as ft

def main(page):
    Distancia = ft.TextField(label='Distancia')
    Velocidad = ft.TextField(label='Velocidad')
    Tiempo = ft.TextField(label='Tiempo')
    V_inicial = ft.TextField(label='Velocidad Inicial')
    V_final = ft.TextField(label='Velocidad Final')
    
    page.add()
    
    
ft.app(target=main)