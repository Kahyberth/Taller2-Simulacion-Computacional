import { Generate } from "./generate.js";
import Table from 'cli-table';
const generador = new Generate(5, 106, 1283, 6075, 100);

//Proceso de generación de números aleatorios
const datos = generador.linealCongruente();
const numero_clases = Math.sqrt(datos.length);
const gradosLibertad = numero_clases - 1;
let sumChi = 0;
const tabulado = []
const table = new Table({
    head: ['Clase', 'FO', 'FE', 'Chi Cuadrado'],
    colWidths: [10, 15, 20, 20]
});

for (let i = 0; i < numero_clases; i++) {
    const FO = datos.filter(dato => dato >= i / numero_clases && dato < (i + 1) / numero_clases).length;
    const FE = datos.length / numero_clases;
    const diferencia = Math.pow(FO - FE, 2);
    const chi = diferencia / FE;
    sumChi += chi;
    tabulado.push([(i + 1).toString(),FO.toString(), FE.toString(), chi.toString()]);
}


for (const row of tabulado) {
    table.push(row);
}


console.log(datos)
//const periodo = datos.length;
console.log(table.toString());

const periodo = generador.periodo();

if (sumChi <= 16.919) {
    console.log(
    `
    Los números generados son uniforme, 
    suma chi cuadrado: ${sumChi}
    Perido de la secuencia: ${periodo}
    Grados de libertad: ${gradosLibertad}
    Numero de clases: ${numero_clases}
    Cantidad de números generados: ${datos.length}
    `);
} else {
    console.log(`Los números generados no son uniformes`);
}