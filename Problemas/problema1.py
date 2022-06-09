from InquirerPy import \
    inquirer  # Like input() pero mas bonito (also can handle some input errors)


# msg debe ser un string y retorna un float
def Getnum(msg: str) -> float:
    return float(inquirer.number(message=msg).execute())


sum = 0
for x in range(1, 5):
    sum += Getnum(f"Ingrese el {x} numero")
print("El promedio de los 4 numeros es", sum / 4)
