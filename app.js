import { Chicuadrado } from './src/Uniformity/chicuadrado.js';
import { Kolmogorov } from "./src/Uniformity/kolmogorov.js";
import { Corridas } from "./src/Independence/corridas.js";
import { LinealCongruente } from "./src/Generator/linealcongruente.js";
import { Poker } from "./src/Independence/poker.js";
import { Series } from "./src/Independence/series.js";
import { Estandarminimo} from "./src/Generator/estandarminimo.js";
import {independenceMenu, input, menu, pause, pokerMenu, pseudoMenu, uniformityMenu} from "./src/Menu/menu.js";


const main = async () => {
    let opt = "";

    let numPesudoAleatorios = 0;
    let uniformityValue = 0;
    let independeceValue = 0;

    const values = {
        xo: 0,
        a: 0,
        c: 0,
        m: 0
    }

    do {
        opt = await menu();
        switch (opt) {
            case '1':
                const pseudoAleatorios = await pseudoMenu();
                if ( pseudoAleatorios !== '3') {
                    for (let i = 0; i < 4; i++) {
                        const dato = await input(`Ingrese el valor de: ${Object.keys(values)[i]}`);
                        values[Object.keys(values)[i]] = dato;
                    }
                }
                switch (pseudoAleatorios){
                    case '1':
                        numPesudoAleatorios = new LinealCongruente(values.xo, values.a, values.c, values.m);
                        numPesudoAleatorios = numPesudoAleatorios.linealCongruente();
                        console.log(numPesudoAleatorios);
                        break;
                    case '2':
                        numPesudoAleatorios = new Estandarminimo(values.xo, values.a, values.c, values.m);
                        numPesudoAleatorios = numPesudoAleatorios.estandarMinimo();
                        console.log(numPesudoAleatorios);
                        break;
                    case '3':
                        const data = [];
                        for (let i = 0; i < 100; i++) {
                            data.push(Math.random(i));
                        }
                        numPesudoAleatorios = data;
                        console.log(numPesudoAleatorios);
                        break;
                }
                break;
            case '2':
                const uniformity = await uniformityMenu();
                switch (uniformity) {
                    case '1':
                        uniformityValue = new Chicuadrado(numPesudoAleatorios);
                        uniformityValue.chicuadrado();
                        break;
                    case '2':
                        uniformityValue = new Kolmogorov(numPesudoAleatorios);
                        uniformityValue.kolmogorov();
                        break;
                }
                break;
            case '3':
                const independence = await independenceMenu();
                switch (independence) {
                    case '1':
                        independeceValue = new Corridas(numPesudoAleatorios);
                        independeceValue.corridas();
                        break;
                    case '2':
                        independeceValue = new Series(numPesudoAleatorios);
                        independeceValue.series(2);
                        break;
                    case '3':
                        independeceValue = new Poker(numPesudoAleatorios);
                        const poker = await pokerMenu();
                        if(poker === '3'){
                            independeceValue.poker_3()
                        }
                        else if (poker === '5') {
                            independeceValue.poker_5()
                        }
                        break;
                }
                break;
        }

        await pause();
    } while (opt !== '0');
}

main();