from InquirerPy import \
    inquirer  # Like input() pero mas bonito (also can handle some input errors)
from rich.console import Console
from rich.table import Table  # Imprimir tablas


# msg debe ser un string y retorna un float
def Getnum(msg: str) -> float:
    return float(
        inquirer.number(message=msg, float_allowed=True, replace_mode=True).execute()
    )


inversor1: float = Getnum("Ingrese el aporte del inversor 1")
inversor2: float = Getnum("Ingrese el aporte del inversor 2")
inversor3: float = Getnum("Ingrese el aporte del inversor 3")
totalInvest: float = inversor1 + inversor2 + inversor3

# No creo objetos porque nunca me enseñaron oop :P
inversor1Percent = round(inversor1 / totalInvest * 100, 2)
inversor2Percent = round(inversor2 / totalInvest * 100, 2)
inversor3Percent = round(inversor3 / totalInvest * 100, 2)

# CREAMOS UNA TABLA | Deberia usar pandas unu
console = Console()
tabla = Table(show_header=True)
tabla.add_column("Inversor")
tabla.add_column("Cantidad")
tabla.add_column("Porcentaje (%)")
tabla.add_row("Inversor 1", str(inversor1), str(inversor1Percent))
tabla.add_row("Inversor 2", str(inversor2), str(inversor2Percent))
tabla.add_row("Inversor 3", str(inversor3), str(inversor3Percent))

console.print(tabla)
