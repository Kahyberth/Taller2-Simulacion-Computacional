import Table from "cli-table3";

export class Series {
    constructor(list) {
        this.lst = list;
    }


    series( k_value = 2 ) {
        const k = k_value;
        const data_list = this.lst;
        console.log(data_list.length);
        const n_groups =  data_list.length / k;
        const n_classes = Math.ceil(Math.sqrt(n_groups));
        console.log(n_groups)
        const grouped_values = this.groupValues(data_list, 2);
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
            const values = this.filterByRange(i);
            this.table_values(values);
        }


    }

    /**
     * Se encarga de tabular los valores
     * @param list
     */
    table_values(list) {
     const row = list[0][1];
     const columns = list[1][1];






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
            data_list.filter(data => {
                if ( data >= rangeElement[0] && data < rangeElement[1]  ) {
                    quantity.push([data , [rangeElement[0], rangeElement[1]]]);
                }
            });
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