import sys

from InquirerPy import inquirer
from rich.console import Console
from rich.table import Table
from rich.text import Text

## OK ESTO SERA DIFICIL
console = Console()  # Herramienta de rich para imprimir las tablas | terminal agnostic


def Getnum(msg: str) -> float:
    return float(
        inquirer.number(message=msg, float_allowed=True, replace_mode=True).execute()
    )


def GetInt(msg: str) -> int:
    return int(inquirer.number(message=msg).execute())


tablaPrecios = Table(title="Precios")
tablaPrecios.add_column("Genero")
tablaPrecios.add_column("Precio")
tablaPrecios.add_row("Salsa", "S/ 56")
tablaPrecios.add_row("Rock", "S/ 63")
tablaPrecios.add_row("Pop", "S/ 87")
tablaPrecios.add_row("Folclore", "S/ 120,5")

### TAbla de resumen de la operacion
tablaResumen = Table(title="Resumen")
tablaResumen.add_column("Genero")
tablaResumen.add_column("Cantidad")
tablaResumen.add_column("Precio")
tablaResumen.add_column("Descuento")
tablaResumen.add_column("Importe a pagar")


def comprar():
    console.print(tablaPrecios)
    cesta = inquirer.checkbox(
        message="Elija que DVDs desea comprar (seleccione con espacio | Enter para confirmar)",
        choices=["Salsa", "Rock", "Pop", "Folclore"],
        vi_mode=True,  # siempre activen el modo vim <3
    ).execute()

    if cesta == []:
        sys.exit("Cesta Vacia Nada que hacer")

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
    # print("Cantidad de cesta", cestaFinal)
    # print("Precios ", precios)
    # print("Cesta Precios", cestaPrecios)
    cestaDescuentos = dict()  # dict vacio
    cestaPrecioFinal = dict()
    for key, value in cestaFinal.items():
        cestaDescuentos[key] = round(
            cestaPrecios.get(key) * descuentos(value) / 100, 2
        )  # cestaPrecios.get(key) retorna un None al declaralo como un dict vacio
        cestaPrecioFinal[key] = round(
            cestaPrecios.get(key) - cestaDescuentos.get(key), 2
        )

        # Pero si retorna floats y por ende si funciona
    # print("cesta descuentos:", cestaDescuentos)
    # print("este es el precio con el descuento")
    # print(cestaPrecioFinal)

    precioTotal = 0
    for value in cestaPrecioFinal.values():
        precioTotal += value

    print("el precio final es:", precioTotal)
    #### Calculando regalos
    ## Cesta final (la cantidad comprada)
    regalo = False

    if cestaFinal.get("Pop") != None and cestaFinal.get("Pop") > 6:
        regalo = True
    elif cestaFinal.get("Rock") != None and cestaFinal.get("Rock") > 6:
        regalo = True
    # print("Te regalamos un poster es", regalo)
    ### Imprimimos los datos como corresponde
    for key, value in cestaFinal.items():
        tablaResumen.add_row(
            str(key),
            str(cestaFinal.get(key)),
            "S/" + str(cestaPrecios.get(key)),
            "S/" + str(cestaDescuentos.get(key)),
            "S/" + str(cestaPrecioFinal.get(key)),
        )
    console.print(tablaResumen)

    textoPrecioTotal = Text("El precio total es: " + "S/" + str(precioTotal))
    textoPrecioTotal.stylize("bold magenta", 20)
    console.print(textoPrecioTotal)

    if regalo:
        textoRegalo = Text("Felicidades Ganaste un Poster!!")
        textoRegalo.stylize("bold red", 23, 29)
        console.print(textoRegalo)


comprar()
## YA creo que todo esta completo | eso espero
