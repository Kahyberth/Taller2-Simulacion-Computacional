import Table from 'cli-table3';
export class Independencia {
    constructor(lista) {
        this.lista = lista;
    }

    corridas() {
        const datos = this.lista;
        const media = ((2 * datos.length) - 1) / 3;
        const varianza = ((16 * datos.length) - 29) / 90;
        const zconteo = this.conteo();
        const z = (zconteo - media) / Math.sqrt(varianza);
        console.log("Varianza: ", varianza)
        console.log("zconteo: ", zconteo)
        console.log("Media: ", media);
        console.log(z);
        if (-1.96 <= z && z <= 1.96) {
            console.log("Los números son independientes");
        }
    }


    conteo() {
        const datos = this.lista;
        let positivo = "";
        let negativo = "";
        const corridas = [];
        datos.forEach((dato, index) => {
            if (index > 0) {
                if (dato > datos[index - 1]) {
                    positivo += "+";
                    if (negativo != "") {
                        corridas.push(negativo);
                        negativo = "";
                    }
                }
                else {
                    if (positivo != "") {
                        corridas.push(positivo);
                        positivo = "";
                    }
                    negativo += "-";
                }
            }
        });

        return corridas.length + 1;
    }


    series () {
        const k = 2
        const datos = this.lista;
        const n_grupos = datos.length / k;
        const c = Math.ceil(Math.sqrt(n_grupos));
        const n_clases = Math.ceil(Math.sqrt(Math.sqrt(n_grupos)));
        let series = [];
        const rangos = [
            [0, 0.2],
            [0.2, 0.4],
            [0.4, 0.6],
            [0.6, 0.8],
            [0.8, 1],
          ];
          for(let i = 0; i < n_clases; i++) {
            const data = this.filterByRange(rangos[i]);
            series.push(data);
          }
        return series[0].length;
    }

    filterByRange (rango) {
        const datos = this.lista;
        const serie = []
        datos.forEach(dato => {
            if (rango[0] <= dato && dato < rango[1]) {
                serie.push(dato);
            }
        });

        return serie;
    }


    poker() {
        let table = new Table({
            head: ['Tipo de Poker', 'FO', 'FE', 'Chi Cuadrado'],
            style: {
              head: [], //disable colors in header cells
              border: [], //disable colors for the border
            },
            colWidths: [30, 30, 30, 30], //set the widths of each column (optional)
          });
        const tabulados = [];
        let iguales = 10*1*1/1000;
        let igual_diferente = 10*9*3/1000;
        let diferentes = 10*9*8/1000;
        const datos = this.lista;
        const digitos = [];
        datos.forEach(e => digitos.push(e.toString().split('.')[1].slice(0,3)));
        const resultado = this.contarSimilitudes(digitos);

        iguales *= datos.length;
        igual_diferente *= datos.length;
        diferentes *= datos.length;

        const poker3 = resultado.poker3;
        const poker2 = resultado.poker2;
        const poker1 = resultado.poker1;

        tabulados.push([3, poker3, iguales, (Math.pow((iguales - poker3), 2)/ iguales)]);
        tabulados.push([2, poker2, igual_diferente, (Math.pow((igual_diferente - poker2), 2)/ igual_diferente)]);
        tabulados.push([1, poker1, diferentes, (Math.pow((diferentes - poker1), 2)/ diferentes)]);
        

    
        table.push(...tabulados);
        
        console.log(table.toString());


        
    }

    contarSimilitudes(arrayDeStrings) {
        const resultados = { poker3: 0, poker2: 0, poker1: 0 };

        for (const str of arrayDeStrings) {
            const ocurrencias = {};

            for (const char of str) {
                ocurrencias[char] = (ocurrencias[char] || 0) + 1;
            }

            let tieneCoincidencias = false;

            for (const key in ocurrencias) {
                const count = ocurrencias[key];

                if (count >= 3) {
                    resultados.poker3 += 1;
                    tieneCoincidencias = true;
                } else if (count === 2) {
                    resultados.poker2 += 1;
                    tieneCoincidencias = true;
                }
            }

            if (!tieneCoincidencias) {
                resultados.poker1 += 1;
            }
        }

        return resultados;
    }



}