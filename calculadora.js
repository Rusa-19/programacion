function menu() {
    console.log("Calculadora");
    console.log("Opciones");
    console.log("1. Sumar");
    console.log("2. Restar");
    console.log("3. Multiplicacion");
    console.log("4. Division");
    console.log("5. Salir");
}

function operaciones(opcion, numero1, numero2) {
    switch (opcion) {
        case "1":
            return numero1 + numero2;
        case "2":
            return numero1 - numero2;
        case "3":
            return numero1 * numero2;
        case "4":
            if (numero2 === 0) {
                return "Error: Division no permitida";
            }
            return numero1 / numero2;
        default:
            return "Opcion no valida";
    }
}

function calculadora() {
    const readline = require("readline");
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    function calcular() { // Función interna para realizar una operación
        menu();

        rl.question("Elija una opcion: ", (opcion) => {
            if (opcion === "5") {
                console.log("Vuelve pronto!");
                rl.close();
                return; // Salir del bucle y del programa
            }

            rl.question("Ingrese el primer numero: ", (input1) => {
                const numero1 = parseFloat(input1);

                rl.question("Ingrese el segundo numero: ", (input2) => {
                    const numero2 = parseFloat(input2);
                    const resultado = operaciones(opcion, numero1, numero2);
                    console.log("Resultado: " + resultado);

                    calcular();
                });
            });
        });
    }

    calcular();
}

calculadora();