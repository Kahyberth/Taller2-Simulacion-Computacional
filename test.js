import { Generate } from "./generate.js";
import { Pruebas } from "./pruebasUniformidad.js";
import { Independencia } from "./pruebasIndependencia.js";
const generador = new Generate(5, 8, 1280, 63);

const datos = generador.linealCongruente();
const lista3 = [0.1126, 0.1276 ,0.1426, 0.1576, 0.1726 ,0.1576, 0.1426, 0.1276, 0.1126 ,0.0976, 0.0826 ,0.1046 ,0.1266, 0.1486 ,0.1706 ,0.1926, 0.2146, 0.2366 ,0.2586, 0.2806 ,0.3026 ,0.3246, 0.3072, 0.2898 ,0.2724 ,0.2550, 0.2376, 0.2202, 0.2028, 0.1854 ,0.1680, 0.1506, 0.1332, 0.1158, 0.0984, 0.0810]

const lista4 = [0.00115,0.22461	,0.48433,0.09089,0.68942,
        0.33142	,0.4653,	0.51518,	0.02395,	0.66448,
        0.00066,	0.45972,	0.84643,	0.79442,	0.97112,
        0.2227826,	0.85726,	0.62199,	0.00492,	0.08876,
        0.25956,	0.79147,	0.38179,	0.73897,	0.7936,
        0.23954,	0.68597,	0.44053,	0.01575,	0.91632,
        0.07777,	0.29237,	0.78409,	0.90845,	0.17047,
        0.6064,	0.78343,	0.8886,	0.31993,	0.61788,
        0.69844,	0.81772,	0.17588,	0.7603,	0.9388,
        0.63905,	0.52108,	0.20263,	0.31928,	0.59803
    ]
//const pruebas = new Pruebas(lista4);

const independencia = new Independencia(lista4);
independencia.poker(3);

const uniformidad = new Pruebas(lista4);

uniformidad.kolmogorov();


// pruebas.kolmogorov();
// console.log("Periodo: ", generador.periodo());
// const independencia = new Independencia(lista4);
// const valores = independencia.corridas();
// console.log(lista4.length)



// const lista = [
//     0.08, 0.09, 0.23, 0.29,
//     0.42, 0.55, 0.58, 0.72, 
//     0.89, 0.91, 0.84, 0.74, 0.73, 0.71, 0.53, 
//     0.41, 0.31, 0.18, 0.16, 0.11, 0.01, 0.09,0.30,
//     0.32, 0.45, 0.47, 0.69, 0.74, 0.91, 0.95, 0.91, 
//     0.88, 0.86, 0.68, 0.54, 0.38, 0.36, 0.29, 0.13, 0.12]

// const lista2 = [0.41,0.68 ,0.89 ,0.94, 0.74, 0.91, 0.55 
//     ,0.62 ,0.36 ,0.27, 0.19 ,0.72 ,0.75 ,0.08 ,0.54, 
//     0.02 ,0.01 ,0.36, 0.16, 0.28, 0.18, 0.01 ,0.95, 0.69, 
//     0.18 ,0.47, 0.23, 0.32, 0.82, 0.53, 0.31, 0.42, 0.73, 0.04, 
//     0.83, 0.45, 0.13, 0.57, 0.63, 0.29]

// console.log(lista2.length)
// const independencia = new Independencia(lista2);
// const corridas = independencia.corridas();
// const corridas2 = independencia.conteo();
// console.log(corridas2)


