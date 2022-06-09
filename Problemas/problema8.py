from InquirerPy import inquirer


def Getnum(msg: str) -> float:
    return float(
        inquirer.number(message=msg, float_allowed=True, replace_mode=True).execute()
    )


def DniEsValido(dni) -> bool:
    if len(dni) == 8:
        return True
    else:
        return False


# Un problema:

Usuario = Getnum("Ingrese su DNI")
if DniEsValido(Usuario):
    print("el DNI es valido")
else:
    print("es DNI no es valido")
