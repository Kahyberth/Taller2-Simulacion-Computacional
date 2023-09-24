import { Generate } from "./generate.js";
import { Pruebas } from "./pruebas.js";
const generador = new Generate(5, 5, 13, 64);

const datos = generador.linealCongruente();

const pruebas = new Pruebas(datos);

pruebas.chi_cuadrado();
console.log("Periodo: ", generador.periodo());

