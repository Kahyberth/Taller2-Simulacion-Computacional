import  Table  from "cli-table3";

export class Poker {
  constructor(list) {
    this.list = list;
  }

  poker_3() {
    const data_list = this.list
    var n = data_list.length;

    var counts = {
      "TD": 0,
      "1P": 0,
      "T": 0
    };

    for (var i = 0; i < n; i++) {
      var number = data_list[i];
      var cadena = number.toString()
      var cadena2 = cadena.slice(2, 5)
      //console.log(cadena)
      //console.log(cadena2)

      
      var unique_digits = new Set(cadena2);
      //console.log(unique_digits)

      

      if (unique_digits.size === 3) {
        counts["TD"] += 1;
      } else if (unique_digits.size === 2) {
        counts["1P"] += 1;
      } else if (unique_digits.size === 1) {
        counts["T"] += 1;
      }
      //console.log(number, unique_digits, decimal_digits, counts);
    }

    // Asegurémonos de que la suma de todas las categorías sea igual al total de números
    console.log("-----------------------------------------------------------------");
    console.log(Object.values(counts).reduce((a, b) => a + b, 0));
    console.log(n);
    console.log("-----------------------------------------------------------------");
    console.log(counts);

    var FE = { "TD": 0.72 * n, "1P": 0.27 * n, "T": 0.01 * n };
    console.log(FE);

    var chi_square = 0;
    for (var category in FE) {
      chi_square += Math.pow((FE[category] - counts[category]), 2) / FE[category];
      console.log(chi_square);
    }

    var critical_value = 5.991; // Valor crítico para un nivel de significancia del 0.05 (para 2 grados de libertad)

    if (chi_square <= critical_value) {
      console.log("La secuencia es independiente (PÓKER DE 3)");
      console.log(`${chi_square} <= ${critical_value}`);
    } else {
      console.log("La secuencia no es independiente (PÓKER DE 3)");
      console.log(`${chi_square} > ${critical_value}`);
    }
  }


  poker_5() {
    const data_list = this.list
    var n = data_list.length;

    var counts = {
      "TD": 0,
      "1P": 0,
      "2P": 0,
      "T": 0,
      "TP": 0,
      "P": 0,
      "Q": 0
    };

    for (var i = 0; i < n; i++) {
      var number = data_list[i];
      var cadena = number.toString()
      var decimal_digits = cadena.slice(2, 7)
      //console.log(cadena)
      //console.log(decimal_digits)
      
      var unique_digits = new Set(decimal_digits);
      //console.log(unique_digits)
    
      if (unique_digits.size === 5) {
        counts["TD"] += 1;
      } else if (unique_digits.size === 4) {
        counts["1P"] += 1;
      } else if (unique_digits.size === 3) {
        for (var digit of unique_digits) {
          if (decimal_digits.toString().split('').filter(d => d === digit.toString()).length === 3) {
            counts["T"] += 1;
            break;
          } else if (decimal_digits.toString().split('').filter(d => d === digit.toString()).length === 2) {
            counts["2P"] += 1;
            break;
          }
        }
      } else if (unique_digits.size === 2) {
        for (var digit of unique_digits) {
          if (decimal_digits.toString().split('').filter(d => d === digit.toString()).length === 4) {
            counts["P"] += 1;
            break;
          } else if (decimal_digits.toString().split('').filter(d => d === digit.toString()).length === 3 || decimal_digits.toString().split('').filter(d => d === digit.toString()).length === 2) {
            counts["TP"] += 1;
            break;
          }
        }
      } else if (unique_digits.size === 1) {
        counts["Q"] += 1;
      }
    }

    // Asegurémonos de que la suma de todas las categorías sea igual al total de números
    console.log("-----------------------------------------------------------------");
    console.log(Object.values(counts).reduce((a, b) => a + b, 0));
    console.log(n);
    console.log("-----------------------------------------------------------------");
    console.log(counts);

    var FE = {
      "TD": 0.3024 * n,
      "1P": 0.5040 * n,
      "2P": 0.1080 * n,
      "TP": 0.0090 * n,
      "P": 0.0045 * n,
      "Q": 0.0001 * n
    };

    var chi_square = 0;
    for (var category in FE) {
      chi_square += Math.pow((FE[category] - counts[category]), 2) / FE[category];
    }

    var critical_value = 12.592; // Valor crítico para un nivel de significancia del 0.05 (para 2 grados de libertad)

    if (chi_square <= critical_value) {
      console.log("La secuencia es independiente (PÓKER DE 3)");
      console.log(`${chi_square} <= ${critical_value}`);
    } else {
      console.log("La secuencia no es independiente (PÓKER DE 3)");
      console.log(`${chi_square} > ${critical_value}`);
    }
  }


}