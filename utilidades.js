let texto = "";
let stepbyStep = document.getElementById("stepbystep");


export function CargaComletada() {
    const loading = document.getElementById('loader')
    loading.style.display = 'none'
}
export function obtenerTexto() {
    return texto
}
export function resetarTexto() {
    texto = ""
}
export function agregarTexto(textoNuevo) {
    texto += "<p>" + textoNuevo + "</p>"
}
export function creartabla(arreglo) {
    let tabla = "<table>"
    arreglo.forEach(row => {
        tabla += "<tr>"
        row.forEach(value => {
            tabla += "<td>" + value + "</td>"
        })
        tabla += "</tr>"

    })
    tabla += "</table>"
    texto += tabla

}
export function añadirsalto() {
    texto += "<br>"
}
export function añadirTab() {
    texto += "\t"
}
export function mostrarTexto() {
    stepbyStep.innerHTML = texto
}

