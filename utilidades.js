let texto = "";
let stepbyStep = document.getElementById("stepbystep");

let tex = `
<dialog id="loader">
        <div class="hamster-bg">
            <div aria-label="Orange and tan hamster running in a metal wheel" role="img" class="wheel-and-hamster">
                <div class="wheel"></div>
                <div class="hamster">
                    <div class="hamster__body">
                        <div class="hamster__head">
                            <div class="hamster__ear"></div>
                            <div class="hamster__eye"></div>
                            <div class="hamster__nose"></div>
                        </div>
                        <div class="hamster__limb hamster__limb--fr"></div>
                        <div class="hamster__limb hamster__limb--fl"></div>
                        <div class="hamster__limb hamster__limb--br"></div>
                        <div class="hamster__limb hamster__limb--bl"></div>
                        <div class="hamster__tail"></div>
                    </div>
                </div>
                <div class="spoke"></div>
            </div>
            <center>
                <span class="loadingTxt">Cargando...</span>
            </center>
        </div>
    </dialog>
    `

export function CargaComletada() {
    const loading = document.getElementById('loader')
    loading.style.display = 'none'
    
    const $calcular = document.getElementById('calcular');
    const $guardar = document.getElementById('guardar');
    const $borrar = document.getElementById('borrar');
    const $cargarModelo = document.getElementById('cargarModelo');
    
    $calcular.style.display = 'flex';
    $guardar.style.display = 'flex';
    $borrar.style.display = 'flex';
    $cargarModelo.style.display = 'none';
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
    let tabla = '<div class="tablecontainer"><table>'
    arreglo.forEach(row => {
        tabla += "<tr>"
        row.forEach(value => {
            tabla += "<td>" + value + "</td>"
        })
        tabla += "</tr>"

    })
    tabla += "</table></div>"
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

