from generador import Generador
from independencia import Independencia
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Border, Side
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

lista = Generador(5, 106, 1283, 6075).generadorLinealCongruente()
dato = Independencia(lista)
intervalo = dato.obtenerIntervalo()
frecuenciaObservada = dato.frecuenciaObservada()
frecuenciaEsperada = dato.frecuenciaEsperada()
estadistico = dato.estadistico()
sumaEstadistico = dato.sumaEstadistico()
chiCuadrado = dato.chiCuadrado()

sumaEstadistico = [sumaEstadistico]
chiCuadrado = [chiCuadrado]


if sumaEstadistico <= chiCuadrado:
      print("La muestra sigue la distribución uniforme")
else:
      print("La muestra no sigue la distribución uniforme")


max_length = max(len(intervalo), len(frecuenciaObservada), len(frecuenciaEsperada), len(estadistico))


intervalo += [None] * (max_length - len(intervalo))
frecuenciaObservada += [None] * (max_length - len(frecuenciaObservada))
frecuenciaEsperada += [None] * (max_length - len(frecuenciaEsperada))
estadistico += [None] * (max_length - len(estadistico))
sumaEstadistico += [None] * (max_length - len(sumaEstadistico))
chiCuadrado += [None] * (max_length - len(chiCuadrado))


d = {
    'Intervalos': intervalo,
    'Frecuencia Observada': frecuenciaObservada,
    'Frecuencia Esperada': frecuenciaEsperada,
    'Estadistico': estadistico,
    'Suma Estadistico': sumaEstadistico,
    'Chi Cuadrado': chiCuadrado,
}

df = pd.DataFrame(data=d)


nombreArchivo = 'informe.xlsx'
df.to_excel(nombreArchivo, index=False)


# Genera datos que sigan una distribución normal
mu = 0  # Media
sigma = 1  # Desviación estándar
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)  # Valores de x

# Calcula la PDF de la distribución normal
pdf = norm.pdf(x, mu, sigma)

# Grafica la PDF
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, color='blue', label='Distribución Normal')
plt.xlabel('x')
plt.ylabel('PDF')
plt.title('Gráfico de Distribución Normal (Campana)')
plt.legend()
plt.grid()
plt.show()