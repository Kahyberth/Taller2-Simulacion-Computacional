export class LinealCongruente {
    constructor(x0, a,c,m,n = 100) {
        this.x0 = x0;
        this.a = a;
        this.c = c;
        this.m = m;
        this.n = n;
    }

    linealCongruente() {
        let x = this.x0;
        let a = this.a;
        let c = this.c;
        let m = this.m;
        const n = this.n;
        let array = [];
        for (let i = 0; i < n; i++) {
            x = (a * x + c) % m;
            array.push(x / m);
        }
        return array;
    }

    //Periodo del generador
    periodo () {
        let x = this.x0;
        let a = this.a;
        let c = this.c;
        let m = this.m;
        let array = [];
        const n = this.n;
        for (let i = 0; i < n; i++) {
            x = (a * x + c) % m;
            array.push(x / m);
            if (x === this.x0) {
                break;
            }
        }
        return array.length;
    }


}