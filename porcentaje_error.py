import flet as ft
from App_important_controls import controls as ct

def porcentaje_error(page: ft.Page) -> ft.View:
    page.title = 'Porcentaje de error'
    page.scroll = ft.ScrollMode.ALWAYS
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def change_exact(e):
        exact2.value = exact1.value
        exact2.update()
        calculate(e)  
    
    def calculate(e):
        try:
            if exact1.value != '' and aproximate.value != '' and exact1.value != '0':
                absolute_error.value = f'{abs((float(aproximate.value) - float(exact1.value))/float(exact1.value)) * 100} %'
                print(absolute_error.value)
                absolute_error.update()
        except:
            return

    
    # variables de entrada
    aproximate = ft.TextField(label='Valor experimental', width=250)
    exact1 = ft.TextField(label='Valor exacto', width=250,on_change=change_exact)
    exact2 = ft.TextField(label='Valor exacto', width=250)
    #variables de salida
    absolute_error = ft.TextField(label='Error',width=250,disabled=True)
    formula2 = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    aproximate,
                                    ft.Text('-',size=40,color=ft.colors.BLUE_ACCENT),
                                    exact1,
                                ],alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Container(height=2, width=600,bgcolor=ft.colors.BLUE_ACCENT,),
                            ft.Row(
                                controls=[exact2], alignment=ft.MainAxisAlignment.CENTER
                            )
                        ]
                    ),height=130
                ),
                ft.Text('X 100% = ',size=30,color=ft.colors.BLUE_ACCENT),
                absolute_error,
            ]
        ), height=page.height,width=page.width
    )
    
    column = ft.Column(
        controls=[
            ct.header_page(page),
            formula2,
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
            ct.background(ft.Container),
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
        '/Porcentaje_error',
        [
            stack,
        ],padding=0
    )
      
