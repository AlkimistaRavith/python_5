



def factorial(n):
    fact_res = 1
    for i in range(2, n + 1):
        fact_res *= i
    return fact_res

def productoria(lista):
    prod_res = 1
    for numero in lista:
        prod_res *= numero
    return prod_res

def calcular(**kwargs):
    for clave, valor in kwargs.items():
        if clave.startswith('fact_'):
            if isinstance(valor, int): 
                print(f"El factorial de {valor} = {factorial(valor)}")
            else:
                print(f"Valor no válido para el factorial {clave}. Debe ser un número entero (n).")
        elif clave.startswith('prod_'):
            if isinstance(valor, list):
                print(f"La productoria de {valor} = {productoria(valor)}")
            else:
                print(f"Valor no válido para la productoria {clave}. Debe ser una lista de números entero ([n1,n2,n3,...,etc.]).")
        else:
            print(f"El argumento {clave}, no cumple con el formato. Por favor utiliza fact_i o prod_i para calcular un factorial o una productoria, respectivamente.")

calcular(fact_1=[1,2,3], prod_1=[3,6,4,2,8], fact_2=6)clear
