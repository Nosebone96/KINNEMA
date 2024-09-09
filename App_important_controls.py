import flet as ft

class controls:
    
    def header_page(page: ft.Page):
        page = page
        app_bar = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                            ft.IconButton(ft.icons.CODE_ROUNDED, url='https://github.com/Nosebone96/KINNEMA')
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Divider(height=1, color='white'),
                ]
            ),margin=ft.margin.only(bottom=20,top=10),padding=ft.padding.only(left=10,right=10)
        )
        return app_bar
        
    def Buttons(e, Calcular, Limpiar) -> ft.Container:
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.ElevatedButton(
                        'calcular',
                        on_click=Calcular,                
                        icon=ft.icons.CALCULATE,
                        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)),
                        icon_color='green',
                        height=50,
                        width=150,
                    ),
                    ft.ElevatedButton(
                        'limpiar',
                        on_click=Limpiar,
                        icon=ft.icons.CLEANING_SERVICES,
                        style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30)),
                        height=50,
                        width=150,
                        icon_color="red",
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START, height=50
            )
        )
    def cambio_Textfield(e):
            Textfields = e.control
            try:
                float(Textfields.value)
                Textfields.border_color = ft.TextField.border_color
            except ValueError:
                Textfields.border_color = ft.colors.RED
            if Textfields.value == '':
                Textfields.border_color = ft.TextField.border_color
            Textfields.update()
            
    def background(e) -> ft.Container:
        return ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=["#000000", "#151515", "#0C213B", "#194071", "#2589D0"]
            ),
            expand=True, margin=0, padding=0
        )
    