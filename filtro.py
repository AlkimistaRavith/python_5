try:
    import sys

    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }

    def filtro(precios:dict[str,int], umbral:int , corte:str = "mayor"):
        #Evaluación por defecto (mayor)
        if corte == "mayor":
            mayor_a = [] 
            for k , v in precios.items():
                if v > umbral:
                    mayor_a.append(k)
            print(mayor_a)
        #Evaluación opcional (menor)
        elif corte == "menor":
            menor_a = [] 
            for k , v in precios.items():
                if v < umbral:
                    menor_a.append(k)
            print(menor_a)
        #si el argumento de la variable corte no es "mayor" o "menor"
        else:
            print("""
Has ingresado un argumento que no es válido.
Por favor ingresa <python filtro.py [Precio de corte]> para obtener los productos con un Precio mayor al de Corte.
O, <python filtro.py [Precio de corte] menor> para obtener los productos con un Precio menor al de corte.""")

        return()
    
    #Para cuando no se indica modo de corte (mayor o menor)
    if len(sys.argv) == 2 :
        umbral = int(sys.argv[1])
        filtro(precios, umbral)
    #Cuando se agrega un argumento a la variable "corte" (menor, mayor o uno no valido)
    elif len(sys.argv) == 3 :
        umbral = int(sys.argv[1])
        corte = sys.argv[2]
        filtro(precios, umbral , corte)
    #Si no se ingresa ninguna argumento.
    elif len(sys.argv) == 1 :
        print("""
Hola, bienvenido a la evaluación de precios:
Por favor ingresa <python filtro.py [Precio de corte]> para obtener los productos con un Precio mayor al de Corte.
O, <python filtro.py [Precio de corte] menor> para obtener los productos con un Precio menor al de corte.
""")
    #Si se agregan más de 3 argumentos
    else:
        print("""
Has ingresado un argumento que no es válido.
Por favor ingresa <python filtro.py [Precio de corte]> para obtener los productos con un Precio mayor al de Corte.
O, <python filtro.py [Precio de corte] menor> para obtener los productos con un Precio menor al de corte.
""")

#Para cuando el argumento no sea numerico en variable umbral
except ValueError:
    print("""
Has ingresado un argumento que no es válido.
Por favor ingresa <python filtro.py [Precio de corte]> para obtener los productos con un Precio mayor al de Corte.
O, <python filtro.py [Precio de corte] menor> para obtener los productos con un Precio menor al de corte.""")