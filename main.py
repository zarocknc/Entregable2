from InquirerPy import inquirer

alternativas = [
    "Problema 1",
    "Problema 2",
    "Problema 3",
    "Problema 4",
    "Problema 5",
    "Problema 6",
    "Problema 7",
    "Problema 8",
    "Problema 9",
    "Problema 10",
]

eleccion = inquirer.select(
    message="Elija que problema desea abrir:", choices=alternativas, vi_mode=True
).execute()

action = {
    "Problema 1": "Problemas/problema1.py",
    "Problema 2": "Problemas/problema2.py",
    "Problema 3": "Problemas/problema3.py",
    "Problema 4": "Problemas/problema4.py",
    "Problema 5": "Problemas/problema5.py",
    "Problema 6": "Problemas/problema6.py",
    "Problema 7": "Problemas/problema7.py",
    "Problema 8": "Problemas/problema8.py",
    "Problema 9": "Problemas/problema9.py",
    "Problema 10": "Problemas/problema10.py",
}
exec(open(action[eleccion]).read())
