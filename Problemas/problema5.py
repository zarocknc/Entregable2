from InquirerPy import inquirer


def Getnum(msg: str) -> float:
    return float(
        inquirer.number(message=msg, float_allowed=True, replace_mode=True).execute()
    )


numeros = [
    Getnum("ingrese el primer numero"),
    Getnum("ingrese el segundo numero"),
    Getnum("ingrese el tercer numero"),
]
numeroMayor = sorted(numeros)[2]

print("el mayor numero es:", numeroMayor)


##########################
### simplemente el algoritmo
### Lee 3 numero y retorna el numero mayor
### (en el caso la primera opcion no satisfaga el significado de "algoritmo")
def maxNum(n1, n2, n3):
    return sorted([n1, n2, n3])[2]


##########################
