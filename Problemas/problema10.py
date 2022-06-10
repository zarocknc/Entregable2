import pickle
import sys

from InquirerPy import inquirer
from rich.console import Console
from rich.table import Table

# -------------------------------------------------
# FUNCIONES
# ----------------------------------------------------

console = Console()  # Utilidad de rich para ser terminal agnostic


def Getnum(msg: str) -> float:
    return float(
        inquirer.number(message=msg, float_allowed=True, replace_mode=True).execute()
    )


def GetText(msg: str) -> str:
    return inquirer.text(message=msg, validate=lambda result: len(result) > 0).execute()


def turno():
    return inquirer.select(
        message="Inquique el turno del trabajador:",
        choices=["mañana", "tarde", "noche"],
        vi_mode=True,
    ).execute()


def crearTrabajador():
    Trabajadores.append(Trabajador())


def mostrarTrabajadores():
    tabla = Table()
    tabla.add_column("Nombre")
    tabla.add_column("Turno")
    tabla.add_column("Horas")
    tabla.add_column("Salario Diario")
    tabla.add_column("SalarioNeto")
    for trabajador in Trabajadores:
        # print("--------------------")
        # print(trabajador.nombre)
        # print(trabajador.turno)
        # print(trabajador.salarioNeto)
        tabla.add_row(
            trabajador.nombre,
            str(trabajador.turno),
            str(trabajador.horas),
            str(trabajador.salarioDiario),
            str(trabajador.salarioNeto),
        )
    console.print(tabla)


def GuardarCambios():
    with open("problem10.pickle", "wb") as fp:
        pickle.dump(Trabajadores, fp)


def menu():
    eleccion = inquirer.select(
        message="Que desea realizar",
        choices=[
            "Crear trabajador",
            "Mostrar trabajadores",
            "Guardar cambios",
            "Salir",
        ],
        vi_mode=True,
    ).execute()
    options = {
        "Crear trabajador": lambda: crearTrabajador(),
        "Mostrar trabajadores": lambda: mostrarTrabajadores(),
        "Guardar cambios": lambda: GuardarCambios(),
        "Salir": lambda: sys.exit("Saliendo..."),
    }
    options[eleccion]()
    menu()


# --------------------------------------------------
# CREANDO CLASE
# ---------------


class Trabajador:
    def __init__(self) -> None:
        self.nombre = GetText("Indique su nombre")
        self.horas = Getnum("Ingrese las horas:")
        self.turno = turno()
        self.determinarSalario()
        self.determinarSalarioNeto()

    def determinarSalarioNeto(self):
        if self.turno == "noche":
            if 2000 <= self.salarioDiario <= 5000:
                self.salarioNeto = round(
                    self.salarioMensual - (self.salarioDiario * 15 / 100), 2
                )
            elif 8000 <= self.salarioDiario <= 10000:
                self.salarioNeto = round(
                    self.salarioMensual - (self.salarioDiario * 17 / 100), 2
                )
            else:
                self.salarioNeto = self.salarioMensual
        else:
            self.salarioNeto = self.salarioMensual

    def determinarSalario(self):
        if self.turno == "mañana":
            self.salarioDiario = round(self.horas * 37.0, 2)
            self.salarioMensual = round(self.salarioDiario * 30, 2)  # mes laboral
        elif self.turno == "tarde":
            self.salarioDiario = round(self.horas * 38.2, 2)
            self.salarioMensual = round(self.salarioDiario * 30, 2)  # mes laboral
        elif self.turno == "noche":
            self.salarioDiario = round(self.horas * 38.5, 2)
            self.salarioMensual = round(self.salarioDiario * 30, 2)  # mes laboral


# ------------------------------------------------------------------------------------
# INICIO DEL PROGRAMA
# -------------------

Trabajadores = []  # Creamos una lista de trabajadores vacia


# Carga a los trabajadores del archivo problem10.pickle | si no existe el archivo crea uno | pickle es un binario para guardar los datos
try:
    Trabajadores = pickle.load(open("problem10.pickle", "rb"))
except (OSError) as e:
    pickle.dump(Trabajadores, open("problem10.pickle", "wb"))

menu()
