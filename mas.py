import flet as ft 
import math as m 

def main_mas(page: ft.Page) -> ft.page:

    
    def Calcular_PP(e):
        i = 0
        try:
            p_p = float(P_pendulo.value)
        except ValueError:
            i += 1
        try:
            l_p = float(L_pendulo.value)
        except ValueError:
            i += 1
        try:
            g_p = float(G_pendulo.value)
        except ValueError:
            i += 1
        if i >= 2:
            return 
        if P_pendulo.value == '':
            P_pendulo.value = f'{2 * m.pi * m.sqrt(l_p / g_p)}'
        if L_pendulo.value == '':
            L_pendulo.value = f'{(g_p / (4 * m.pi**2)) * p_p**2}'
        if G_pendulo.value == '':
            G_pendulo.value = f'{(4 * m.pi**2 * l_p) / p_p**2}'
        page.update()

    def Limpiar_PP(e):
        P_pendulo.value = ''
        L_pendulo.value = ''
        G_pendulo.value = ''
        page.update()

    def Calcular_PR(e):
        i = 0
        try:
            p_r = float(P_resorte.value)
        except ValueError:
            i += 1
        try:
            m_r = float(M_resorte.value)
        except ValueError:
            i += 1
        try:
            k_r = float(K_resorte.value)
        except ValueError:
            i += 1
        if i >= 2:
            return 
        if P_resorte.value == '':
            P_resorte.value = f'{2 * m.pi * m.sqrt(m_r / k_r)}'
        if M_resorte.value == '':
            M_resorte.value = f'{(k_r / (4 * m.pi**2)) * p_r**2}'
        if K_resorte.value == '':
            K_resorte.value = f'{(4 * m.pi**2 * m_r) / p_r**2}'
        page.update() 
    
    def Limpiar_PR(e):
        P_resorte.value = ''
        M_resorte.value = ''
        K_resorte.value = ''
        page.update() 
    
    P_pendulo = ft.TextField(label="Periodo:", )
    L_pendulo = ft.TextField(label='Longitud:',)
    G_pendulo = ft.TextField(label='Gravedad:',)
    
    P_resorte = ft.TextField(label="Periodo:",)
    M_resorte= ft.TextField(label='Masa:',)
    K_resorte = ft.TextField(label='Constante elastica:',)

    content_pendulo = ft.Container(
    content=ft.Column(
        controls=[
            P_pendulo,
            L_pendulo,
            G_pendulo,
            ft.ElevatedButton(text="Calcular", on_click=Calcular_PP),
            ft.ElevatedButton(text="Limpiar", on_click=Limpiar_PP)
        ]
    ),
    margin=20,
    padding=30
)

    content_resorte = ft.Container(
    content=ft.Column(
        controls=[
            P_resorte,
            M_resorte,
            K_resorte,
            ft.ElevatedButton(text="Calcular", on_click=Calcular_PR),
            ft.ElevatedButton(text="Limpiar", on_click=Limpiar_PR)
        ]
    ),
    margin=20,
    padding=30
)

    Tabs_mas = ft.Tabs(
        selected_index=0,
        animation_duration=400,
        tabs=[
            ft.Tab(
                text = 'Péndulo simple',
                content=content_pendulo
            ),
            ft.Tab(
                text = 'Sistema masa-resote',
                content=content_resorte
            ),
        ]
    )
    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=Tabs_mas, 
                    margin= ft.margin.only(top= 10, left= 0, right=0)
                ),
            ]
        )
    )
ft.app(target=main_mas)


