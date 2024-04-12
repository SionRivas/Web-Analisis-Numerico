import  sympy as sp
import numpy as np

from pyscript import document
from pyscript.js_modules import utilidades as utl

print("Muller")
print("model-loaded")
print("hola desde python")
utl.CargaComletada()

def obtener_Datos(event):
    # Definir símbolos
    x = sp.symbols('x')
    print("Obteniendo Datos")
    # Ecuación a dividir (dividendo)
    f_x_crudo = document.getElementById("funcion").value
    x0_crudo = document.getElementById("X0").value
    x1_crudo = document.getElementById("X1").value
    x2_crudo = document.getElementById("X2").value
    tolerancia_crudo = document.getElementById("tolerancia").value
    f_x = sp.sympify(f_x_crudo)
    x0 = float(x0_crudo)
    x1 = float(x1_crudo)
    x2 = float(x2_crudo)
    error_aceptado = float(tolerancia_crudo)
    calcular_Muller(f_x, x0, x1, x2, error_aceptado)


def calcular_Muller(f_x, x0, x1,x2, error_aceptado):
    utl.resetarTexto()
    utl.mostrarLoader()
    x = sp.symbols('x')
    iteracion = 0
    tabla_final = []
    tabla_final.append(["Iteracion","X0","X1","X2","Raiz","Ea%"])

    while True:
        iteracion +=1
        #calcular evaluadas
        f_x0 = f_x.subs(x, x0)
        f_x1 = f_x.subs(x, x1)
        f_x2 = f_x.subs(x, x2)

        #calcular h0 y h1
        h0 = x1 - x0
        h1 = x2 - x1

        #calcular delta0 y delta1
        delta0 = (f_x1 - f_x0) / h0
        delta1 = (f_x2 - f_x1) / h1

        #calcular a, b, c
        a = (delta1 - delta0) / (h1 + h0)
        b = a * h1 + delta1
        c = f_x2

        #calcular D
        D = (sp.sqrt(b**2 - 4*a*c))

        if abs(b + D) > abs(b - D):
            x_calculado = x2 + ((-2*c)/(b + D)) #en la diapositiva de la ingeniera sale b**2 chapra no
        else:
            x_calculado = x2 + ((-2*c)/(b - D))# con b**2 tarda muchas iteraciones


        #Error acomulado
        error_acomulado = error_aproximado_porcentual(x2,x_calculado)
        tabla_final.append([iteracion,format(x0),format(x1),format(x2),format(x_calculado),format(error_acomulado)])
        #comparacion 
        print("Iteracion: ",iteracion)
        #ahy error cuando el metodo tiene un error muy grande rompe el codigo ya q no puede vealuar la comparacion
        if error_acomulado < error_aceptado:
            break
        #sino cambiar valores
        x0 = x1
        x1 = x2
        x2 = x_calculado

    utl.agregarTitulo1("Tabla de resultados")
    utl.creartabla(tabla_final)
    
    #mostrar raices
    utl.agregarTexto("La raíz es: "+str(x_calculado))
    utl.mostrarTexto()
    utl.ocultarLoader()
    print("Raices aproximadas: ", x_calculado)



def error_aproximado_porcentual(valor_anterior, valor_actual):
        if valor_actual == 0:
            return 0
        return abs((valor_actual - valor_anterior) / valor_actual) * 100