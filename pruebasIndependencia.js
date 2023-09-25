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
}