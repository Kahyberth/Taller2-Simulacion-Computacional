import Table from 'cli-table';
export class Pruebas {
    constructor(lista) {
        this.lista = lista;
        this.tabulado = [];
        this.table = [];
        this.sumChi = 0;
    }

    chi_cuadrado() {
        console.log("\n");
        this.tabulado = [];
        this.table = new Table({
            head: ['Clase', 'FO', 'FE', 'Chi Cuadrado'],
            colWidths: [10, 15, 20, 20]
        });
        const datos = this.lista;
        const numero_clases = Math.sqrt(datos.length);
        const gradosLibertad = numero_clases - 1;
        for (let i = 0; i < numero_clases; i++) {
            const FO = datos.filter(dato => dato >= i / numero_clases && dato < (i + 1) / numero_clases).length;
            const FE = datos.length / numero_clases;
            const diferencia = Math.pow(FO - FE, 2);
            const chi = diferencia / FE;
            this.sumChi += chi;
            this.tabulado.push([(i + 1).toString(),FO.toString(), FE.toString(), chi.toString()]);
        }

        for (const row of this.tabulado) {
            this.table.push(row);
        }

        console.log(this.table.toString());

        if (this.sumChi <= 16.919) {
            console.log(
            `
            Los números generados son uniforme, 
            suma chi cuadrado: ${this.sumChi}
            Grados de libertad: ${gradosLibertad}
            Numero de clases: ${numero_clases}
            Cantidad de números generados: ${datos.length}
            `);
        } else {
            console.log(`Los números generados no son uniformes`);
        }

        return this.sumChi;
    }


    kolmogorov() {
        console.log("\n");
        this.tabulado = [];
        this.table = new Table({
            head: ['Clase', 'FO', 'FOA', 'POA', 'PEA', '|PEA - POA|'],
            colWidths: [10, 15, 20, 20, 20, 20]
        })
        const datos = this.lista;
        const numero_clases = Math.ceil(Math.sqrt(datos.length));
        const gradosLibertad = this.lista.length;
        const kolmogorov = [];
        let FOA = 0;
        for(let i = 0; i < numero_clases; i++) {
            const FO = datos.filter(dato => dato >= i / numero_clases && dato < (i + 1) / numero_clases).length;
            FOA = FO + FOA;
            const POA = FOA / datos.length;
            const PEA = (i + 1) / numero_clases;
            kolmogorov.push(Math.abs(PEA - POA));
            this.tabulado.push([(i + 1),FO, FOA,POA, PEA, Math.abs(PEA - POA)]);
        }

        const dm_calc = kolmogorov.reduce((a, b) => Math.max(a, b));
        
        for (const row of this.tabulado) {
            this.table.push(row);
        }

        console.log(this.table.toString());

        const dm_critic = 1.36 / Math.sqrt(datos.length);

        if ( dm_calc <= dm_critic ) {
            console.log(
            `
            Los números generados son uniforme, 
            Dm calculado: ${dm_calc}
            Dm crítico: ${dm_critic}
            Grados de libertad: ${gradosLibertad}
            Numero de clases: ${numero_clases}
            Cantidad de números generados: ${datos.length}
            `);
        }


        return dm_calc;

    }
}