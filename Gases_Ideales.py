import flet as ft
import importlib 
def main(page: ft.page):
    page.title = "Gases Idelaes"
    def Volver_main(e):
        page.controls.clear()
        page.go(importlib.import_module('Menu_principal').main(page))
        