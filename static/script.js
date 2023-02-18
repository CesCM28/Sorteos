const botones = document.querySelectorAll(".boleto");
const posible = document.getElementById("#posible");
const disponibles = document.getElementById("#disponibles");

botones.forEach(boton => {
    boton.addEventListener("click", () => {
        this.posible.appendChild(boton);
    })
})

function regresar() {
    botones.forEach(boton => {
        this.disponibles.appendChild(boton);
    })
}