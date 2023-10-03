import { Chicuadrado } from './src/Uniformity/chicuadrado.js';
import { Kolmogorov } from "./src/Uniformity/kolmogorov.js";
import { Corridas } from "./src/Independence/corridas.js";
import { LinealCongruente } from "./src/Generator/linealcongruente.js";
import { Poker } from "./src/Independence/poker.js";
import { Series } from "./src/Independence/series.js";

const datos = new LinealCongruente(5,106,1280,6075);
const valores = datos.linealCongruente();

const data = []
for(let i = 0; i <= 100; i++) {
    let valoresRandom = Math.random( i );
   data.push(valoresRandom);
}

//const series = new Series(lista4);
//const array = series.groupValues(lista4, 2);
//console.log(array);


const chi2 = new Chicuadrado(data);
//uniformidad.chicuadrado();

const kolmogorov = new Kolmogorov(data);
//kolmogorov.kolmogorov();

const corridas = new Corridas(data);

//console.log(corridas.corridas());


const poker = new Poker(data);
poker.poker_5();

