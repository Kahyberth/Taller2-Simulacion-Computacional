import { Chicuadrado } from './src/Uniformity/chicuadrado.js';
import { Kolmogorov } from "./src/Uniformity/kolmogorov.js";
import { Corridas } from "./src/Independence/corridas.js";
import { LinealCongruente } from "./src/Generator/linealcongruente.js";


const datos = new LinealCongruente(5,106,1280,6075);
const valores = datos.linealCongruente();

const prueba = new Corridas(valores);
console.log(prueba.corridas());
