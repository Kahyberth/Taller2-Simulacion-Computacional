import { Generate } from "./generate.js";
import { Pruebas } from "./pruebasUniformidad.js";
import { Independencia } from "./pruebasIndependencia.js";
const generador = new Generate(5, 5, 13, 64);

const datos = generador.linealCongruente();

const pruebas = new Pruebas(datos);

// pruebas.kolmogorov();
// console.log("Periodo: ", generador.periodo());

const lista = [
    0.08, 0.09, 0.23, 0.29,
    0.42, 0.55, 0.58, 0.72, 
    0.89, 0.91, 0.84, 0.74, 0.73, 0.71, 0.53, 
    0.41, 0.31, 0.18, 0.16, 0.11, 0.01, 0.09,0.30,
    0.32, 0.45, 0.47, 0.69, 0.74, 0.91, 0.95, 0.91, 
    0.88, 0.86, 0.68, 0.54, 0.38, 0.36, 0.29, 0.13, 0.12]

const lista2 = [0.41,0.68 ,0.89 ,0.94, 0.74, 0.91, 0.55 
    ,0.62 ,0.36 ,0.27, 0.19 ,0.72 ,0.75 ,0.08 ,0.54, 
    0.02 ,0.01 ,0.36, 0.16, 0.28, 0.18, 0.01 ,0.95, 0.69, 
    0.18 ,0.47, 0.23, 0.32, 0.82, 0.53, 0.31, 0.42, 0.73, 0.04, 
    0.83, 0.45, 0.13, 0.57, 0.63, 0.29]

console.log(lista2.length)
const independencia = new Independencia(lista2);
const corridas = independencia.corridas();
