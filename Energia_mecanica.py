import flet as ft
import math
from App_important_controls import controls

def main_energia_mecanica(page: ft.Page) -> ft.Page:
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))
    
    def Calcular_EC(e):
        i = 0
        try:
            E_cinetica = float(Energia_cinetica.value)
        except ValueError:
            i += 1
        try:
            masa = float(Masa_EC.value)
        except ValueError:
            i+=1
        try:
            velocidad = float(Velocidad_EC.value)
        except ValueError:
            i+=1
        if i >= 2:
            return
        
        if Energia_cinetica.value == '':
            Energia_cinetica.value = f'{(masa * velocidad**2) / 2}'
        if Masa_EC.value == '':
            Masa_EC.value = f'{2 * E_cinetica / velocidad**2}'
        if Velocidad_EC.value == '':
            Velocidad_EC.value = f'{math.sqrt(2*E_cinetica / masa)}'
        Cinetica.value = Energia_cinetica.value
        On_suma_fuerzas(e)
        page.update()
        
        
    def Limpiar_EC(e):
        Energia_cinetica.value = ''
        Masa_EC.value = ''
        Velocidad_EC.value = ''
        page.update()
    
    def Calcular_EPG(e):
        gravedad = 9.8
        i = 0
        try:
            EPG = float(Energia_potencial_gravitacional.value)
        except ValueError:
            i += 1
        try:
            masa = float(Masa_EPG.value)
        except ValueError:
            i+=1
        try:
            altura = float(Altura.value)
        except ValueError:
            i+=1
        if i >= 2:
            return
        if Energia_potencial_gravitacional.value == '':
            Energia_potencial_gravitacional.value = f'{masa * gravedad * altura}'
        if Masa_EPG.value == '':
            Masa_EPG.value = f'{EPG / (gravedad * altura)}'
        if Altura.value == '':
            Altura.value = f'{EPG / (gravedad * masa)}'
        Potencial_G.value = Energia_potencial_gravitacional.value
        On_suma_fuerzas(e)
        page.update()
            
            
    def Limpiar_EPG(e):
        Energia_potencial_gravitacional.value = ''
        Masa_EPG.value = ''
        Altura.value = ''
        page.update()
            
    def Calcular_EPE(e):
        i = 0
        try:
            EPE = float(energia_potencial_Elastica.value)
        except ValueError:
            i += 1
        try:
            CE = float(Constante_Elasticidad.value)
        except ValueError:
            i+=1
        try:
            distancia = float(Distancia.value)
        except ValueError:
            i+=1
        if i >= 2:
            return
        if energia_potencial_Elastica.value == '':
            energia_potencial_Elastica.value = f'{CE * distancia**2 / 2}'
        if Distancia.value == '':
            Distancia.value = f'{math.sqrt(2 * EPE / CE)}'
        if Constante_Elasticidad.value == '':
            Constante_Elasticidad.value = f'{EPE * 2 / distancia**2}'
        Potencial_E.value = energia_potencial_Elastica.value
        On_suma_fuerzas(e)
        page.update()
        
        
    def Limpiar_EPE(e):
        energia_potencial_Elastica.value = ''
        Constante_Elasticidad.value = ''
        Distancia.value = ''
        page.update()
    
    def On_suma_fuerzas(e):
        cinetica = 0
        gravitacional = 0
        elastica = 0
        try:
            cinetica = float(Cinetica.value)
        except ValueError:
            cinetica = 0
        try:
            gravitacional = float(Potencial_G.value)
        except ValueError:
            gravitacional = 0
        try:
            elastica = float(Potencial_E.value)
        except ValueError:
            elastica = 0
        suma_fuerzas.value = f'{cinetica + gravitacional + elastica}'
        page.update()
        
        
        

    Energia_cinetica = ft.TextField(label="energía cinetica:", on_change=controls.cambio_Textfield,suffix_text='J')
    Masa_EC = ft.TextField(label='Masa:', on_change=controls.cambio_Textfield, suffix_text='kg')
    Velocidad_EC = ft.TextField(label='Velocidad:', on_change=controls.cambio_Textfield, suffix_text='m/s')
    
    Energia_potencial_gravitacional = ft.TextField(label='Energía Potencial Gravitacional:', on_change=controls.cambio_Textfield, suffix_text='J')
    Masa_EPG = ft.TextField(label='Masa:', on_change=controls.cambio_Textfield, suffix_text='kg')
    Altura = ft.TextField(label='Altura', on_change=controls.cambio_Textfield, suffix_text='m')
    
    energia_potencial_Elastica = ft.TextField(label='Energia Potencial Elástica', on_change=controls.cambio_Textfield, suffix_text='J')
    Constante_Elasticidad = ft.TextField(label='Constante de Elasticidad', on_change=controls.cambio_Textfield,suffix_text='N/m')
    Distancia = ft.TextField(label='distancia', on_change=controls.cambio_Textfield, suffix_text='m')
    
    suma_fuerzas = ft.TextField(label='Sumatoria De Fuerzas:', disabled=True, suffix_text='J')
    Cinetica = ft.TextField(label='Energía Cinetica', on_change=On_suma_fuerzas, suffix_text='J')
    Potencial_G = ft.TextField(label='Energía Potencial Gravitacional', on_change=On_suma_fuerzas, suffix_text='J')
    Potencial_E = ft.TextField(label='Energía Potencial Elastica', on_change=On_suma_fuerzas, suffix_text='J')
    
    
    
    
    content_cinetica = ft.Container(
        content=(
            ft.Column(
                controls=(
                    Energia_cinetica,
                    Masa_EC,
                    Velocidad_EC,
                    controls.Buttons(Calcular=Calcular_EC, Limpiar= Limpiar_EC, e=ft.Container),
                )   
            )
        ), margin=20, padding= 30  
    )
    
    
    Co_energia_potencial_G = ft.Container(
        content=(
            ft.Column(
                controls=(
                    Energia_potencial_gravitacional,
                    Masa_EPG,
                    Altura,
                    controls.Buttons(Calcular=Calcular_EPG, Limpiar=Limpiar_EPG, e=ft.Container),
                )
            )
        ), margin=20, padding= 30  
    )
    Energia_potencial_E = ft.Container(
        content=ft.Column(
            controls=(
                energia_potencial_Elastica,
                Constante_Elasticidad,
                Distancia,
                controls.Buttons(Calcular=Calcular_EPE, Limpiar=Limpiar_EPE, e=ft.Container),
            )
        ), margin=20, padding= 30  
    )
    Sumatoria_fuerzas = ft.Container(
        content=(
            ft.Column(
                controls=(
                    Cinetica,
                    Potencial_G,
                    Potencial_E,
                    suma_fuerzas,
                )
            )
        ), margin=20, padding= 30 
    )
               
    Tabs_mecanica = ft.Tabs(
        selected_index=0,
        animation_duration=400,
        tabs=[
            ft.Tab(
                text = 'Energía Cinética',
                content=content_cinetica,
            ),
            ft.Tab(
                text = 'Energía Potencial Gravitacional',
                content=Co_energia_potencial_G
            ),
            ft.Tab(
                text='Energía Potencial Elástica',
                content=Energia_potencial_E,
            ),
            ft.Tab(
                text='Sumatoria de Fuerzas',
                content=Sumatoria_fuerzas,
            )
        ]
    )
    
    page.add(
        ft.Column(
            controls=[
                controls.header_page(Volver_main=Volver_main, e=ft.Container),
                ft.Container(
                    content=Tabs_mecanica, 
                    margin= ft.margin.only(top= 10, left= 0, right=0)
                ),
            ]
        )
    )
