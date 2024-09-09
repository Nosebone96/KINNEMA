import flet as ft
import math as Math
from App_important_controls import controls

def main_triangulo(page:ft.Page)-> ft.View:
    page.title = "Resolución de Triangulo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    class resolver_triangulo(ft.Control):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.angulos_faltantes = 0
            self.lados_faltantes = 0
            self.a = 0.0
            self.b = 0.0
            self.c = 0.0
            self.A = 0.0
            self.B = 0.0
            self.C = 0.0
            self.area = 0.0
            self.semiperimetro = 0.0
            self.ha = 0.0
            self.hb = 0.0
            self.hc = 0.0
            self.inradio = 0.0
            self.circunradio = 0.0
            self.mediana_a = 0.0
            self.mediana_b = 0.0
            self.mediana_c = 0.0
            self.perimetro = 0.0
                        
            try:
                self.a = float(lado_a.value)
            except ValueError:
                self.a = 0
                self.lados_faltantes += 1
            try:
                self.b = float(lado_b.value)
            except ValueError:
                self.b = 0
                self.lados_faltantes += 1
            try:
                self.c = float(lado_c.value)
            except ValueError:
                self.c = 0
                self.lados_faltantes += 1
            try:
                self.A = float(angulo_a.value)
            except ValueError:
                self.angulos_faltantes +=1
                self.A = 0
            try:
                self.B = float(angulo_b.value)
            except ValueError:
                self.B = 0
                self.angulos_faltantes +=1
            try:
                self.C = float(angulo_c.value)
            except ValueError:
                self.C = 0
                self.angulos_faltantes +=1
            print(f'ladosf:{self.lados_faltantes} angulosf:{self.angulos_faltantes}')
            i = 0
            print('_______________________________________')
            while (self.angulos_faltantes > 0 or self.lados_faltantes > 0) and i <= 2:
                print(f'vuelta {i} ladosf:{self.lados_faltantes} angulosf:{self.angulos_faltantes}')
                if self.a == 0 or self.b == 0 or self.c == 0:
                    if self.angulos_faltantes <= 2 and self.lados_faltantes <= 1:
                        self.ley_coseno_LAL()
                    if self.angulos_faltantes <= 2 and self.lados_faltantes <= 1:
                        self.ley_seno_ALL()
                    if self.angulos_faltantes <= 1 and self.lados_faltantes <= 2:
                        self.ley_seno_ALA()
                else:
                    self.ley_coseno_LLL()
                i += 1
            self.semiperimetro = self.semiperimetro_triangulo()
            semiperimetro.value = f'{round(self.semiperimetro, 2)}'
            self.area = self.area_triangulo()
            area.value = f'{round(self.area, 2)}'
            self.ha = self.hl_triangulo(self.a)
            altura_ha.value = f'{round(self.ha, 2)}'
            self.hb = self.hl_triangulo(self.b)
            altura_hb.value = f'{round(self.hb, 2)}'
            self.hc = self.hl_triangulo(self.c)
            altura_hc.value = f'{round(self.hc, 2)}'
            self.inradio = self.inradio_triangulo()
            inradio.value = f'{round(self.inradio, 2)}'
            self.circunradio = self.circunradio_triangulo()
            circunradio.value = f'{round(self.circunradio, 2)}'
            self.mediana_a = self.mediana(self.b, self.c, self.a)
            Mediana_ma.value = f'{round(self.mediana_a, 2)}'
            self.mediana_b = self.mediana(self.a, self.c, self.b)
            Mediana_mb.value = f'{round(self.mediana_b, 2)}'
            self.mediana_c = self.mediana(self.a, self.b, self.c)
            Mediana_mc.value = f'{round(self.mediana_c, 2)}'
            self.perimetro = self.semiperimetro * 2
            perimetro.value = f'{round(self.perimetro, 2)}'
            
            page.update()
        def ley_seno_ALL(self):
            #..................................................
            try:
                if self.A != 0 and self.a != 0:
                    if self.b != 0 and self.B == 0:
                        self.B = self.b * Math.sin(Math.radians(self.A)) / self.a
                        self.B = Math.degrees(Math.asin(self.B))
                        angulo_b.value = f'{round(self.B, 2)}'
                        self.angulos_faltantes -= 1
                        angulo_b.update()
                    elif self.c != 0 and self.C == 0:
                        self.C = self.c * Math.sin(Math.radians(self.A)) / self.a
                        self.C = Math.degrees(Math.asin(self.C))
                        angulo_c.value = f'{round(self.C, 2)}'
                        self.angulos_faltantes -= 1
                        angulo_c.update()
                elif self.B != 0 and self.b != 0:
                    if self.a != 0 and self.A == 0:
                        self.A = self.a * Math.sin(Math.radians(self.B)) / self.b
                        self.A = Math.degrees(Math.asin(self.A))
                        angulo_a.value = f'{round(self.A, 2)}'
                        self.angulos_faltantes -= 1
                        angulo_a.update()
                    elif self.c != 0 and self.C == 0:
                        self.C = self.c * Math.sin(Math.radians(self.B)) / self.b
                        self.C = Math.degrees(Math.asin(self.C))
                        angulo_c.value = f'{round(self.C, 2)}'
                        self.angulos_faltantes -= 1
                        angulo_c.update()
                elif self.C != 0 and self.c != 0:
                    if self.a != 0 and self.A == 0:
                        self.A = self.a * Math.sin(Math.radians(self.C)) / self.c
                        self.A = Math.degrees(Math.asin(self.A))
                        angulo_a.value = f'{round(self.A, 2)}'
                        self.angulos_faltantes -= 1
                        angulo_a.update()
                    elif self.b != 0 and self.B == 0:
                        self.B = self.b * Math.sin(Math.radians(self.C)) / self.c
                        self.B = Math.degrees(Math.asin(self.B))
                        angulo_b.value = f'{round(self.B, 2)}'
                        self.angulos_faltantes -= 1 
                        angulo_b.update()
            except Exception as error:
                print(error)
                page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
                page.snack_bar.open = True
            print('pasa por la ley del seno all')
        
        def ley_coseno_LLL(self):
            try:
                if self.A == 0:
                    self.A = Math.acos((Math.pow(self.b, 2) + Math.pow(self.c, 2) - Math.pow(self.a, 2)) / (2.0 * self.b * self.c))
                    self.A *= 180 / Math.pi
                    angulo_a.value = f'{round(self.A, 2)}'
                    self.angulos_faltantes -= 1
                    angulo_a.update()
                if self.B == 0:
                    self.B = Math.acos((Math.pow(self.a, 2) + Math.pow(self.c, 2) - Math.pow(self.b, 2)) / (2.0 * self.a * self.c))
                    self.B *= 180 / Math.pi
                    angulo_b.value = f'{round(self.B, 2)}'
                    self.angulos_faltantes -= 1
                    angulo_b.update()
                if self.C == 0:
                    self.C = Math.acos((Math.pow(self.a, 2) + Math.pow(self.b, 2) - Math.pow(self.c, 2)) / (2.0 * self.a * self.b))
                    self.C *= 180 / Math.pi
                    angulo_c.value = f'{round(self.C, 2)}'
                    self.angulos_faltantes -= 1
                    angulo_c.update()
            except Exception as error:
                print(error)
                page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
                page.snack_bar.open = True
            print('pasa por la ley del coseno lll')
    
        def ley_seno_ALA(self):
            try:
                # Calcular el tercer ángulo si dos ángulos son conocidos
                if self.A != 0 and self.B != 0 and self.C == 0:
                    self.C = 180 - (self.A + self.B)
                    angulo_c.value = f'{round(self.C, 2)}'
                    angulo_c.update()
                elif self.B != 0 and self.C != 0 and self.A == 0:
                    self.A = 180 - (self.B +self.C)
                    angulo_a.value = f'{round(self.A, 2)}'
                    angulo_a.update()
                elif self.C != 0 and self.A != 0 and self.B == 0:
                    self.B = 180 - (self.C + self.A)
                    angulo_b.value = f'{round(self.B, 2)}'
                    angulo_b.update()
                
                # Aplicar la Ley del Seno según los valores disponibles
                if self.a != 0 and self.A != 0:
                    if self.b == 0 and self.B != 0:
                        self.b = (self.a * Math.sin(Math.radians(self.B))) / Math.sin(Math.radians(self.A))
                        lado_b.value = f'{round(self.b, 2)}'
                        self.lados_faltantes -= 1
                        lado_b.update()
                    if self.c == 0 and self.C != 0:
                        self.c = (self.a * Math.sin(Math.radians(self.C))) / Math.sin(Math.radians(self.A))
                        lado_c.value = f'{round(self.c, 2)}'
                        self.lados_faltantes -= 1
                        lado_c.update()

                elif self.b != 0 and self.B != 0:
                    if self.a == 0 and self.A != 0:
                        self.a = (self.b * Math.sin(Math.radians(self.A))) / Math.sin(Math.radians(self.B))
                        lado_a.value = f'{round(self.a, 2)}'
                        self.lados_faltantes -= 1
                        lado_a.update()
                    if self.c == 0 and self.C != 0:
                        self.c = (self.b * Math.sin(Math.radians(self.C))) / Math.sin(Math.radians(self.B))
                        lado_c.value = f'{round(self.c, 2)}'
                        self.lados_faltantes -= 1
                        lado_c.update()

                elif self.c != 0 and self.C != 0:
                    if self.a == 0 and self.A != 0:
                        self.a = (self.c * Math.sin(Math.radians(self.A))) / Math.sin(Math.radians(self.C))
                        lado_a.value = f'{round(self.a, 2)}'
                        self.lados_faltantes -= 1
                        lado_a.update()
                    if self.b == 0 and self.B != 0:
                        self.b = (self.c * Math.sin(Math.radians(self.B))) / Math.sin(Math.radians(self.C))
                        lado_b.value = f'{round(self.b, 2)}'
                        self.lados_faltantes -= 1
                        lado_b.update()
            except Exception as error:
                print(error)
                page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
                page.snack_bar.open = True
            print('pasa por la ley del seno')
            

        def ley_coseno_LAL(self):
            try:
                if self.a == 0 and self.b != 0 and self.c != 0 and self.A != 0:
                    self.a = Math.sqrt(Math.pow(self.b, 2) + Math.pow(self.c, 2) - 2 * self.b * self.c * Math.cos(Math.pi * self.A / 180.0))
                    lado_a.value = f'{round(self.a, 2)}'
                    self.lados_faltantes -= 1
                    lado_a.update()
                if self.b == 0.0 and self.a != 0 and self.c != 0 and self.B != 0:
                    self.b = Math.sqrt(Math.pow(self.a, 2) + Math.pow(self.c, 2) - 2 * self.a * self.c * Math.cos(Math.pi * self.B / 180.0))
                    lado_b.value = f'{round(self.b, 2)}'
                    self.lados_faltantes -= 1
                    lado_b.update()
                if self.c == 0 and self.a != 0 and self.b != 0 and self.C != 0:
                    self.c = Math.sqrt(Math.pow(self.b, 2) + Math.pow(self.a, 2) - 2 * self.b * self.a * Math.cos(Math.pi * self.C / 180.0))
                    lado_c.value = f'{round(self.c, 2)}'
                    self.lados_faltantes -= 1
                    lado_c.update()
            except Exception as error:
                print(error)
                page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
                page.snack_bar.open = True
            print('pasa por la ley del coseno lal')
            
        
        def semiperimetro_triangulo(self) -> float:
            try:
                return (self.a + self.b + self.c) / 2
            except Exception as error:
                print(error)
                page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
                page.snack_bar.open = True
            print('pasa por semiperimetro')
        
        
        def area_triangulo(self) -> float:
            try:
                return Math.sqrt(self.semiperimetro * (self.semiperimetro - self.a) * (self.semiperimetro - self.b) * (self.semiperimetro - self.c))
            except Exception as error:
                print(error)
                page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
                page.snack_bar.open = True
            print('pasa por area')
        
        def hl_triangulo(self,p) -> float:
            try:
                return (2 * self.area) / p
            except Exception as error:
                print(error)
                page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
                page.snack_bar.open = True
            print('pasa por altura ha')
            
        def inradio_triangulo(self) -> float:
            try:
                return self.area / self.semiperimetro
            except Exception as error:
                print(error)
                page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
                page.snack_bar.open = True
            print('pasa por inradio')
        
        def circunradio_triangulo(self) -> float:
            try:
                return self.a * self.b * self.c / (4 * self.area)
            except Exception as error:
                print(error)
                page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
                page.snack_bar.open = True
            print('pasa por circunradio')
            
        def mediana(self, p1, p2, p3) -> float:
            try:
                return 1/2 * Math.sqrt( 2 * Math.pow(p1, 2) + 2 * Math.pow(p2, 2) - Math.pow(p3, 2))
            except Exception as error:
                print(error)
                page.snack_bar = ft.SnackBar(ft.Text("Error: Verifica que los datos digitados sean correctos"))
                page.snack_bar.open = True
            print('pasa por mediana')
            
            
    def Limpiar_triangulo(e):
        lado_a.value = ''
        lado_b.value = ''
        lado_c.value = ''
        angulo_a.value = ''
        angulo_b.value = ''
        angulo_c.value = ''
        area.value = ''
        perimetro.value = ''
        semiperimetro.value = ''
        altura_ha.value = ''
        altura_hb.value = ''
        altura_hc.value = ''
        inradio.value = ''
        circunradio.value = ''
        Mediana_ma.value = ''
        Mediana_mb.value = ''
        Mediana_mc.value = ''
        page.update()
    
    
    lado_a = ft.TextField(label="Lado A",width=230)
    lado_b = ft.TextField(label="Lado B", width=230)
    lado_c = ft.TextField(label="Lado C",width=230)
    angulo_a = ft.TextField(label="Angulo A",width=230)
    angulo_b = ft.TextField(label="Angulo B", width=230)
    angulo_c = ft.TextField(label="Angulo C", width=230)
    
    area = ft.TextField(label="Area",disabled=True, width=150)
    perimetro = ft.TextField(label="Perimetro",disabled=True, width=150)
    semiperimetro = ft.TextField(label="Semiperimetro", disabled=True, width=150)
    altura_ha = ft.TextField(label="Altura ha", disabled=True, width=150)
    altura_hb = ft.TextField(label="Altura hb", disabled=True, width=150)
    altura_hc = ft.TextField(label="Altura hc", disabled=True, width=150)
    inradio = ft.TextField(label="Inradio", disabled=True, width=150)
    circunradio = ft.TextField(label="Circunradio", disabled=True, width=150)
    Mediana_ma = ft.TextField(label="Mediana ma", disabled=True, width=150)
    Mediana_mb = ft.TextField(label="Mediana mb", disabled=True, width=150)
    Mediana_mc = ft.TextField(label="Mediana mc", disabled=True, width=150)
    
    
    lados_angulos = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(controls=[lado_a, angulo_a], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START),
                ft.Row(controls=[lado_b, angulo_b], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START),
                ft.Row(controls=[lado_c, angulo_c], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START),
                controls.Buttons(Calcular=resolver_triangulo, Limpiar=Limpiar_triangulo, e=ft.Container),
            ]
        )
    )
    datos = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(controls=[area,perimetro,semiperimetro], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START),
                ft.Row(controls=[altura_ha,altura_hb,altura_hc], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START),
                ft.Row(controls=[Mediana_ma,Mediana_mb,Mediana_mc], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START),
                ft.Row(controls=[inradio,circunradio], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START),
            ]
        )
    )
    
    
    column = ft.Column(
        controls=[
            controls.header_page(page),
            lados_angulos,
            datos,
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
        "/Triangulo",
        [
            stack,
        ],padding=0,
    )
