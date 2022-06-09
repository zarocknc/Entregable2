from InquirerPy import \
    inquirer  # Like input() pero mas bonito (also can handle some input errors)
from rich.console import Console
from rich.table import Table  # Imprimir tablas


# msg debe ser un string y retorna un float
def Getnum(msg: str) -> float:
    return float(
        inquirer.number(message=msg, float_allowed=True, replace_mode=True).execute()
    )


def GetInt(msg: str) -> int:
    return int(inquirer.number(message=msg).execute())


def GetText(msg: str) -> str:
    return inquirer.text(message=msg, validate=lambda result: len(result) > 0).execute()


class Empleado:
    def __init__(self):
        self.horasDeTrabajo: int = GetInt("Cuantas horas trabaja:")
        self.nombre: str = GetText("Introdusca su nombre")
        self.salarioPorHora: float = Getnum("Introdusca el salario por hora")
        self.salarioDiario = round(self.salarioPorHora * self.horasDeTrabajo, 2)
        self.salarioSemanal = self.salarioDiario * 6  # Suponemos que trabaja 6 dias :c
        self.salarioMensual = self.salarioSemanal * 4
        self.salarioAnual = self.salarioMensual * 12
        self.salarioPorHoraAum = round(
            (self.salarioPorHora * 15 / 100) + self.salarioPorHora, 2
        )
        self.salarioDiarioAum = round(self.salarioPorHoraAum * self.horasDeTrabajo, 2)
        self.salarioSemanalAum = round(self.salarioDiarioAum * 6, 2)
        self.salarioMensualAum = self.salarioSemanalAum * 4
        self.salarioAnualAum = self.salarioMensualAum * 12


esclavo1 = Empleado()
## AHORA CREAMOS UNA TABLA
console = Console()
tabla = Table(show_header=True, title="Salario")
tabla.add_column("Datos")
tabla.add_column("Index 1")
tabla.add_column("Index 1 Aumento de sueldo +15%")
tabla.add_row("Nombre", str(esclavo1.nombre), str(esclavo1.nombre))
tabla.add_row(
    "Horas de trabajo", str(esclavo1.horasDeTrabajo), str(esclavo1.horasDeTrabajo)
)
tabla.add_row(
    "Salario por hora", str(esclavo1.salarioPorHora), str(esclavo1.salarioPorHoraAum)
)
tabla.add_row(
    "Salario Diario", str(esclavo1.salarioDiario), str(esclavo1.salarioDiarioAum)
)
tabla.add_row(
    "Salario Semanal", str(esclavo1.salarioSemanal), str(esclavo1.salarioSemanalAum)
)
tabla.add_row(
    "Salario Mensual", str(esclavo1.salarioMensual), str(esclavo1.salarioMensualAum)
)
tabla.add_row(
    "Salario Anual", str(esclavo1.salarioAnual), str(esclavo1.salarioAnualAum)
)
console.print(tabla)
