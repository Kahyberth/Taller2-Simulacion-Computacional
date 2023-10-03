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

        const values = [];
        for (const i of grouped_values) {
            values.push(this.filterByRange(i));

        }
        this.table_values(values);


    }

    /**
     * Se encarga de tabular los valores
     * @param list
     */
    table_values(list) {

       const coordinates = [];

        for (let i = 0; i < list.length; i++) {
            const row = list[i][0][1];
            const columns = list[i][1][1];

            coordinates.push([row,columns]);

        }


       this.tabulateCoordinates(coordinates);

    }

    tabulateCoordinates(coordinates) {
        const patternCount = {};

        for (const pattern of coordinates) {
            const patternString = JSON.stringify(pattern);

            if (patternCount[patternString]) {
                patternCount[patternString]++;
            } else {
                patternCount[patternString] = 1;
            }
        }

        const rows = new Set(coordinates.map(pattern => JSON.stringify(pattern[0])));
        const cols = new Set(coordinates.map(pattern => JSON.stringify(pattern[1])));

        const table = new Table({
            head: [''].concat(Array.from(cols).map(col => JSON.parse(col).join(','))), // Encabezado de columnas
        });

        for (const row of Array.from(rows)) {
            const rowData = [JSON.parse(row).join(',')];
            for (const col of Array.from(cols)) {
                const patternCountKey = JSON.stringify([JSON.parse(row), JSON.parse(col)]);
                rowData.push(patternCount[patternCountKey] || 0);
            }
            table.push(rowData);
        }

        console.log('Tabla de patrones y sus conteos:');
        console.log(table.toString());
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