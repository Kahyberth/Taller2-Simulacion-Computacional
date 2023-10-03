import Table from "cli-table3";

export class Corridas {
    constructor(list) {
        this.lst = list;
    }


    corridas() {

        let table = new Table({
            head: ['MEDIA', 'VARIANZA', 'CONTEO', 'Z', 'INDEPENDIENTE'],
            style: {
                head: [],
                border: [],
            },
            colWidths: [20, 20, 10, 18, 18],
        });


        const data_list = this.lst;
        const avarage = ((2 * data_list.length) - 1) / 3;
        const varaince = ((16 * data_list.length) - 29) / 29;
        const counter = this.conteo();
        const z_value = ( counter - avarage) / Math.sqrt(varaince);

        if (-1.96 <= z_value && z_value <= 1.96) {
            table.push([avarage, varaince, counter, z_value, true]);
        }
        else {
            table.push([avarage, varaince, counter, z_value, false]);
        }

        console.log(table.toString());
        return z_value;
    }


    conteo() {
        const data_list = this.lst;
        let positive = "";
        let negative = "";
        const runs = [];

        data_list.forEach((dato, index) => {
            if (index > 0) {
                if (dato > data_list[index - 1]) {
                    if (negative != "") {
                        runs.push(negative);
                        negative = "";
                    }
                    positive += "+";
                }
                else {
                    if (positive != "") {
                        runs.push(positive);
                        positive = "";
                    }
                    negative += "-";
                }
            }
        });

        return runs.length + 1;
    }

}