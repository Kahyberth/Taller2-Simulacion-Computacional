import  Table from 'cli-table3'
export class Chicuadrado {

    constructor(list) {
        this.lst = list;
    }

    chicuadrado() {
        let table = new Table({
            head: ['Clase', 'Fo', 'Fe', 'Chi-Cuadrado'],
            style: {
                head: [],
                border: [],
            },
            colWidths: [30, 30, 30, 30],
        });

        const data_list = this.lst;
        const number_of_classes = 10;
        const grades = number_of_classes - 1;
        let sumChi = 0;
        for (let i = 0; i < number_of_classes; i++) {
            const FO = data_list.filter(data => data >= i / number_of_classes && data < (i + 1) / number_of_classes).length;
            const FE = data_list.length / number_of_classes;
            const difference = Math.pow(FO - FE, 2);
            const chi = difference / FE;
            sumChi += chi;
            table.push([`[${(i)/number_of_classes} , ${(i + 1)/number_of_classes}]`,FO, FE, chi])
        }

        console.log(table.toString())



    }


}