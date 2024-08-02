import math 
import flet as ft 
from App_important_controls import controls
from flet.plotly_chart import PlotlyChart
import numpy as np
import plotly.graph_objects as go


def ley_de_snell(page: ft.Page) -> ft.Page:
    page.scroll = ft.ScrollMode.ALWAYS
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))
    
    def change_type_snell(e):
        Indice_1.disabled = False
        Indice_2.disabled = False
        Angulo_1.disabled = False
        Angulo_2.disabled = False
        if type_snell.value == "light":
            Indice_1.label = "Indice de refracción incidente:"
            Indice_2.label = "Indice de refracción refractado:"
        else:
            Indice_1.label = "velocidad de la onda incidente:"
            Indice_2.label = "velocidad de la onda refractada:"
        Indice_1.update()
        Indice_2.update()
        Angulo_1.update()
        Angulo_2.update()
        
    def grafica(e, angulo, angulo2):
        # Crea una figura
        fig = go.Figure()
        
        angulo = angulo + np.pi / 2
        angulo2 = angulo2 - np.pi / 2
        # Define el punto de inicio de la línea
        x0 = 0
        y0 = 0

        # Define la longitud de la línea
        longitud = 10

        # Crea una lista de puntos que se extiendan en la dirección deseada
        x = np.linspace(x0, x0 + (longitud * 2) * np.cos(angulo), 100)
        y = np.linspace(y0, y0 + (longitud * 2) * np.sin(angulo), 100)
        x2 = np.linspace(x0, x0 + (longitud * 2) * np.cos(angulo2), 100)
        y2 = np.linspace(y0, y0 + (longitud * 2) * np.sin(angulo2), 100)

        # Agrega la línea a la figura
        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode='lines',
            name="Onda Incidente"
        ))

        fig.add_trace(go.Scatter(
            x=x2,
            y=y2,
            mode='lines',
            name="onda Refractada"
        ))
         
        # Configura el rango de la gráfica para que se vea la línea hasta el infinito
        fig.update_layout(
            xaxis=dict(
                range=[longitud * -1, longitud + 1],
                title='Eje X',
                gridwidth=1,
                gridcolor='lightgray',
                zeroline=True,
                zerolinewidth=2,
                zerolinecolor='black'
            ),
            yaxis=dict(
                range=[longitud * -1, longitud + 1],
                title='Eje Y',
                gridwidth=1,
                gridcolor='lightgray',
                zeroline=True,
                zerolinewidth=2,
                zerolinecolor='black',
            )
        )
        return fig
        
    
    def calcular_ley_snell(e):
        i = 0
        try:
            I_1 = float(Indice_1.value)
        except ValueError:
            I_1 = 0
            i += 1
        try:
            I_2 = float(Indice_2.value)
        except ValueError:
            I_2 = 0
            i+=1
        try:
            A_1 = float(Angulo_1.value)
            A_1 = math.radians(A_1)
        except ValueError:
            A_1 = 0
            i+=1
        try:
            A_2 = float(Angulo_2.value)
            A_2 = math.radians(A_2)
        except ValueError:
            A_2 = 0
            i+=1
            
        if i >= 2:
            return

        container_grafica.controls.clear()
        if type_snell.value == "light":
            with_light(e,I_1,I_2,A_1,A_2)
        else:
            other_wave(e,I_1,I_2,A_1,A_2)
        page.update()
        
        
        
    def with_light(e,I_1,I_2,A_1,A_2):
        if Indice_1.value == '':
            I_1 = I_2 * math.sin(A_2) / math.sin(A_1)
            Indice_1.value = f'{I_1}'
            Indice_1.update()
        elif Indice_2.value == '':
            I_2 = I_1 * math.sin(A_1) / math.sin(A_2)
            Indice_2.value = f'{I_2}'
            Indice_2.update()
        elif Angulo_1.value == '':
            A_1 = math.asin(I_2 * math.sin(A_2) / I_1)
            Angulo_1.value = f'{math.degrees(A_1)}'
            Angulo_1.update()
        elif Angulo_2.value == '':
            A_2 = math.asin(I_1 * math.sin(A_1) / I_2)
            Angulo_2.value = f'{math.degrees(A_2)}'
            Angulo_2.update()
        light_graph = PlotlyChart(grafica(e,angulo=A_1,angulo2=A_2), expand=True)
        container_grafica.controls.append(light_graph)
        
        
            
    
    def other_wave(e,I_1,I_2,A_1,A_2):
        if Indice_1.value == '':
            I_1 = I_2 * math.sin(A_1) / math.sin(A_2)
            Indice_1.value = f'{I_1}'
            Indice_1.update()
        elif Indice_2.value == '':
            I_2 = I_1 * math.sin(A_2) / math.sin(A_1)
            Indice_2.value = f'{I_2}'
            Indice_2.update()
        elif Angulo_1.value == '':
            A_1 = math.asin(math.sin(A_2) * I_1 / I_2)
            Angulo_1.value = f'{math.degrees(A_1)}'
            Angulo_1.update()
        elif Angulo_2.value == '':
            A_2 = math.asin(math.sin(A_1) * I_2 / I_1)
            Angulo_2.value = f'{math.degrees(A_2)}'
            Angulo_2.update()
        light_graph = PlotlyChart(grafica(e,angulo=A_1,angulo2=A_2), expand=True)
        container_grafica.controls.append(light_graph)
            
    def limpiar_ley(e):
        Indice_1.value = ''
        Indice_2.value = ''
        Angulo_1.value= ''
        Angulo_2.value = ''
        container_grafica.controls.pop()
        page.update()
        
    
          
    type_snell = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="light", label="Luz"),
        ft.Radio(value="wave", label="Otra Onda"),],alignment= ft.MainAxisAlignment.CENTER
    ),on_change=change_type_snell,)
     
     
    Indice_1 = ft.TextField(on_change=controls.cambio_Textfield,suffix_text='i',disabled=True)
    Indice_2 = ft.TextField(on_change=controls.cambio_Textfield,suffix_text='r',disabled=True)
    Angulo_1 = ft.TextField(label="Angulo incidente:", on_change=controls.cambio_Textfield,suffix_text='θi',disabled=True)
    Angulo_2 = ft.TextField(label="Angulo de refracción:", on_change=controls.cambio_Textfield,suffix_text='θr',disabled=True)
    textfields = ft.Container(
        content= ft.Column(
            controls=(
                Indice_1,Indice_2,Angulo_1,Angulo_2
            )
        )
    )
    container_grafica = ft.Row()
                 
    page.add(
        controls.header_page(Volver_main=Volver_main, e=ft.Container),
        type_snell,
        textfields,
        controls.Buttons(ft.Container, Calcular=calcular_ley_snell, Limpiar=limpiar_ley),
        container_grafica,
    )

