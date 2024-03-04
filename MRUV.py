import flet as ft
import importlib
import math as m

def main_MRUV(page: ft.Page):
    def Volver_main(e):
        page.controls.clear()
        page.go(importlib.import_module('Menu_principal').main(page))
    Distancia = ft.TextField(label='Distancia', suffix_text='m')
    Aceleracion = ft.TextField(label='Aceleracion', suffix_text='m/s²')
    Tiempo = ft.TextField(label='Tiempo', suffix_text='s')
    V_inicial = ft.TextField(label='Velocidad Inicial', suffix_text='m/s')
    V_final = ft.TextField(label='Velocidad Final', suffix_text='m/s')
    textfields = ft.Container(
        content= ft.Column(
            controls=(
                Distancia,Aceleracion,Tiempo,V_inicial,V_final
            )
        )
    )
    def Calcular(e):
        i = 0
        try:
            distancia = float(Distancia.value)
        except ValueError:
            i+=1
        try:
            aceleración = float(Aceleracion.value)
        except ValueError:
            i+=1
        try:
            tiempo = float(Tiempo.value)
        except ValueError:
            i+=1
        try:
            velocidad_i = float(V_inicial.value)
        except ValueError:
            i+=1
        try:
            velocidad_f = float(V_final.value)
        except ValueError:
            i+=1
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
        page.update()
            
    def Limpiar(e):
        Distancia.value = ""
        Tiempo.value = ""
        Aceleracion.value = ""
        V_inicial.value = ""
        V_final.value = ""
        page.update()

    page.add(
        importlib.import_module('App_important_controls').header_page(ft.Container, Volver_main),
        textfields,
        importlib.import_module('App_important_controls').Buttons(ft.Container, Calcular, Limpiar),
    )