import { Chicuadrado } from './src/Uniformity/chicuadrado.js';
import { Kolmogorov } from "./src/Uniformity/kolmogorov.js";
import { Corridas } from "./src/Independence/corridas.js";

 const lista2 = [0.41,0.68 ,0.89 ,0.94, 0.74, 0.91, 0.55
     ,0.62 ,0.36 ,0.27, 0.19 ,0.72 ,0.75 ,0.08 ,0.54,
     0.02 ,0.01 ,0.36, 0.16, 0.28, 0.18, 0.01 ,0.95, 0.69,
     0.18 ,0.47, 0.23, 0.32, 0.82, 0.53, 0.31, 0.42, 0.73, 0.04,
     0.83, 0.45, 0.13, 0.57, 0.63, 0.29]

const prueba = new Corridas(lista2);
console.log(prueba.corridas());

