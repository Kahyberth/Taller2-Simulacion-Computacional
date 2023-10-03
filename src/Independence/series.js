import Table from "cli-table3";

export class Series {
    constructor(list) {
        this.lst = list;
    }


    series( k_value = 2 ) {
        const k = k_value;
        const data_list = this.lst;
        console.log(data_list.length);
        const n_groups =  data_list / k;
        const n_classes = Math.ceil(Math.sqrt(n_groups));
        const grouped_values = this.groupValues(data_list, n_groups);
        let table = new Table({
            head: [' ','[0-0.2)', '[0.2-0.4)', '[0.4,0.6)', '[0.6,0.8)','[0.8,1)'],
            style: {
                head: [],
                border: [],
            },
            colWidths: [15,15, 15, 15, 15,15],
        });

        console.log(table.toString());
        for (const i of grouped_values) {
            for (const iElement of i) {

            }
        }


    }

    filterByRange(data_list) {
        const range = [
            [0,0.2],
            [0.2,0.4],
            [0.4,0.6],
            [0.6,0.8],
            [0.8,1]
        ]

        const quantity = [];
        for (const rangeElement of range) {
            quantity.push(data_list.filter(data => data >= rangeElement[0] && data < rangeElement[1]).length);
        }

        return quantity;
    }


    groupValues(data_list, quantity) {
        const groups = [];
        for(let i = 0; i < data_list.length; i += quantity) {
            groups.push(data_list.slice(i, i + quantity));
        }
        return groups;
    }




}