import  sympy as sp
import numpy as np

from pyscript import document
from pyscript.js_modules import utilidades as utl

print("Biseccion")
print("model-loaded")
print("hola desde python")
utl.CargaComletada()

x = sp.symbols("x")

def calcular_es(cifras):
    return 0.5 * 10 ** (2 - cifras)

def obtener_Datos(event):
    print("Obteniendo Datos")
    f_x_crudo = (document.getElementById("funcion")).value
    f_x = sp.sympify(f_x_crudo)
    x1_crudo = (document.getElementById("a")).value
    x1 = float(x1_crudo)
    xu_crudo = (document.getElementById("b")).value
    xu = float(xu_crudo)
    toleracia_crudo = (document.getElementById("tolerancia")).value
    tolerancia = float(toleracia_crudo)
    print("f_x: " + f_x_crudo)
    print("x1: " + x1_crudo)
    print("xu: " + xu_crudo)
    print("tolerancia: " + toleracia_crudo)
    calcular_biseccion(f_x,x1,xu,tolerancia)


def calcular_biseccion(f_x,x1,xu,es):
    utl.resetarTexto()
    tabla_final = []

    """
    x1 = 0.1
    xu = 0.5
    """

    #f_x = sp.E**(-x) - x
    utl.agregarTexto("Metodo de la Biseccion")
    utl.agregarTexto(("Funcion a evaluar: " + str(f_x)))
    utl.agregarTexto("Paso #1---------")



    valinit1 = float(f_x.subs(x,x1))
    valinit2 = float(f_x.subs(x,xu))

    utl.agregarTexto("el valor de x1 es: " + str(x1))
    utl.agregarTexto("el valor de xu es: " + str(xu))

    utl.agregarTexto("la Funcion evalueda en X1: " + str(valinit1))
    utl.agregarTexto("la Funcion evalueda en Xu: " + str(valinit2))



    if (valinit1 < 0) ^ (valinit2 < 0):
        utl.agregarTexto("La funcion np Cambia de signo")


    utl.agregarTexto("Paso #2---------")

    roots = sp.solve(f_x)

    utl.agregarTexto("Raices Totales: " + str(roots))
    complexs = []
    for root in roots:
        if root.is_real == False:
            complexs.append(root)

    for complex in complexs:
        roots.remove(complex)

    utl.agregarTexto("Raices complejas: " + str(complexs))
    if len(roots) > 0:
        roots = list(map(float,roots))
        roots = sorted(roots)
        utl.agregarTexto("Raices Reales: " + str(roots))
    utl.agregarTexto("la posibles raices son: " + str(roots))



    utl.agregarTexto("Paso #3---------")


    def calcular_xr (x1,xu):
        return (x1 + xu) / 2

    xr = calcular_xr(x1,xu)
    utl.agregarTexto("La primera aproximacion es: " + str(xr))

    utl.agregarTexto("Proceso")


    def evaluar_f_x(xi):
        return  float(f_x.subs(x,xi))

    def format(numero):
        return "{:.6f}".format(numero)
    def calcular_ev(vr,va):
        return vr - va
    def calcular_ea(va, van):
        return abs((va - van) / va) * 100


    # Imprimir los valores de cada columna de la tabla utilizando format()

    tabla_final.append(["Iteracion","X1","Xu","Xr","f(x1)","f(xu)","f(xr)","f(x1)*f(xr)","Condicion","Ev","Ea"])

 
    iteracion = 1
    xrm1 = 0
    while True:
        xr = calcular_xr(x1,xu)

        x1_evaluada = evaluar_f_x(x1)
        xu_evaluada = evaluar_f_x(xu)
        xr_evaluada = evaluar_f_x(xr)

        fx1fxr = x1_evaluada * xr_evaluada

        #Condicion

        if fx1fxr == 0:
            condicion = "= 0"
            break
        elif fx1fxr < 0:
            condicion = "< 0"
        elif fx1fxr > 0:
            condicion = "> 0"
        
        ev = calcular_ev(roots[0],xr)

        if iteracion != 1:
            ea = format(calcular_ea(xr,xrm1))
        else:
            ea = "----"


        tabla_final.append([iteracion,format(x1),format(xu),format(xr),format(x1_evaluada),format(xu_evaluada),format(xr_evaluada),format(fx1fxr),condicion,format(ev),ea])

        if fx1fxr == 0:
            break
        elif fx1fxr < 0:
            xu = xr
        elif fx1fxr > 0:
            x1 = xr


        ea = calcular_ea(xr,xrm1)
        
        xrm1 = xr
        if ea < es :
            break
        
        iteracion += 1

        



    utl.creartabla(tabla_final)

    utl.agregarTexto("la raiz de la ecuacion es: " + str(xr))
    utl.agregarTexto("con un error de: " + str(ea) + "%")
    utl.agregarTexto("y se a conseguido con: " + str(iteracion) + " iteracion")
    utl.agregarTexto("Con un error de 3 cifras significativas")

    utl.mostrarTexto()