import flet as ft
from flet import (Page)
import numpy as np
from calcular import Calcular
from generarExcel import GenerarExcel
global calculo
calculo = 100
class App:
    def __init__(self) -> None:
        pass
    
    def main(page: Page):      
        global resultado 
        resultado = []
        cells = []
        excel = []
        def loadData(e):
            if len(resultado) > 0 :
                print(len(resultado))
                resultado.pop()
            if (nav.selected_index == 0):
                try:
                    print(tx1.value, tx2.value, tx3.value, tx4.value, [generadores.value, uniformidad.value, independencia.value])
                    calculo = Calcular(int(tx1.value), int(tx2.value), int(tx3.value), int(tx4.value), [generadores.value, uniformidad.value, independencia.value])
                    print("Datos cargados correctamente")
                    page.update()
                except:
                    print("Error al cargar los datos")
            resultado.append(calculo)
        
        
        
        def generarExcel(e):
            if uniformidad.value == "Chi2":
                d = {
                    'Rango': excel[0],
                    'FO': excel[1],
                    'FE': excel[2],
                    'Estadístico': excel[3],
                    }
                GenerarExcel(d, "Chi2").generarExcel()
            elif uniformidad.value == "Kolmogorov":
                d = {
                    'Rango': excel[0],
                    'FO': excel[1],
                    'FOA': excel[2],
                    'POA': excel[3],
                    'PEA': excel[4],
                    '|POA-PEA|': excel[5],
                    }
                gen_excel = GenerarExcel(d, "Kolmogorov")
                gen_excel.generarExcel()
            
       
        
        
        def generar(e):
            gen_numeros = resultado[0].generate()
            gen_uniformity = resultado[0].uniformity()
            
            if uniformidad.value == "Chi2":
                for i in range(len(gen_uniformity[0])):
                    cells.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(str(gen_uniformity[0][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[1][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[2][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[3][i]))),
                            ]
                        )
                    )
                    
                    excel.append(gen_uniformity[0][i])
                    excel.append(gen_uniformity[1][i])  
                    excel.append(gen_uniformity[2][i])
                    excel.append(gen_uniformity[3][i])

                
        
                    
            elif uniformidad.value == "Kolmogorov":
                for i in range(len(gen_uniformity[0])-1):
                    cells.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(str(gen_uniformity[0][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[1][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[2][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[3][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[4][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[5][i]))),
                            ]
                        )
                    )
                
                excel.append(gen_uniformity[0][i])
                excel.append(gen_uniformity[1][i])
                excel.append(gen_uniformity[2][i])
                excel.append(gen_uniformity[3][i])
                excel.append(gen_uniformity[4][i])
                excel.append(gen_uniformity[5][i])
            
            
            page.update()
            print(gen_uniformity)
        
        def selector(e):
            if nav.selected_index == 0:
                loadData(e)
            elif nav.selected_index == 1:
                generar(e)
            elif nav.selected_index == 2:
                generarExcel(e)
        
        
        def dropDown(e):
            if uniformidad.value == "Chi2":
                try:
                    if len(panel_table.current.controls) > 0:
                        panel_table.current.controls.remove(kolmogorovTable)
                    panel_table.current.controls.append(chi2Table)
                    page.update()
                except:
                    pass
                
            elif uniformidad.value == "Kolmogorov":
                try:
                    if len(panel_table.current.controls) > 0:
                        panel_table.current.controls.remove(chi2Table)
                    panel_table.current.controls.append(kolmogorovTable)
                    page.update()
                except:
                    pass
                
                
        def theme_changed(e):
            page.theme_mode = (
                ft.ThemeMode.DARK
                if page.theme_mode == ft.ThemeMode.LIGHT
                else ft.ThemeMode.LIGHT
            )
            c1.label = (
                "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
            )
            page.update()
        
        
    
        c1 = ft.Switch(label="Light theme", value = True, on_change=theme_changed)
        
        uniformidad = ft.Dropdown(
            on_change=dropDown,
            width=200,
            label="Tipo de Uniformidad",
            options=[
                ft.dropdown.Option("Chi2"),
                ft.dropdown.Option("Kolmogorov")
            ]
        )
        
        
        generadores = ft.Dropdown(
            width=200,
            label="Tipo de generador",
            options=[
                ft.dropdown.Option("Lineal"),
                ft.dropdown.Option("Estandar Minimo")
            ]
        )
        
        independencia = ft.Dropdown(
            width=200,
            label="Tipo de independencia",
            options=[
                ft.dropdown.Option("Corridas"),
                ft.dropdown.Option("Series"),
                ft.dropdown.Option("Poker")
            ]
        )
        
        
        container = ft.Column(
            controls=[
            c1,
            uniformidad,
            generadores,
            independencia
            ],
        height= 250
        )
        
        
        tx1 = ft.TextField(label="X0")
        tx1.width = 80
        tx1.height = 35
        tx2 = ft.TextField(label="a")
        tx2.width = 80
        tx2.height = 35
        tx3 = ft.TextField(label="c")
        tx3.width = 80
        tx3.height = 35
        tx4 = ft.TextField(label="m")
        tx4.width = 80
        tx4.height = 35
        container2 = ft.Column(
            controls=[
                tx1,
                tx2,
                tx3,
                tx4  
            ],
        )
        nav = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.ACCESSIBILITY, selected_icon=ft.icons.DONE, label="Cargar Datos",
                    
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FUNCTIONS,label="Generar"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.BOOK, selected_icon=ft.icons.DONE, label="Exportar a Excel"
                ),
            ],
            
            on_change= selector,
            width= 170,
            height= 180
        )


        


        
        
                
        
        chi2Table =  ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Intervalos")),
                    ft.DataColumn(ft.Text("Frecuencia Observada")),
                    ft.DataColumn(ft.Text("Frecuencia Esperada")),
                    ft.DataColumn(ft.Text("Estadístico")),
                ],
                rows= cells,
                width=1000,
                height=600
            )
        
        kolmogorovTable =  ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Intervalos")),
                    ft.DataColumn(ft.Text("FO")),
                    ft.DataColumn(ft.Text("FOA ")),
                    ft.DataColumn(ft.Text("POA")),
                    ft.DataColumn(ft.Text("PEA")),
                    ft.DataColumn(ft.Text("|POA-PEA|")),
                ],
                rows= cells,
                width=1000,
                height=600
            )

        
        

            
        
        tableControl =  ft.Ref[ft.Column]()
        
        panel = ft.Column(
            controls=[
                nav,
                container,
                container2,
            ],
        )
        
        panel_table = ft.Ref[ft.Column]()
        
        
        page.add(ft.Row(
            controls=[
                panel,
                ft.VerticalDivider(width=1),
                ft.Column(
                    ref=panel_table,
                    controls=[],
                    height=620),
                ft.VerticalDivider(width=1),
            ],
                height=620
        ))
            
    ft.app(target=main)