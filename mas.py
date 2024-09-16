import flet as ft
import math as m
import numpy as np
import plotly.graph_objects as go
from flet.plotly_chart import PlotlyChart
from plotly.subplots import make_subplots
from App_important_controls import controls

def main_mas(page: ft.Page) -> ft.View:
    page.title = 'Movimiento Armonico Simple'

    def calculate_period(length, gravity):
        return 2 * m.pi * m.sqrt(length / gravity)

    def calculate_length(period, gravity):
        return (gravity / (4 * m.pi**2)) * period**2

    def calculate_gravity(length, period):
        return (4 * m.pi**2 * length) / period**2

    def calculate_frequency(period):
        return 1 / period

    def calculate_angular_frequency(length, gravity):
        return m.sqrt(gravity / length)

    def plot_sinusoidal_graphs(amplitude, frequency):
     fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

     x = np.linspace(0, 10, 1000)
     W = 2 * m.pi * frequency
     y = amplitude * np.cos(W * x)
     fig.append_trace(go.Scatter(x=x, y=y, name='Posición'), row=1, col=1)

     v = np.linspace(0, 10, 1000)
     w = 2 * m.pi * frequency
     y = -amplitude * w * np.sin(w * v)
     fig.append_trace(go.Scatter(x=v, y=y, name='Velocidad'), row=2, col=1)

     a = np.linspace(0, 10, 1000)
     w = 2 * m.pi * frequency
     y = -amplitude * w**2 * np.cos(w * a)
     fig.append_trace(go.Scatter(x=a, y=y, name='Aceleración'), row=3, col=1)

     fig.update_layout(height=600, width=800, title_text="Gráficas de movimiento armónico simple")
     return fig

    def calcular_pp(e):
        try:
            if p_pendulo.value and l_pendulo.value:
                period = float(p_pendulo.value)
                length = float(l_pendulo.value)
                gravity = calculate_gravity(length, period)
                frequency = calculate_frequency(period)
                angular_frequency = calculate_angular_frequency(length, gravity)
                p_pendulo.value = f"{period:.2f}"
                l_pendulo.value = f"{length:.2f}"
                g_pendulo.value = f"{gravity:.2f}"
                f_pendulo.value = f"{frequency:.2f}"
                fa_pendulo.value = f"{angular_frequency:.2f}"
            elif p_pendulo.value and g_pendulo.value:
                period = float(p_pendulo.value)
                gravity = float(g_pendulo.value)
                length = calculate_length(period, gravity)
                frequency = calculate_frequency(period)
                angular_frequency = calculate_angular_frequency(length, gravity)
                p_pendulo.value = f"{period:.2f}"
                l_pendulo.value = f"{length:.2f}"
                g_pendulo.value = f"{gravity:.2f}"
                f_pendulo.value = f"{frequency:.2f}"
                fa_pendulo.value = f"{angular_frequency:.2f}"
            elif l_pendulo.value and g_pendulo.value:
                length = float(l_pendulo.value)
                gravity = float(g_pendulo.value)
                period = calculate_period(length, gravity)
                frequency = calculate_frequency(period)
                angular_frequency = calculate_angular_frequency(length, gravity)
                p_pendulo.value = f"{period:.2f}"
                l_pendulo.value = f"{length:.2f}"
                g_pendulo.value = f"{gravity:.2f}"
                f_pendulo.value = f"{frequency:.2f}"
                fa_pendulo.value = f"{angular_frequency:.2f}"
            else:
                print("Invalid values")
                return
        except ValueError as e:
            print("invalid values failed")
            return
        
        page.update()


    def calcular_pr(e):
        try:
            amplitude = float(a_resorte.value)
            if p_resorte.value and l_resorte.value:
                period = float(p_resorte.value)
                length = float(l_resorte.value)
                gravity = calculate_gravity(length, period)
                frequency = calculate_frequency(period)
                angular_frequency = calculate_angular_frequency(length, gravity)
                p_resorte.value = f"{period:.2f}"
                l_resorte.value = f"{length:.2f}"
                g_resorte.value = f"{gravity:.2f}"
                f_resorte.value = f"{frequency:.2f}"
                fa_resorte.value = f"{angular_frequency:.2f}"
                a_resorte.value = f"{amplitude:.2f}"
            elif p_resorte.value and g_resorte.value:
                period = float(p_resorte.value)
                gravity = float(g_resorte.value)
                length = calculate_length(period, gravity)
                frequency = calculate_frequency(period)
                angular_frequency = calculate_angular_frequency(length, gravity)
                p_resorte.value = f"{period:.2f}"
                l_resorte.value = f"{length:.2f}"
                g_resorte.value = f"{gravity:.2f}"
                f_resorte.value = f"{frequency:.2f}"
                fa_resorte.value = f"{angular_frequency:.2f}"
                a_resorte.value = f"{amplitude:.2f}"
            elif l_resorte.value and g_resorte.value:
                length = float(l_resorte.value)
                gravity = float(g_resorte.value)
                period = calculate_period(length, gravity)
                frequency = calculate_frequency(period)
                angular_frequency = calculate_angular_frequency(length, gravity)
                p_resorte.value = f"{period:.2f}"
                l_resorte.value = f"{length:.2f}"
                g_resorte.value = f"{gravity:.2f}"
                f_resorte.value = f"{frequency:.2f}"
                a_resorte.value = f"{amplitude:.2f}"
                fa_resorte.value = f"{angular_frequency:.2f}"
            else:
                print("Invalid values")
                return
        except ValueError as e:
            print("invalid values failed")
            return

        fig1 = plot_sinusoidal_graphs(amplitude, frequency)
        chart1 = PlotlyChart(fig1)
        content_resorte.content.controls.append(chart1)  
        page.update()

    def limpiar_pp(e):
        p_pendulo.value = ''
        l_pendulo.value = ''
        g_pendulo.value = ''
        f_pendulo.value = ''
        a_pendulo.value = ''
        fa_pendulo.value = ''
        content_pendulo.content.controls.pop()
        page.update()

    def limpiar_pr(e):
        p_resorte.value = ''
        l_resorte.value = ''
        g_resorte.value = ''
        f_resorte.value = ''
        a_resorte.value = ''
        fa_resorte.value = ''
        content_resorte.content.controls.pop()
        page.update()

    p_pendulo = ft.TextField(label="Periodo:", )
    l_pendulo = ft.TextField(label='Longitud:',)
    g_pendulo = ft.TextField(label='Gravedad:',)
    f_pendulo = ft.TextField(label='Frecuencia:',)
    fa_pendulo = ft.TextField(label='Frecuencia angular:',)
    a_pendulo = ft.TextField(label='Amplitud:',)


    p_resorte = ft.TextField(label="Periodo:", )
    l_resorte = ft.TextField(label='masa:',)
    g_resorte = ft.TextField(label='constante elastica:',)
    f_resorte = ft.TextField(label='Frecuencia:',)
    fa_resorte = ft.TextField(label='Frecuencia angular:',)
    a_resorte = ft.TextField(label='Amplitud:',)

    content_pendulo = ft.Container(
        content=ft.Column(
            controls=[
                p_pendulo,
                l_pendulo,
                g_pendulo,
                f_pendulo,
                a_pendulo,
                fa_pendulo,
                controls.Buttons(Calcular=calcular_pp, Limpiar=limpiar_pp, e=ft.Container),
            ]
        ),
        margin=20,
        padding=30
    )

    content_resorte = ft.Container(
        content=ft.Column(
            controls=[
                p_resorte,
                l_resorte,
                g_resorte,
                f_resorte,
                a_resorte,
                fa_resorte,
                controls.Buttons(Calcular=calcular_pr, Limpiar=limpiar_pr, e=ft.Container),
            ]
        ),
        margin=20,
        padding=30
    )

    tabs_mas = ft.Tabs(
        selected_index=0,
        animation_duration=400,
        width=1000,
        height=1300,
        tabs=[
            ft.Tab(
                text='Sistema de péndulo simple',
                content=content_pendulo
            ),
            ft.Tab(
                text='Sistema masa-resorte',
                content=content_resorte  
            ),
        ]
    )

    return ft.View(
        "/MAS",
        [
            ft.Column(
                controls=[
                    controls.header_page(page),
                    ft.Container(
                        content=tabs_mas, 
                        margin= ft.margin.only(top= 10, left= 0, right=0)
                    ),
                ]
            )
        ],scroll=True
        
    )