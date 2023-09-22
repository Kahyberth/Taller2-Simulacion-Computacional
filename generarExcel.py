import pandas as pd
import os


class GenerarExcel:
    def __init__(self, d, nombre_archivo_excel):
        self.d = d
        self.file_name = nombre_archivo_excel

    def generateExcel(self):
        excel_file = self.file_name
        path = os.path.join("Results", excel_file + ".xlsx")
        df = pd.DataFrame(data=self.d)
        df.to_excel(path, index=False)
