import flet as ft
import math as m
import numpy as np
import plotly.express as px
from flet.plotly_chart import PlotlyChart
from App_important_controls import controls
def main_mas(page: ft.Page) -> ft.Page:
    page.scroll = ft.ScrollMode.ALWAYS
    page.title = 'Movimiento Armonico Simple'
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))
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

    def plot_sinusoidal_graph(amplitude, frequency):
        x = np.linspace(0, 10, 1000)
        W = 2 * m.pi * frequency
        y = amplitude * np.cos(W * x)
        fig = px.line(x=x, y=y)

        # Find peak and trough indices
        peak_idx = np.where(np.diff(np.sign(np.diff(y))) < 0)[0] + 1
        trough_idx = np.where(np.diff(np.sign(np.diff(y + 1e-10))) > 0)[0] + 1

        # Add annotations for the first 3 peaks, the highest peak, and the lowest trough
        for i in range(1):
            if i < len(peak_idx):
                fig.add_annotation(text=f"x={x[peak_idx[i]]:.2f}, y={y[peak_idx[i]]:.2f}", x=x[peak_idx[i]], y=y[peak_idx[i]], showarrow=True, arrowhead=1)
                fig.add_annotation(text=f"x={x[trough_idx[i]]:.2f}, y={y[trough_idx[i]]:.2f}", x=x[trough_idx[i]], y=y[trough_idx[i]], showarrow=True, arrowhead=1)
        return fig        

    def plot_sinusoidal_velocity_graph(frequency, amplitude):
        v = np.linspace(0, 10, 1000)
        w = 2 * m.pi * frequency
        y = -amplitude * w * np.sin(w * v)
        fig = px.line(x=v, y=y)

        # Find peak and trough indices
        peak_idx = np.where(np.diff(np.sign(np.diff(y))) < 0)[0] + 1
        trough_idx = np.where(np.diff(np.sign(np.diff(y + 1e-10))) > 0)[0] + 1

        # Add annotations for the first 1 peaks, the highest peak, and the lowest trough
        for i in range(1):
            if i < len(peak_idx):
                fig.add_annotation(text=f"x={v[peak_idx[i]]:.2f}, y={y[peak_idx[i]]:.2f}", x=v[peak_idx[i]], y=y[peak_idx[i]], showarrow=True, arrowhead=1)
                fig.add_annotation(text=f"x={v[trough_idx[i]]:.2f}, y={y[trough_idx[i]]:.2f}", x=v[trough_idx[i]], y=y[trough_idx[i]], showarrow=True, arrowhead=1)
        return fig

    def plot_sinusoidal_aceleration(frequency, amplitude):
        a = np.linspace(0, 10, 1000)
        w = 2 * m.pi * frequency
        y = -amplitude * w**2 * np.cos(w * a)
        fig = px.line(x=a, y=y)

        # Find peak and trough indices
        peak_idx = np.where(np.diff(np.sign(np.diff(y))) < 0)[0] + 1
        trough_idx = np.where(np.diff(np.sign(np.diff(y + 1e-10))) > 0)[0] + 1

        # Add annotations for the first 1 peaks, the highest peak, and the lowest trough
        for i in range(1):
            if i < len(peak_idx):
                fig.add_annotation(text=f"x={a[peak_idx[i]]:.2f}, y={y[peak_idx[i]]:.2f}", x=a[peak_idx[i]], y=y[peak_idx[i]], showarrow=True, arrowhead=1)
                fig.add_annotation(text=f"x={a[trough_idx[i]]:.2f}, y={y[trough_idx[i]]:.2f}", x=a[trough_idx[i]], y=y[trough_idx[i]], showarrow=True, arrowhead=1)
        return fig

    def calcular_pp(e):
        try:
            amplitude = float(a_pendulo.value)
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
                a_pendulo.value = f"{amplitude:.2f}"
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
                a_pendulo.value = f"{amplitude:.2f}"
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
                a_pendulo.value = f"{amplitude:.2f}"
                fa_pendulo.value = f"{angular_frequency:.2f}"
            else:
                print("Invalid values")
                return
        except ValueError as e:
            print("invalid values failed")
            return

        fig1 = plot_sinusoidal_graph(amplitude, frequency)
        fig2 = plot_sinusoidal_velocity_graph(frequency, amplitude)
        fig3 = plot_sinusoidal_aceleration(frequency, amplitude)

        chart1 = PlotlyChart(fig1)
        chart2 = PlotlyChart(fig2)
        chart3 = PlotlyChart(fig3)

        graph_container = ft.Column(
            controls=[chart1, chart2, chart3]
        )

        content_pendulo.content.controls.append(graph_container)
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

        fig1 = plot_sinusoidal_graph(amplitude, frequency)
        fig2 = plot_sinusoidal_velocity_graph(frequency, amplitude)
        fig3 = plot_sinusoidal_aceleration(frequency, amplitude)

        chart1 = PlotlyChart(fig1)
        chart2 = PlotlyChart(fig2)
        chart3 = PlotlyChart(fig3)

        graph_container = ft.Column(
            controls=[chart1, chart2, chart3]
        )

        content_resorte.content.controls.append(graph_container)
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
                controls.Buttons(e=ft.Container, Calcular=calcular_pp, Limpiar=limpiar_pp)
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
                controls.Buttons(e=ft.Container, Calcular=calcular_pr, Limpiar=limpiar_pr)
            ]
        ),
        margin=20,
        padding=30
    )

    tabs_mas = ft.Tabs(
        selected_index=0,
        animation_duration=400,
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

    page.add(
        ft.Column(
            controls=[ft.Container(
                    content=tabs_mas, 
                    margin=ft.margin.only(top=10, left=0, right=0)
                ),
                ft.Column(
                  scroll=ft.ScrollMode.ALWAYS,
                  expand=True,
                )
            ]
        )
    )