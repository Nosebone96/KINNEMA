import flet as ft
from models.Models import controls

def main_doppler( page: ft.Page ) -> ft.View:


    def formula_doppler(e, FE, VO, VF, VS):
        try:
            print(f'{FE},{VO}, {VF}, {VS}')
            resultado = FE * ( (VS + VO )  / ( VS - VF ) )
            return  resultado 
            

        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: Verifica que los datos digitados sean correctos"))
            page.snack_bar.open = True
            print(f'{ex}')
            page.update()


    def calcular(e):
        i = 0
        try:
            fe = float(frecuencia_emisor.value)
        except Exception:
            fe = 0
            i += 1
        try:
            vo = float(velocidad_observador.value)
        except Exception:
            vo = 0
            i +=1
        try:
            vf = float(velocidad_fuente.value)
        except Exception:
            vf = 0
            i +=1
        try:
            vs = float(velocidad_sonido.value)
        except:
            vs = 0
            i +=1

        if dd_fuente.value == 'se aleja':
            print('ddfuente se aleja')
            vf *= -1
        if dd_observador.value == 'se aleja':
            print('ddobservador se aleja')
            vo *= -1
        print(f'{fe},{vo}, {vf}, {vs}')
        doppler = formula_doppler(e=e,FE=fe, VO=vo, VF=vf, VS=vs)
        efecto_doppler.value = f'{doppler}'
        page.update()
            
        

    def limpiar(e):
        frecuencia_emisor.value = ''
        velocidad_sonido.value = ''
        velocidad_observador.value = ''
        velocidad_fuente.value = ''
        efecto_doppler.value = ''
        dd_fuente.value = None
        dd_observador.value = None
        page.update()
    
    

    frecuencia_emisor = ft.TextField(label='frecuencia del emisor')
    velocidad_sonido = ft.TextField(label='velocidad del sonido')
    velocidad_observador = ft.TextField(label='velocidad del observador')
    velocidad_fuente = ft.TextField(label='velocidad de la fuente')
    efecto_doppler = ft.TextField(label='efecto Doppler', disabled=True, border_color=ft.colors.BLUE_400)
    dd_fuente = ft.Dropdown(
        options=[
            ft.dropdown.Option('se aleja'),
            ft.dropdown.Option('se acerca')
        ]
    )
    dd_observador = ft.Dropdown(
        options=[
            ft.dropdown.Option('se aleja'),
            ft.dropdown.Option('se acerca')
        ]
    )

    column = ft.Column(
        controls=[
            controls.header_page(page),
            ft.Row([frecuencia_emisor], alignment='CENTER'),
            ft.Row([velocidad_sonido], alignment='CENTER'),
            ft.Row([velocidad_fuente, dd_fuente], alignment='CENTER'),
            ft.Row([velocidad_observador, dd_observador], alignment='CENTER'),
            ft.Row([efecto_doppler], alignment='CENTER'),
            controls.Buttons(Calcular=calcular, Limpiar=limpiar, e=ft.Container),
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
        'Efecto_doppler',
        [
            stack,
        ], padding=0,
    )