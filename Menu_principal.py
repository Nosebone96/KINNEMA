import flet as ft


def main(page):
    t = ft.Text(value="KINNEMA", color="blue", size=20)
    page.controls.append(t)
    page.update()
   

ft.app(target=main)