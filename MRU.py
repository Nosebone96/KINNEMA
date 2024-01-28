import flet as ft

def main(page):
    distancia = ft.TextField(label='DISTANCIA')
    velocidad = ft.TextField(label='VELOCIDAD')
    tiempo = ft.TextField(label='TIEMPO')
    
    def limpiar(e):
        distancia.value = ''
        velocidad.value = ''
        tiempo.value = ''
        page.update()

    def verificar_formato(e):
        i = 0
        D = V = T = 0
        if not isinstance(distancia.value.isdigit(), str) and distancia.value != '': 
            D = float(distancia.value)
        else:
            i += 1
        if not isinstance(velocidad.value.isdigit(), str) and velocidad.value != '': 
             V = float(velocidad.value)
        else:
            i += 1
        if not isinstance(tiempo.value.isdigit(), str) and tiempo.value != '': 
            T = float(tiempo.value)
        else:
            i += 1
        if i > 1:
            return
        else:
            if distancia.value == '':
                distancia.value = f'{T * V}'
            elif velocidad.value == '':
                velocidad.value = f'{D / T}'
            else:
                tiempo.value = f'{D / V}'
        page.update()        
    page.add(
        distancia,
        velocidad,
        tiempo,
        ft.ElevatedButton('Calcular', on_click=verificar_formato),
        ft.ElevatedButton('limpiar', on_click=limpiar)
    )

ft.app(target=main)