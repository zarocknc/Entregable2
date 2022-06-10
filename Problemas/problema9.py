import sys

from InquirerPy import inquirer

## OK ESTO SERA DIFICIL


def Getnum(msg: str) -> float:
    return float(
        inquirer.number(message=msg, float_allowed=True, replace_mode=True).execute()
    )


def GetInt(msg: str) -> int:
    return int(inquirer.number(message=msg).execute())


def comprar():
    cesta = inquirer.checkbox(
        message="Elija que DVDs desea comprar (seleccione con espacio)",
        choices=["Salsa", "Rock", "Pop", "Folclore"],
    ).execute()
    print(cesta)
    cestaFinal = {}
    for item in cesta:
        cestaFinal[item] = GetInt(f"Cuantos DVD de {item} desea comprar:")
    precios = {
        "Salsa": 56.0,
        "Rock": 63.0,
        "Pop": 87.0,
        "Folclore": 120.5,
    }

    def descuentos(cantidad: int) -> float:
        if 0 <= cantidad <= 3:
            return 0
        elif cantidad == 4:
            return 6.0
        elif 5 <= cantidad <= 10:
            return 8.0
        elif cantidad > 10:
            return 10.2
        else:
            return sys.exit("error: la cantidad es incorrecta")

    cestaPrecios = {}
    for key, value in cestaFinal.items():
        # print(precios.get(key))  # .get return el valor del item con el key especificado
        cestaPrecios[key] = value * precios.get(key)
    print("Cantidad de cesta", cestaFinal)
    print("Precios ", precios)
    print("Cesta Precios", cestaPrecios)
    cestaDescuentos = dict()  # dict vacio
    cestaPrecioFinal = dict()
    for key, value in cestaFinal.items():
        cestaDescuentos[key] = (
            cestaPrecios.get(key) * descuentos(value) / 100
        )  # cestaPrecios.get(key) retorna un None al declaralo como un dict vacio
        cestaPrecioFinal[key] = round(
            cestaPrecios.get(key) - cestaDescuentos.get(key), 2
        )

        # Pero si retorna floats y por ende si funciona
    print("cesta descuentos:", cestaDescuentos)
    print("este es el precio con el descuento")
    print(cestaPrecioFinal)

    #### Calculando regalos
    ## Cesta final (la cantidad comprada)
    regalo = False

    if cestaFinal.get("Pop") != None and cestaFinal.get("Pop") > 6:
        regalo = True
    elif cestaFinal.get("Rock") != None and cestaFinal.get("Rock") > 6:
        regalo = True
    print("Te regalamos un poster es", regalo)
    ### Imprimimos los datos como corresponde


comprar()
## YA creo que todo esta completo | eso espero
