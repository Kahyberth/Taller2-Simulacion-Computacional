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
        global results
        results = []
        cells = []
        excel = []
        def loadData(e):
            if len(results) > 0 :
                results.pop()
                
            if (nav.selected_index == 0):
                try:
                    print(tx1.value, tx2.value, tx3.value, tx4.value, [generators.value, uniformity_f.value, independence.value])
                    calculo = Calcular(int(tx1.value), int(tx2.value), int(tx3.value), int(tx4.value), [generators.value, uniformity_f.value, independence.value])
                    print("Datos cargados correctamente")
                    page.update()
                except:
                    print("Error al cargar los datos")
            page.update()
            results.append(calculo)
        
        print(results)
        
        def generateExcel(e):
             if uniformity_f.value == "Chi2":
                d = {
                    'Intervalos': excel[0],
                    'Frecuencia Observada': excel[1],
                    'Frecuencia Esperada': excel[2],
                    'Estadístico': excel[3],
                }
                gen_excel = GenerarExcel(d, "Chi2")
                gen_excel.generateExcel()
                
             elif uniformity_f.value == "Kolmogorov":
                d = {
                    'Intervalos': excel[0],
                    'FO': excel[1],
                    'FOA': excel[2],
                    'POA': excel[3],
                    'PEA': excel[4],
                    '|POA-PEA|': excel[5],
                }
                gen_excel = GenerarExcel(d, "Kolmogorov")
                gen_excel.generateExcel()
                
            
        def generate(e):
            gen_numeros = results[0].generate()
            gen_uniformity = results[0].uniformity()
            gen_independence = results[0].independence()

            if uniformity_f.value == "Chi2":
                cells.clear()
                excel.clear()
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
                    
                
                for i in range(4):
                    excel.append(gen_uniformity[i])
        
                    
            elif uniformity_f.value == "Kolmogorov":
                cells.clear()
                excel.clear()
                for i in range(len(gen_uniformity[0])):
                    cells.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(str(gen_uniformity[0][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[1][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[2][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[3][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[4][i]))),
                                ft.DataCell(ft.Text(str(gen_uniformity[5][i-1]))),
                            ]
                        )
                    )
                
                for i in range(6):
                    if i == 5:
                        excel.append(gen_uniformity[i-1])
                    else:
                        excel.append(gen_uniformity[i])

            
            
            
            page.update()


        def selector(e):
            if nav.selected_index == 0:
                loadData(e)
            elif nav.selected_index == 1:
                generate(e)
            elif nav.selected_index == 2:
                generateExcel(e)
        
        
        def dropDown(e):
            if uniformity_f.value == "Chi2":
                try:
                    if len(panel_table.current.controls) > 0:
                        panel_table.current.controls.remove(kolmogorovTable)
                    panel_table.current.controls.append(chi2Table)
                    page.update()
                except:
                    pass

            elif uniformity_f.value == "Kolmogorov":
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

        uniformity_f = ft.Dropdown(
            on_change=dropDown,
            width=200,
            label="Tipo de Uniformidad",
            options=[
                ft.dropdown.Option("Chi2"),
                ft.dropdown.Option("Kolmogorov")
            ]
        )
        
        
        generators = ft.Dropdown(
            width=200,
            label="Tipo de generador",
            options=[
                ft.dropdown.Option("Lineal"),
                ft.dropdown.Option("Estandar Minimo")
            ]
        )
        
        independence = ft.Dropdown(
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
            uniformity_f,
            generators,
            independence
            ],
        height= 250
        )
        
        #TODO: Falta por cambiar los valores predeterminados
        tx1 = ft.TextField(label="X0")
        tx1.width = 80
        tx1.height = 35
        tx1.value = 5
        tx2 = ft.TextField(label="a")
        tx2.width = 80
        tx2.height = 35
        tx2.value = 106
        tx3 = ft.TextField(label="c")
        tx3.width = 80
        tx3.height = 35
        tx3.value = 1280
        tx4 = ft.TextField(label="m")
        tx4.width = 80
        tx4.height = 35
        tx4 .value = 6075
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
                    icon=ft.icons.ACCOUNT_BOX, selected_icon=ft.icons.DONE, label="Cargar Datos",
                    
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


        #Chi-square table
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
        
        #KolmogorovTable
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
                height=800
            )


        
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
                height=630
        ))
            
    ft.app(target=main)