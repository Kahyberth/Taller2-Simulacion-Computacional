import flet as ft
import numpy as np
from calcular import Calcular

def main(page: ft.Page):
    pb = ft.ProgressBar(width=400)
    def selector(e):
        datos = []
        if (e.control.selected_index == 0):
            layaout.controls.append(
                ft.Row(
                    controls=[
                        ft.Text("Generando Números", style="headlineSmall"),
                        ft.Column([ ft.Text("Procesando....."), pb]), 
                    ]
            ))
            page.update()  
            app = Calcular(5, 106, 1283, 6075,["Lineal Congruente", "Chi Cuadrado"])
            app.generate()  
            app.independencia()
            layaout.controls.pop()
            page.update()     
            datos = app.datos
            print(datos[1])
            
            
            
        elif (e.control.selected_index == 1):            
            print(datos[1])
        elif (e.control.selected_index == 2):
            print("Generar PDF")
      
    rail = ft.NavigationRail(
    selected_index=0,
    label_type=ft.NavigationRailLabelType.ALL,
    extended=False,
    min_width=100,
    min_extended_width=400,
    leading=ft.Image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", width=100, height=100),
    group_alignment=-0.9,
    destinations=[
        ft.NavigationRailDestination(
            icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.SETTINGS_OUTLINED, label="Generar"
        ),
        ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.LIST),
            selected_icon_content=ft.Icon(ft.icons.DONE),
            label="Independencia",
        ),
        ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.LINE_AXIS_ROUNDED),
            selected_icon_content=ft.Icon(ft.icons.DONE),
            label="Uniformidad",
        ),
         ft.NavigationRailDestination(
            label_content=ft.TextField(label="x0", width=80)
        ),
         ft.NavigationRailDestination(
            label_content=ft.TextField(label="a", width=80)
        ),
         ft.NavigationRailDestination(
            label_content=ft.TextField(label="c", width=80)
        ),
         ft.NavigationRailDestination(
             
            label_content=ft.TextField(label="m", width=80)
        ),
        ft.NavigationRailDestination(
            icon=ft.icons.EXPAND_CIRCLE_DOWN,
            selected_icon_content=ft.Icon(ft.icons.DONE),
            label_content=ft.Text("Generar Excel"),
        ),
        
    ],
    on_change=selector,
    height=800,
    width=300,
)

    
    
            
    
    tabla =  ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Intervalos")),
                ft.DataColumn(ft.Text("Frecuencia Observada")),
                ft.DataColumn(ft.Text("Frecuencia Esperada")),
                ft.DataColumn(ft.Text("Estadístico")),
            ],
            rows= [],
            width=600,
            height=800
        )

    
    

        
    
    tableControl =  ft.Ref[ft.Column]()
    
    
    layaout =  ft.Column(
            controls=[
                ft.Row(
                    [
                        rail,
                        ft.VerticalDivider(width=1),
                        ft.Column(ref=tableControl, controls=[tabla], scroll= ft.ScrollMode.ALWAYS, width=600, height=800),
                        ft.VerticalDivider(width=1),
                    ],
                    
                    
                ),
            ],
            scroll= ft.ScrollMode.ALWAYS,
        )
    
    page.add(
       layaout
    )

ft.app(target=main)