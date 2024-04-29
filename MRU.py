import flet as ft
import plotly.graph_objects as go
from flet.plotly_chart import PlotlyChart
from App_important_controls import controls

def main_MRU(page) -> ft.Page:
    page.scroll = ft.ScrollMode.ALWAYS
    page.title = 'Movimiento Rectilíneo Uniforme'
    distancia = ft.TextField(label='DISTANCIA', suffix_text='m', on_change=controls.cambio_Textfield)
    velocidad = ft.TextField(label='VELOCIDAD', suffix_text='m/s', on_change=controls.cambio_Textfield)
    tiempo = ft.TextField(label='TIEMPO', suffix_text='s',on_change=controls.cambio_Textfield)
    TextFields = ft.Column([distancia, velocidad, tiempo,], expand= True, spacing=40)
    Distancia_segundos = []
    velocidad_segundos = []
    fig = go.Figure(data=[
        go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[], name='Distancia-Tiempo'),
        go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[],name='Velocidad-Tiempo')
    ])
    container_graphic = ft.Container(PlotlyChart(fig))
    
    def Volver_main(e):
        page.controls.clear()
        import Menu_principal
        page.go(Menu_principal.main(page))
    
    def Limpiar(e):
        distancia.value = ''
        velocidad.value = ''
        tiempo.value = ''
        page.update()

    def Calcular(e):
        i = 0
        D = V = T = 0
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
        if i > 1:
            return
        else:
            if distancia.value == '':
                distancia.value = f'{T * V}'
            elif velocidad.value == '':
                V = D / T
                velocidad.value = f'{V}'
            else:
                tiempo.value = f'{D / V}'
            graficas(v=V,e=go.Figure)
        page.update()
        
    def graficas(e, v)-> go.Figure:
        for i in range(1, 10):
            resultado_distancia = i * v
            resultado_velocidad = resultado_distancia / i
            Distancia_segundos.append((resultado_distancia))
            velocidad_segundos.append(resultado_velocidad) 

        fig.data[0].y = Distancia_segundos
        fig.data[1].y = velocidad_segundos

        page.update()
        Distancia_segundos.clear()
        velocidad_segundos.clear()
          
    page.add(
        controls.header_page(Volver_main=Volver_main, e=ft.Container),
        ft.Container(TextFields, padding=80),
        controls.Buttons(ft.Container, Calcular=Calcular, Limpiar=Limpiar),
        container_graphic,
        
    )
