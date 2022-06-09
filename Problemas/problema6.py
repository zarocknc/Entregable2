from InquirerPy import inquirer


def Getnum(msg: str) -> float:
    return float(
        inquirer.number(message=msg, float_allowed=True, replace_mode=True).execute()
    )


def isPar(number) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


numero1 = Getnum("ingrese un numero:")

if isPar(numero1):
    print("el numero es par")
else:
    print("el numero es impar")
