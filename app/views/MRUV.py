import flet as ft
import plotly.io as pio
import plotly.graph_objects as go
from flet.plotly_chart import PlotlyChart
import time
from models.Models import controls
import math as m
import threading

def main_MRUV(page: ft.Page):
    pio.renderers.default = 'svg'
    page.scroll = ft.ScrollMode.ALWAYS
    page.title = 'Movimiento Rectilíneo Uniformemente Variado'

    Distancia_segundos = []
    velocidad_segundos = []
    Aceleracion_segundos = []

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
                if V_final.value == "" and (V_inicial.value != "" and Aceleracion.value != "" and Tiempo.value != ""):
                    V_final.value = f"{velocidad_i + aceleración * tiempo}"
                if V_final.value == "" and (V_inicial.value != "" and Aceleracion.value != "" and Distancia.value != ""):
                    V_final.value = f"{m.sqrt(velocidad_i**2 + 2.0 * aceleración * distancia)}"  
                try:
                    velocidad_f = float(V_final.value)
                except:
                     print('no se calcula la velocidad final')
            n_r += 1
        
        Distancia_segundos.append(0)
        velocidad_segundos.append(velocidad_i)
        Distancia_segundos.extend(velocidad_i * i + 1/2 * aceleración * i**2 for i in range(1, 11))
        velocidad_segundos.extend(velocidad_i + aceleración * i for i in range(1, 11))
        Aceleracion_segundos.extend(aceleración for i in range(0, 11))
            
        fig.data[0].x = list(range(0, 11))
        fig.data[1].x = list(range(0, 11))
        fig.data[2].x = list(range(0, 11))
        fig.data[0].y = Distancia_segundos
        fig.data[1].y = Aceleracion_segundos
        fig.data[2].y = velocidad_segundos
        Txfaceleracion.value = Aceleracion.value
        Txfvelocidad.value = V_inicial.value
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
        
    def llenar_tabla(e):
        velocidad.append(Txfvelocidad.value)
        distancia.extend("0")
        distancia.extend(float(Txfvelocidad.value) * i + 1/2 * float(Txfaceleracion.value) * i**2 for i in range(1, 11))
        velocidad.extend(float(Txfvelocidad.value) + float(Txfaceleracion.value) * i for i in range(1, 11))
        print(distancia)
        print(velocidad)
        for i in range(1,12):
            data_table.rows[0].cells[i].content.value = velocidad[((i - 1))]
            data_table.rows[1].cells[i].content.value = distancia[(i - 1)]
            data_table.rows[2].cells[i].content.value = Txfaceleracion.value
            data_table.update()
            time.sleep(1.1)
        distancia.clear()
        velocidad.clear()
        aceleracion.clear()
            
    def animate_container(e):
        c1.left=0
        speed = 0.01
        movimiento = float(Txfvelocidad.value)
        velocidad_i = float(Txfvelocidad.value)
        aceleracion = float(Txfaceleracion.value)
        for i in range(1000):
            movimiento = velocidad_i + aceleracion * (i / 100)
            c1.left += movimiento
            c1.update()
            time.sleep(speed)
        c1.update()
        
    def ejecutar_ambas(e):
        hilo1 = threading.Thread(target=llenar_tabla, args=(e,))
        hilo2 = threading.Thread(target=animate_container, args=(e,))
        hilo1.start()
        hilo2.start()
    
    
    Distancia = ft.TextField(label='Distancia', suffix_text='m', on_change=controls.cambio_Textfield)
    Aceleracion = ft.TextField(label='Aceleracion', suffix_text='m/s²', on_change=controls.cambio_Textfield)
    Tiempo = ft.TextField(label='Tiempo', suffix_text='s', on_change=controls.cambio_Textfield)
    V_inicial = ft.TextField(label='Velocidad Inicial', suffix_text='m/s', on_change=controls.cambio_Textfield)
    V_final = ft.TextField(label='Velocidad Final', suffix_text='m/s', on_change=controls.cambio_Textfield)
    
    calculadora = ft.Container(
        content= ft.Column(
            controls=(
                Distancia,Aceleracion,Tiempo,V_inicial,V_final, controls.Buttons(ft.Container, Calcular=Calcular, Limpiar=Limpiar),
            )
        ),margin=ft.margin.only(bottom=30, top=30)
    )
    
    fig = go.Figure(data=[
        go.Scatter(x=[], y=[], name='Distancia-Tiempo'),
        go.Scatter(x=[], y=[], name='aceleracion-Tiempo'),
        go.Scatter(x=[], y=[], name='Velocidad-Tiempo'),
    ])
    
    container_graphic = ft.Container(PlotlyChart(fig, expand=True))
    
    
    Txfvelocidad = ft.TextField(label='Velocidad inicial')
    Txfaceleracion = ft.TextField(label='Aceleración')
    velocidad = []
    distancia = [] 
    aceleracion = []
    
    data_table = ft.DataTable(
        width=1100,
        border_radius=10,
        border=ft.border.all(1, "#9ecaff"),
        vertical_lines=ft.border.BorderSide(1, "#9ecaff"),
        columns=[
            ft.DataColumn(ft.Text("Tiempo (s)"), numeric=True),
            ft.DataColumn(ft.Text("0"), numeric=True),
            ft.DataColumn(ft.Text("1"), numeric=True),
            ft.DataColumn(ft.Text("2"), numeric=True),
            ft.DataColumn(ft.Text("3"), numeric=True),
            ft.DataColumn(ft.Text("4"), numeric=True),
            ft.DataColumn(ft.Text("5"), numeric=True),
            ft.DataColumn(ft.Text("6"), numeric=True),
            ft.DataColumn(ft.Text("7"), numeric=True),
            ft.DataColumn(ft.Text("8"), numeric=True),
            ft.DataColumn(ft.Text("9"), numeric=True),
            ft.DataColumn(ft.Text("10"), numeric=True),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Velocidad (m/s)")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Distancia (m)")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Aceleración (m/s^2)")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                    ft.DataCell(ft.Text("")),
                ],
            ),
        ],
    )
    
    c1 = ft.Container(
        content=ft.Image(src="assets\moto.png"),
        width=200,
        height=200,
        top=0,
        left=0,
        animate=ft.Animation(duration=1000, curve=ft.AnimationCurve.LINEAR),
    )
    
    stak_animation = ft.Stack([c1], height=400, width=1200)
    animar = ft.ElevatedButton("¡¡ANIMAR!!", on_click=ejecutar_ambas)
    
    container_data = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(controls=[Txfaceleracion, Txfvelocidad], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                data_table,
            ],  
        ),margin=ft.margin.only(top=20, bottom=40, left=10, right=10), padding=ft.padding.only(top=20, bottom=20, left=40, right=20),
    )
    
    clm_animacion = ft.Column(
        controls=[
            container_data,
            stak_animation,
            animar,
        ],
    )
    
    tabs = ft.Tabs(
        tab_alignment= ft.MainAxisAlignment.CENTER,
        height=900,
        tabs=[
            ft.Tab(
                text="calculadora",
                content=calculadora,
            ),
            ft.Tab(
                text="Grafica",
                content=container_graphic,
            ),
            ft.Tab(
                text='animación',
                content=clm_animacion,
            )
        ]
    )
    
    
    column = ft.Column(
        controls=[
            controls.header_page(page),
            tabs,
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
        "/MRUV",
        [
            stack,
        ],padding=0
    )