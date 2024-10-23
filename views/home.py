import flet as ft
from models.Models import controls as ct


def home(page: ft.Page) -> ft.View:
    page.title = 'KINNEMA'
    page.scroll = ft.ScrollMode.ALWAYS
    
    # Función para crear un botón personalizado
    def crear_boton(icono, texto, ruta):
        return ft.OutlinedButton(
            on_click=lambda e: page.go(ruta),
            content=ft.Row(
                controls=[
                    ft.Icon(name=icono, color='white'),
                    ft.Text(value=texto, text_align=ft.TextAlign.CENTER),
                ], alignment=ft.MainAxisAlignment.CENTER,
            ),
            expand=True,
            height=50
        )

    # Lista de botones a crear con sus parámetros
    botones = [
        (ft.icons.SYNC_ALT, 'MAS', '/MAS'),
        (ft.icons.SCALE, 'Balanceo Estequiometrico', '/Balanceo_estequiometrico'),
        (ft.icons.SPEED, 'MRUV', '/MRUV'),
        (ft.icons.BOLT, 'Resistencia', '/Valor_resistencia'),
        (ft.icons.FLASH_ON, 'Energía mecanica', '/Energia_mecanica'),
        (ft.icons.LINE_WEIGHT, 'Ley Snell', '/Ley_de_snell'),
        (ft.icons.ELECTRIC_BOLT, 'Carga electrica', '/Carga_electrica'),
        (ft.icons.COMPARE_ARROWS_ROUNDED, 'Ley Coulomb', '/ley_de_coulomb'),
        (ft.icons.CHANGE_HISTORY, 'Triangulo', '/Triangulo'),
        (ft.icons.PERCENT, 'Error', '/Porcentaje_error'),
        (ft.icons.PERCENT, 'Ley de Ohm', '/ley_de_ohm'),
    ]

    # Crear filas con dos botones cada una
    filas = [ft.Container(height=100, width=1)]  # Inicializa la lista de filas
    for i in range(0, len(botones), 2):
        if i + 1 < len(botones):
            # Si hay un par de botones
            fila = ft.Row(
                controls=[
                    crear_boton(*botones[i]),        # Primer botón
                    crear_boton(*botones[i + 1])     # Segundo botón (existe)
                ]
            )
        else:
            # Si es el último botón y no tiene par
            fila = ft.Row(
                controls=[
                    crear_boton(*botones[i]),        # Solo el primer botón
                    ft.Container()  # Un contenedor vacío como placeholder
                ]
            )
        filas.append(fila)

    # Crear el layout principal
    column = ft.Column(
        filas,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        width=page.width,
        height=page.height,
        spacing=20
    )
    
    
    
    
    content = ft.Row(
        controls=[
            column
        ],
        scroll=ft.ScrollMode.ALWAYS,  # Permite scroll horizontal
        width=page.width,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    

    stack = ft.Stack(
        [
            ct.background(ft.Container),
            ct.containers(page),
            ct.example(page=page),
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
        '/',
        [
            stack,
        ],padding=0
    )