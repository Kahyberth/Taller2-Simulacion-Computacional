import inquirer from "inquirer";
import 'colors'

export const menu = async () => {
    console.clear();
    console.log('======================'.green);
    console.log(' Select an option'.blue )
    console.log('======================'.green);

    const opt = await inquirer.prompt([
        {
            type: 'list',
            name: 'option',
            message: '¿ Que desea hacer ?',
            choices: [
                {
                    value: '1',
                    name: `${'1'.blue} Generar Números`
                },
                {
                    value: '2',
                    name: `${'2'.blue} Uniformidad`
                },
                {
                    value: '3',
                    name: `${'3'.blue} Independencia`
                },
                {
                    value: '0',
                    name: `${'4'.blue} Salir`
                },
            ]
        }
    ])

    return opt.option;
}

export const input = async ( message ) => {
    const question = [
        {
            type: 'input',
            name: 'desc',
            message,
        }
    ];
    const { desc } = await inquirer.prompt(question);
    return desc;
}


export const pause = async () => {
    const question = [
        {
            type: 'input',
            name: 'enter',
            message: `Press ${'ENTER'.green} to continue`,
        }
    ];
    console.log('\n');
    await inquirer.prompt(question);
}


export const pseudoMenu = async () => {
    console.clear();
    console.log('======================'.yellow);
    console.log(' Select an option'.yellow )
    console.log('======================'.yellow);
        const opt = await inquirer.prompt([
            {
                type: 'list',
                name: 'option',
                message: 'Select an option',
                choices: [
                    {
                        value: '1',
                        name: `${'1'.yellow} Generador Lineal Congruente`
                    },
                    {
                        value: '2',
                        name: `${'2'.yellow} Generador Estandar Minimo`
                    },
                    {
                        value: '3',
                        name: `${'3'.yellow} Generador del Lenguanje`
                    },
                ]
            }
        ])

    return opt.option;
}


export const uniformityMenu = async () => {
    console.clear();
    console.log('======================'.red);
    console.log(' Select an option'.yellow )
    console.log('======================'.red);
    const opt = await inquirer.prompt([
        {
            type: 'list',
            name: 'option',
            message: 'Select an option',
            choices: [
                {
                    value: '1',
                    name: `${'1'.red} Chi-Cuadrado`
                },
                {
                    value: '2',
                    name: `${'2'.red} Kolmogorov`
                },
            ]
        }
    ])

    return opt.option;
}

export const independenceMenu = async () => {
    console.clear();
    console.log('======================'.rainbow);
    console.log(' Select an option'.rainbow )
    console.log('======================'.rainbow);
    const opt = await inquirer.prompt([
        {
            type: 'list',
            name: 'option',
            message: 'Select an option',
            choices: [
                {
                    value: '1',
                    name: `${'1'.rainbow} Corridas`
                },
                {
                    value: '2',
                    name: `${'2'.rainbow} Series`
                },
                {
                    value: '3',
                    name: `${'3'.rainbow} Poker`
                },
            ]
        }
    ])

    return opt.option;
}


export const pokerMenu = async () => {
    console.clear();
    console.log('======================'.rainbow);
    console.log(' Select an option'.rainbow )
    console.log('======================'.rainbow);
    const opt = await inquirer.prompt([
        {
            type: 'list',
            name: 'option',
            message: 'Select an option',
            choices: [
                {
                    value: '1',
                    name: `${'1'.rainbow} Poker 3`
                },
                {
                    value: '2',
                    name: `${'2'.rainbow} Poker 5`
                },
            ]
        }
    ])

    return opt.option;
}