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

    print("AQUI")
    cestaPrecios = {}
    for key, value in cestaFinal.items():
        # print(precios.get(key))  # .get return el valor del item con el key especificado
        cestaPrecios[key] = value * precios.get(key)
    print(cestaFinal)

    print("HERE")
    # for key, value in cestaFinal.items():
    # precioDeCesta[key] = value - (value * descuentos(value) / 100)
    # counterHelperDeCantidadDeDiscos = 0
    # for value in cestaFinal():
    # counterHelperDeCantidadDeDiscos += value


comprar()
