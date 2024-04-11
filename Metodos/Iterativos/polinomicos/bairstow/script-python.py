import  sympy as sp
import numpy as np

from pyscript import document
from pyscript.js_modules import utilidades as utl

print("Bairtow")
print("model-loaded")
print("hola desde python")
utl.CargaComletada()

def obtener_Datos(event):
    # Definir símbolos
    x = sp.symbols('x')
    print("Obteniendo Datos")
    # Ecuación a dividir (dividendo)
    f_x_crudo = document.getElementById("funcion").value
    r0_crudo = document.getElementById("R0").value
    s0_crudo = document.getElementById("S0").value
    tolerancia_crudo = document.getElementById("tolerancia").value
    f_x = sp.sympify(f_x_crudo)
    r0 = float(r0_crudo)
    s0 = float(s0_crudo)
    error_aceptado = float(tolerancia_crudo)
    calcular_bairstow(f_x, r0, s0, error_aceptado)


def calcular_bairstow(f_x, r0, s0, error_aceptado):
    utl.resetarTexto()
    utl.mostrarLoader()
    x = sp.symbols('x')
    x_aproximada = []
    iteracion = 0
    tabla_final = []

    tabla_final.append(["Iteracion", "r0", "s0", "Error r", "Error s"])

    while True:
        iteracion += 1
        #obtenemos coeficientes para b
        polinomio = f_x.as_poly(x)
        grado = polinomio.degree()
        coeficientes = [polinomio.coeff_monomial(x**i) for i in range(grado, -1, -1)]

        # asiganamos coeficientes de b
        b4 = coeficientes[0]
        b3 = coeficientes[1] + r0 * b4
        b2 = coeficientes[2] + r0 * b3 + s0 * b4
        b1 = coeficientes[3] + r0 * b2 + s0 * b3
        b0 = coeficientes[4] + r0 * b1 + s0 * b2

        #obtenemos coeficientes para c
        c4 = b4
        c3 = b3 + r0 * c4
        c2 = b2 + r0 * c3 + s0 * c4
        c1 = b1 + r0 * c2 + s0 * c3


        # determinar delta r y delta s
        dr, ds = sp.symbols('r s')
        ecuacion1 = c2 * dr + c3 * ds + b1
        ecuacion2 = c1 * dr + c2 * ds + b0
        solucion = sp.solve([ecuacion1, ecuacion2], (dr, ds))

        #cambiar r y s
        r0 = r0 + solucion[dr]
        s0 = s0 + solucion[ds]

        #comprobar error
        error_r = abs(solucion[dr] / r0) * 100
        error_s = abs(solucion[ds] / s0) * 100
        print(iteracion)
        tabla_final.append([iteracion, r0, s0, error_r, error_s])
        #calcular aproximada si errores aceptados
        if error_r < error_aceptado and error_s < error_aceptado:
            r0 = r0.evalf()
            s0 = s0.evalf()
            x_aproximada.append((r0 + sp.sqrt((r0**2) + (4 * s0))) / 2)
            x_aproximada.append((r0 - sp.sqrt((r0**2) + (4 * s0))) / 2)
            #dividir polinomio
            cociente, residuo = sp.div(f_x, (x - x_aproximada[-1]) * (x - x_aproximada[-2]))
            condicion = cociente.as_poly(x).degree()
            if condicion >= 3:
                #volvemos plicar bairstow
                print("Volver a aplicar bairstow")
            elif condicion == 2:
                #aplicar formula cuadratica
                coefficientes = sp.Poly(cociente).coeffs()
                a = coefficientes[0]
                b = coefficientes[1]
                c = coefficientes[2]
                x_aproximada.append((-b + sp.sqrt((b**2) - (4 * a * c))) / (2 * a))
                x_aproximada.append((-b - sp.sqrt((b**2) - (4 * a * c))) / (2 * a))
                break
            elif condicion == 1:
                #aplicar formula lineal
                x_aproximada.append((-s0 / r0))
                break
            else:
                break
                #terminar
            
        #sino volver a iterar

    utl.agregarTitulo1("Tabla de resultados")
    utl.creartabla(tabla_final)
    
    #mostrar raices
    iteracion = 0
    for raiz in x_aproximada:
        iteracion += 1
        utl.agregarTexto(f"Raiz aproximada X{iteracion}: {str(raiz)}")
    utl.mostrarTexto()
    utl.ocultarLoader()
    print("Raices aproximadas: ", x_aproximada)