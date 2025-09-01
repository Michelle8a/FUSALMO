// Primero asegúrate de instalar prompt-sync:
// npm install prompt-sync

const prompt = require("prompt-sync")();

const numero = parseInt(prompt("Ingrese un número: "));

if (isNaN(numero)) {
    console.log("Por favor ingrese un número válido.");
} else if (numero % 2 === 0) {
    console.log(`${numero} es par`);
} else {
    console.log(`${numero} es impar`);
}
