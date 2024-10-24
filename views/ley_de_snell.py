import math 
import flet as ft 
from models.Models import controls
from flet.plotly_chart import PlotlyChart
import numpy as np
import plotly.graph_objects as go

def ley_de_snell(page: ft.Page) -> ft.View:
    page.title = 'Ley de Snell'
    page.scroll = ft.ScrollMode.ALWAYS
        
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
        textfields.update()
     
        
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
            
        theta = np.linspace(angulo, np.pi/2, 100)
        x_arc = x0 + 3 * np.cos(theta)
        y_arc = y0 + 3 * np.sin(theta)
        fig.add_trace(go.Scatter(
            x=x_arc,
            y=y_arc,
            mode='lines',
            line=dict(color='gray', dash='dot'),
            name='Angulo Incidente'
        ))
        fig.add_annotation(text=f'{Angulo_1.value}°',
                   x=x_arc[int(len(x_arc)/2)],
                   y=y_arc[int(len(y_arc)/2)] + 0.5,
                   showarrow=False,
                   font=dict(size=15, color='black'))

        theta2 = np.linspace(angulo2, -np.pi/2, 100)
        x_arc2 = x0 + 3 * np.cos(theta2)
        y_arc2 = y0 + 3 * np.sin(theta2)
        fig.add_trace(go.Scatter(
            x=x_arc2,
            y=y_arc2,
            mode='lines', 
            line=dict(color='gray', dash='dot'), 
            name='Angulo Refractado',
        ))
        
        fig.add_annotation(text=f'{Angulo_2.value}°',
                   x=x_arc2[int(len(x_arc2)/2)],
                   y=y_arc2[int(len(y_arc2)/2)] - 1,
                   showarrow=False,
                   font=dict(size=15, color='black'))

                 
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
        try:
            if Indice_1.value == '':
                I_1 = I_2 * math.sin(A_2) / math.sin(A_1)
                Indice_1.value = f'{round(I_1, 1)}'
                Indice_1.update()
            elif Indice_2.value == '':
                I_2 = I_1 * math.sin(A_1) / math.sin(A_2)
                Indice_2.value = f'{round(I_2, 1)}'
                Indice_2.update()
            elif Angulo_1.value == '':
                A_1 = math.asin(I_2 * math.sin(A_2) / I_1)
                Angulo_1.value = f'{round(math.degrees(A_1,1))}'
                Angulo_1.update()
            elif Angulo_2.value == '':
                A_2 = math.asin(I_1 * math.sin(A_1) / I_2)
                Angulo_2.value = f'{round(math.degrees(A_2),1)}'
                Angulo_2.update()
            light_graph = PlotlyChart(grafica(e,angulo=A_1,angulo2=A_2), expand=True)
            container_grafica.controls.append(light_graph)
        except:
            page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
            page.snack_bar.open = True
            page.update()
        
        
    def other_wave(e,I_1,I_2,A_1,A_2):
        try:
            if Indice_1.value == '':
                I_1 = I_2 * math.sin(A_1) / math.sin(A_2)
                Indice_1.value = f'{round(I_1,1)}'
                Indice_1.update()
            elif Indice_2.value == '':
                I_2 = I_1 * math.sin(A_2) / math.sin(A_1)
                Indice_2.value = f'{round(I_2, 1)}'
                Indice_2.update()
            elif Angulo_1.value == '':
                A_1 = math.asin(math.sin(A_2) * I_1 / I_2)
                Angulo_1.value = f'{round(math.degrees(A_1), 1)}'
                Angulo_1.update()
            elif Angulo_2.value == '':
                A_2 = math.asin(math.sin(A_1) * I_2 / I_1)
                Angulo_2.value = f'{round(math.degrees(A_2), 1)}'
                Angulo_2.update()
            light_graph = PlotlyChart(grafica(e,angulo=A_1,angulo2=A_2), expand=True)
            container_grafica.controls.append(light_graph)
        except:
            page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
            page.snack_bar.open = True
            page.update()
        
            
    def limpiar_ley(e):
        Indice_1.value = ''
        Indice_2.value = ''
        Angulo_1.value= ''
        Angulo_2.value = ''
        try:
            container_grafica.controls.pop()
        except:
            pass
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
       
    
    column = ft.Column(
        controls=[
            controls.header_page(page),
            type_snell,
            textfields,
            controls.Buttons(ft.Container, Calcular=calcular_ley_snell, Limpiar=limpiar_ley),
            container_grafica,
        ],
        scroll=ft.ScrollMode.AUTO,  # Permite scroll vertical
        width=page.width,
        height=page.height
    )
    
    content = ft.Row(
        controls=[
            column
        ],
        scroll=ft.ScrollMode.ALWAYS,  # Permite scroll horizontal
        width=page.width
    )
    

    stack = ft.Stack(
        [
            controls.background(ft.Container),
            controls.containers(page),
            content,
        ],expand=True
    )
    
    def resized(e):
        column.width = page.width
        column.height = page.height
        content.width = page.width
        page.update()
    
    page.on_resized = resized

    
                 
    return ft.View(
        "/Ley_de_snell",
        [
            stack
        ],padding=0,
    )
