
function calcularRenta() {
    var salario = parseFloat(document.getElementById("salario").value);

    var seguro = salario * 0.0725; //7.25% de seguro
    var isss = salario * 0.03; //3% de isss

    var renta;

    if (salario <= 472.00) {
        renta = 0;
    }
    else if (salario <= 895.24) {
        renta = (salario - 472.00) * 0.10 + 17.67;
    }
    else if (salario <= 2038.10) {
        renta = (salario - 895.24) * 0.20 + 60.00;
    }
    else {
        renta = (salario - 2038.10) * 0.30 + 288.57;
    }

    document.getElementById("seguro").textContent = seguro.toFixed(2);
    document.getElementById("isss").textContent = isss.toFixed(2);
    document.getElementById("renta").textContent = renta.toFixed(2);


}

//---
function caclcularEdad() {

var añoActual = new Date().getFullYear();

var añoNacimiento = parseInt(document.getElementById("actual").value);

var edad = añoActual - añoNacimiento;

if (edad >= 18) {
    document.getElementById("edad").textContent = "Eres mayor de edad";
} else {
    document.getElementById("edad").textContent = "Eres menor de edad";
}
}


