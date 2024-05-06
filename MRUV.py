import flet as ft
import plotly.io as pio
import plotly.graph_objects as go
from flet.plotly_chart import PlotlyChart

from App_important_controls import controls
import math as m

def main_MRUV(page: ft.Page):
    pio.renderers.default = 'svg'
    page.scroll = ft.ScrollMode.ALWAYS
    page.title = 'Movimiento Rectilíneo Uniformemente Variado'
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))
        
    Distancia = ft.TextField(label='Distancia', suffix_text='m', on_change=controls.cambio_Textfield)
    Aceleracion = ft.TextField(label='Aceleracion', suffix_text='m/s²', on_change=controls.cambio_Textfield)
    Tiempo = ft.TextField(label='Tiempo', suffix_text='s', on_change=controls.cambio_Textfield)
    V_inicial = ft.TextField(label='Velocidad Inicial', suffix_text='m/s', on_change=controls.cambio_Textfield)
    V_final = ft.TextField(label='Velocidad Final', suffix_text='m/s', on_change=controls.cambio_Textfield)
    textfields = ft.Container(
        content= ft.Column(
            controls=(
                Distancia,Aceleracion,Tiempo,V_inicial,V_final
            )
        )
    )
    
    Distancia_segundos = []
    velocidad_segundos = []
    Aceleracion_segundos = []

    # Create a Plotly figure with two empty traces
    fig = go.Figure(data=[
        go.Scatter(x=[], y=[], name='Distancia-Tiempo'),
        go.Scatter(x=[], y=[], name='aceleracion-Tiempo'),
        go.Scatter(x=[], y=[], name='Velocidad-Tiempo'),
    ])
    
    container_graphic = ft.Container(PlotlyChart(fig), padding=100)

    
    def Calcular(e):
        i = 0
        try:
            distancia = float(Distancia.value)
        except ValueError:
            i+=1
            Distancia.value = ''
        try:
            aceleración = float(Aceleracion.value)
        except ValueError:
            i+=1
            Aceleracion.value = ''
        try:
            tiempo = float(Tiempo.value)
        except ValueError:
            i+=1
            Tiempo.value = ''
        try:
            velocidad_i = float(V_inicial.value)
        except ValueError:
            i+=1
            V_inicial.value = ''
        try:
            velocidad_f = float(V_final.value)
        except ValueError:
            i+=1
            V_final.value = ''
        n_r = 0
        while (Distancia.value == "" or Aceleracion.value == "" or Tiempo.value == "" or V_inicial.value == "" or V_final.value == "") or n_r <= 3:
            # para la velocidad Inicial
            if V_inicial.value == "":
                if Distancia.value != "" and Tiempo.value != "" and Aceleracion.value != "":
                    V_inicial.value = f"{(distancia /tiempo) - (tiempo * aceleración /2.0)}"
                if V_inicial.value == "" and (V_final.value != "" and Aceleracion.value != "" and Tiempo.value != ""):
                    V_inicial.value = f"{velocidad_f - aceleración * tiempo}"
                if V_inicial.value == "" and ( V_final.value != "" and Aceleracion.value != "" and Distancia.value != ""):
                    V_inicial.value = f"{m.sqrt((velocidad_f**2 - 2.0 * aceleración * distancia))}"
                if V_inicial.value == "" and (V_final.value != "" and Distancia.value != "" and Tiempo.value != ""):
                    V_inicial.value = f"{2 * (distancia / tiempo) - velocidad_f}"
                try:
                    velocidad_i = float(V_inicial.value)
                except:
                    print('no se calcula la velocidad inicial')
            #para distancia
            if Distancia.value == "":
                if Distancia.value == "" and (V_inicial.value != "" and V_final.value != "" and Aceleracion.value != ""):
                    Distancia.value = f"{(velocidad_f**2.0 - velocidad_i**2.0) / (2.0 * aceleración)}"
                if Distancia.value == "" and (V_inicial.value != "" and Tiempo.value != "" and Aceleracion.value != ""):
                    Distancia.value =  f"{velocidad_i * tiempo + (aceleración * tiempo**2.0) / 2.0}"
                if Distancia.value == "" and (V_final.value != "" and Tiempo.value != "" and Aceleracion.value != ""):
                    Distancia.value = f"{velocidad_f * tiempo - 0.5 * 2.0 * tiempo ** 2.0}"
                if Distancia.value == "" and (V_inicial.value != "" and V_final.value != "" and Tiempo.value != ""):
                    Distancia.value = f"{((velocidad_i + velocidad_f) / 2.0) * tiempo}"
                try:
                    distancia = float(Distancia.value)
                except:
                    print('no se calcula la distancia')
            #para tiempo
            if Tiempo.value == "":
                if Tiempo.value == "" and (V_final.value != "" and V_inicial.value != "" and Aceleracion.value != ""):
                    Tiempo.value = f"{(velocidad_f - velocidad_i) / aceleración}"
                if Tiempo.value == "" and (Distancia.value != "" and V_inicial.value != "" and V_final.value != ""):
                    Tiempo.value = f"{distancia / ((velocidad_i + velocidad_f) / 2.0)}"
                try:
                    tiempo = float(Tiempo.value)
                except:
                    print('no se calcula el tiempo')
            # para Aceleración
            if Aceleracion.value == "":
                if Aceleracion.value == "" and (V_inicial.value != "" and V_final.value != "" and Tiempo.value != ""):
                    Aceleracion.value = f"{(velocidad_f - velocidad_i) / tiempo}"
                if Aceleracion.value == "" and (V_inicial.value != "" and Distancia.value != "" and Tiempo.value != ""):
                    Aceleracion.value = f"{(distancia - (velocidad_i * tiempo)) / (0.5 * tiempo**2.0)}"
                if Aceleracion.value == "" and (V_inicial.value != "" and V_final.value != "" and Distancia.value != ""):
                    Aceleracion.value = f"{(velocidad_f**2.0 - velocidad_i**2.0) / (2.0 * distancia)}"
                if Aceleracion.value == "" and (Distancia.value != "" and V_final.value != "" and Tiempo.value != ""):
                    Aceleracion.value = f"{2*(velocidad_f * tiempo - distancia) / tiempo**2}"
                try:
                    aceleración = float(Aceleracion.value)
                except:
                     print('no se calcula la aceleración')
            # para velocidad final
            if V_final.value == "":
                if V_final.value == "" and (V_inicial.value != "" and Aceleracion.value != "" and Distancia.value != ""):
                    V_final.value = f"{m.sqrt(velocidad_i**2 + 2.0 * aceleración * distancia)}"
                if V_final.value == "" and (V_inicial.value != "" and Aceleracion.value != "" and Tiempo.value != ""):
                    V_final.value = f"{velocidad_i + aceleración * tiempo}"  
                try:
                    velocidad_f = float(V_final.value)
                except:
                     print('no se calcula la velocidad final')
            n_r += 1
            
        Distancia_segundos.extend(velocidad_i * i + 1/2 * aceleración * i**2 for i in range(1, 11))
        velocidad_segundos.extend(velocidad_i + aceleración * i for i in range(1, 11))
        Aceleracion_segundos.extend(aceleración for i in range(1, 11))
            
        fig.data[0].x = list(range(1, 11))
        fig.data[1].x = list(range(1, 11))
        fig.data[2].x = list(range(1, 11))
        fig.data[0].y = Distancia_segundos
        fig.data[1].y = Aceleracion_segundos
        fig.data[2].y = velocidad_segundos
            
        page.update()
        Distancia_segundos.clear()
        Aceleracion_segundos.clear()
        velocidad_segundos.clear()
            
    def Limpiar(e):
        Distancia.value = ""
        Tiempo.value = ""
        Aceleracion.value = ""
        V_inicial.value = ""
        V_final.value = ""
        page.update()

    page.add(
        controls.header_page(Volver_main=Volver_main, e=ft.Container),
        textfields,
        controls.Buttons(ft.Container, Calcular=Calcular, Limpiar=Limpiar),
        container_graphic,
    )
