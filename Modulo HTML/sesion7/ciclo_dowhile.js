
let opcion;

do {
    console.log("1. Sumar");
    console.log("2. Restar");
    console.log("3. Multiplicar");
    console.log("4. Dividir");
    console.log("5. Salir");
    opcion = parseInt(prompt("Ingrese una opcion: "));

    if (opcion >= 1 && opcion <= 4) {
        let num1 = parseInt(prompt("Ingrese el primer numero: "));
        let num2 = parseInt(prompt("Ingrese el segundo numero: "));

        switch (opcion) {
            case 1:
                console.log(`Resultado: ${num1 + num2}`);
                break;
            case 2:
                console.log(`Resultado: ${num1 - num2}`);
                break;
            case 3:
                console.log(`Resultado: ${num1 * num2}`);
                break;
            case 4:
                console.log(`Resultado: ${num1 / num2}`);
                break;

        }

    }else if(opcion !== 5){
        console.log("Opcion invalida");
    }
} while (opcion != 5);
