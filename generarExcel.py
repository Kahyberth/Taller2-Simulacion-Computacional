import pandas as pd
import os
class GenerarExcel:
    def __init__(self, d, nombre_archivo_excel):
        self.d = d
        self.nombre_archivo_excel = nombre_archivo_excel
    
    def generarExcel(self):
        nombre_archivo_excel = self.nombre_archivo_excel
        ruta_completa = os.path.join("Tablas", nombre_archivo_excel + ".xlsx")
        df = pd.DataFrame(data=self.d)
        df.to_excel(ruta_completa, index=False)
    