export class Estandarminimo {
    constructor(x0, a,c,m) {
        this.x0 = x0;
        this.a = a;
        this.c = c;
        this.m = m;
    }

    estandarMinimo(){
        const q = Math.floor(this.m / this.a);
        const r = (this.m % this.a);
        let xn_1 = this.x0;
        const data_list = []
        this.m = this.a * q + r
        let module = 0;
        while (true) {
            if ( (this.a * (xn_1 % q) - r * Math.floor(xn_1 / q))  >= 0) {
                module = (this.a * (xn_1 % q) - r * Math.floor(xn_1 / q)) % this.m;
            }
            else {
                module = (this.a * (xn_1 % q) - r * Math.floor(xn_1 / q) + this.m) % this.m;
            }
            xn_1 = module;
            if (data_list.find(e => e === xn_1) > 0) {
                break;
            }
            else {
                data_list.push(xn_1);
            }
        }

        return data_list;
    }

}