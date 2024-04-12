import  sympy as sp
import numpy as np

from pyscript import document
from pyscript.js_modules import utilidades as utl

print("Horner")
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
    tolerancia_crudo = document.getElementById("tolerancia").value
    f_x = sp.sympify(f_x_crudo)
    x0 = float(x0_crudo)
    error_aceptado = float(tolerancia_crudo)
    calcular_Horner(f_x, x0, error_aceptado)
    


def calcular_Horner(f_x, x0, error_aceptado):
    utl.resetarTexto()
    utl.mostrarLoader()
    x = sp.symbols('x')
    f_x = f_x
    x0 = float(x0)
    error_aceptado = float(error_aceptado)
    tabla_final = []
    f_x0 = x - x0 #- para cambiar signo
    iteracion = 0
    tabla_final.append(["Iteracion","X0","R","S","Xi","Ea%"])
    while True:
        iteracion += 1
        # 1 div sintetica
        cociente, residuo = sp.div(f_x, f_x0)
        R = residuo
        #2 divicion
        cociente2, residuo2 = sp.div(cociente, f_x0)
        S = residuo2
        x_calculado = x0 - (R/S)
        error_acomulado = error_aproximado_porcentual(x0, x_calculado)
        print(f"Iteración: {iteracion} error: {error_acomulado.evalf()} error aceptado: {error_aceptado}")
        tabla_final.append([iteracion,format(x0),format(R),format(S),format(x_calculado),format(error_acomulado)])
        if error_acomulado < error_aceptado:
            break
        f_x0 = x - x_calculado #- para que cambie el signo 
        x0 = x_calculado

    print(f"La raíz es: {x_calculado}")
    utl.agregarTitulo1("tabla final")
    utl.creartabla(tabla_final)
    utl.agregarTexto("La raíz es: "+str(x_calculado))
    utl.mostrarTexto()
    utl.ocultarLoader()


    
def error_aproximado_porcentual(valor_anterior, valor_actual):
        if valor_actual == 0:
            return 0
        return abs((valor_actual - valor_anterior) / valor_actual) * 100