
const numero = 5;

let factorial = 1;

let i = 1;

while (i <= numero) {
    factorial *= i;
    console.log(`Iteración ${i}: Factorial = ${factorial}`);
    i++;
}

console.log(`El factorial de ${numero} es ${factorial}`);