from InquirerPy import inquirer


def Getnum(msg: str) -> float:
    return float(
        inquirer.number(message=msg, float_allowed=True, replace_mode=True).execute()
    )


def areaTriangulo(base, altura) -> float:
    return base * altura / 2  # super easy


## Un problema

base = Getnum("ingrese la base:")
altura = Getnum("ingrese la altura(h):")
print("el area del triangulo es:", areaTriangulo(base, altura))
