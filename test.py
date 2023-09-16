from generador import Generador
from independencia import Independencia
import pandas as pd

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
    'Intervalo': intervalo,
    'Frecuencia Observada': frecuenciaObservada,
    'Frecuencia Esperada': frecuenciaEsperada,
    'Estadistico': estadistico,
    'Suma Estadistico': sumaEstadistico,
    'Chi Cuadrado': chiCuadrado,
}

df = pd.DataFrame(data=d)


nombreArchivo = 'informe.xlsx'
df.to_excel(nombreArchivo, index=False)