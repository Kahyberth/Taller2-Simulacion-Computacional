import Table from "cli-table3";
export class Kolmogorov {

    constructor(lista) {
        this.lst = lista;
    }

    kolmogorov() {

        let table = new Table({
            head: ['Clase', 'Fo', 'Foa', 'Poa', 'Pea', '|Pea-Poa|'],
            style: {
                head: [],
                border: [],
            },
            colWidths: [18, 18, 18, 18, 18, 18],
        });

        const data_list = this.lst;
        const number_of_classes = 10;
        const grades = data_list.length;
        const kolmogorov_data = [];
        let FOA = 0;
        for(let i  = 0; i < number_of_classes; i++) {
            const FO = data_list.filter(data => data >= i / number_of_classes && data < (i + 1) / number_of_classes).length;
            FOA = FO + FOA;
            const POA = FOA / data_list.length;
            const PEA = (i + 1) / number_of_classes;
            kolmogorov_data.push(Math.abs(PEA - POA));
            table.push([`[${(i)/number_of_classes} , ${(i + 1)/number_of_classes}]`, FO, FOA, POA,PEA, Math.abs(PEA-POA)]);
        }

        const dm_calc = kolmogorov_data.reduce((a,b) => Math.max(a,b));
        console.log(table.toString());
    }


}