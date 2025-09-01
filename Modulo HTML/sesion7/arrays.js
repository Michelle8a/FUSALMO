
let nombres = ["Juan", "María", "Carlos"];
console.log(nombres[0]); // Accede al primer nombre (Juan)
console.log(nombres.length); // Muestra la longitud del array (3)
nombres.push("Ana"); // Agrega un nuevo nombre al final del array
console.log(nombres); // Muestra los nombres actualizados


//Crear un arreglo


//Notacion literal
let numeros = [1, 2, 3, 4, 5];
let nombres2 = ["Juan", "Maria", "Carlos"];
let mezcla = [1, "hola", true];


//Constructor Array
let numeros2 = new Array(1, 2, 3, 4, 5);
let nombres3 = new Array("Juan", "Maria", "Carlos");
let mezcla2 = new Array(1, "hola", true);


//Array Vacio
let vacio = [];
vacio.push("elemento 1");
vacio.push("elemento 2");
vacio.push("elemento 3");
console.log(vacio);


//Inicializar con longitud
let arrayVacio = new Array(3); //Crea un array con 3 espacios vacios
arrayVacio[0] = "elemento 1";
arrayVacio[1] = "elemento 2";
arrayVacio[2] = "elemento 3";
console.log(arrayVacio);


//Metodos de un array

let numeros3 = [1, 2, 3, 4, 5];
numeros3.push(6); // Agrega un elemento al final del array
numeros3.pop(); // Elimina el ultimo elemento del array
numeros3.unshift(0); // Agrega un elemento al inicio del array
numeros3.shift(); // Elimina el primer elemento del array
numeros3.splice(2, 1); // Elimina el elemento en la posicion 2
numeros3.slice(1, 3); // Devuelve un nuevo array con los elementos desde la posicion 1 hasta la 3
numeros3.reverse(); // Invierte el orden de los elementos del array
numeros3.sort(); // Ordena los elementos del array
numeros3.concat([6, 7, 8]); // Concatena dos arrays
numeros3.join(","); // Convierte el array en una cadena de texto
numeros3.indexOf(3); // Devuelve la posicion del elemento en el array
numeros3.includes(3); // Devuelve true si el elemento esta en el array
numeros3.every((elemento) => elemento > 0); // Devuelve true si todos los elementos del array cumplen la condicion
numeros3.some((elemento) => elemento > 0); // Devuelve true si al menos un elemento del array cumple la condicion
numeros3.filter((elemento) => elemento > 0); // Devuelve un nuevo array con los elementos que cumplen la condicion



