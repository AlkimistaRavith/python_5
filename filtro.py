precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtro(precios:dict[str,int], umbral:int , corte:str = "mayor"):
    if corte == "mayor":
        mayor_a = [] 
        for k , v in precios.items():
            if v > umbral:
                mayor_a.append(k)
        print(mayor_a)
    elif corte == "menor":
        menor_a = [] 
        for k , v in precios.items():
            if v < umbral:
                menor_a.append(k)
        print(menor_a)
    else:
        print("esto no es valido")

    return()

filtro(precios, 200000, "menor")
