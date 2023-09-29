function contarSimilitudes(arrayDeStrings) {
    const resultados = { poker3: 0, poker2: 0, poker1: 0 };

    for (const str of arrayDeStrings) {
        const ocurrencias = {};

        for (const char of str) {
            ocurrencias[char] = (ocurrencias[char] || 0) + 1;
        }

        let tieneCoincidencias = false;

        for (const key in ocurrencias) {
            const count = ocurrencias[key];

            if (count >= 3) {
                resultados.poker3 += 1;
                tieneCoincidencias = true;
            } else if (count === 2) {
                resultados.poker2 += 1;
                tieneCoincidencias = true;
            }
        }

        if (!tieneCoincidencias) {
            resultados.poker1 += 1;
        }
    }

    return resultados;
}

const arrayDeStrings = [
    '298', '845', '826', '872', '723',
    '897', '358', '179', '212', '754',
    '212', '772', '062', '824', '576',
    '281', '013', '624', '411', '780',
    '917', '452', '124', '454', '404',
    '047', '236', '222', '555', '262',
    '041', '625', '533'
];

const resultados = contarSimilitudes(arrayDeStrings);
console.log('Resultados:', resultados);
