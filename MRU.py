import flet as ft
import plotly.io as pio
import plotly.graph_objects as go
from flet.plotly_chart import PlotlyChart
from App_important_controls import controls

def main_MRU(page) -> ft.Page:
    pio.renderers.default = 'svg'
    page.scroll = ft.ScrollMode.ALWAYS
    page.title = 'Movimiento Rectilíneo Uniforme'

    # Create text fields for the input values
    distancia = ft.TextField(
        label='DISTANCIA', suffix_text='m', on_change=controls.cambio_Textfield)
    velocidad = ft.TextField(
        label='VELOCIDAD', suffix_text='m/s', on_change=controls.cambio_Textfield)
    tiempo = ft.TextField(
        label='TIEMPO', suffix_text='s', on_change=controls.cambio_Textfield)

    # Create the TextFields Column component
    TextFields = ft.Column([distancia, velocidad, tiempo],expand=True, spacing=40)

    # Create lists to store the data for the graph
    Distancia_segundos = []
    velocidad_segundos = []

    # Create a Plotly figure with two empty traces
    fig = go.Figure(data=[
        go.Scatter(x=[], y=[], name='Distancia-Tiempo'),
        go.Scatter(x=[], y=[], name='Velocidad-Tiempo')
    ])

    # Create a PlotlyChart component with the fig
    container_graphic = ft.Container(PlotlyChart(fig), padding=100)

    # Define the Volver_main function
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))

    # Define the Limpiar function
    def Limpiar(e):
        distancia.value = ''
        velocidad.value = ''
        tiempo.value = ''
        page.update()

    # Define the Calcular function
    def Calcular(e):
        i = 0
        try:
            D = float(distancia.value)
        except ValueError:
            i += 1
        try:
            T = float(tiempo.value)
        except ValueError:
            i += 1
        try:
            V = float(velocidad.value)
        except ValueError:
            i += 1

        if i >= 2:
            return

        if distancia.value == '':
            D = T * V
            distancia.value = f'{D}'
        elif velocidad.value == '':
            V = D / T
            velocidad.value = f'{V}'
        else:
            T = D / V
            tiempo.value = f'{T}'

        # Fill the lists with the calculated data
        Distancia_segundos.extend(i * V for i in range(1, 11))
        velocidad_segundos.extend(((i * V) / i) for i in range(1, 11))

        # Update the Plotly figure with the calculated data
        fig.data[0].x = list(range(1, 11))
        fig.data[0].y = Distancia_segundos
        fig.data[1].x = list(range(1, 11))
        fig.data[1].y = velocidad_segundos
        page.update()

        # Clear the lists
        Distancia_segundos.clear()
        velocidad_segundos.clear()

    # Add the page controls
    page.add(
        controls.header_page(Volver_main=Volver_main, e=ft.Container),
        ft.Container(TextFields, padding=80),
        controls.Buttons(ft.Container, Calcular=Calcular, Limpiar=Limpiar),
        container_graphic,
    )
