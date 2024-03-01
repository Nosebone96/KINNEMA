import flet as ft

    
def header_page(e, Volver_main) -> ft.Container:
    return ft.Container(
        ft.Row(
            [
                ft.IconButton(
                    icon= ft.icons.KEYBOARD_ARROW_LEFT_SHARP,
                    icon_size=40,
                    icon_color='blue',
                    on_click=Volver_main,
                )
            ]
        )
    )