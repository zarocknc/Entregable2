from InquirerPy import inquirer


def Getnum(msg: str) -> float:
    return float(
        inquirer.number(message=msg, float_allowed=True, replace_mode=True).execute()
    )


num1 = Getnum("ingrese el primer numero")
num2 = Getnum("ingrese el segundo numero")


def Preguntar():
    respuesta = inquirer.select(
        message="Seleccione alguna operacion aritmetica",
        choices=["Sumar", "Restar", "Multiplicar", "Dividir"],
        vi_mode=True,  # Siempre usen vi_mode <3
    ).execute()
    print(respuesta)
    operators = {
        "Sumar": lambda n1, n2: n1 + n2,
        "Restar": lambda n1, n2: n1 - n2,
        "Multiplicar": lambda n1, n2: n1 * n2,
        "Dividir": lambda n1, n2: n1 / n2,
    }
    resultado = operators[respuesta](num1, num2)
    print("El resultado de", respuesta, "es:", resultado)


Preguntar()
