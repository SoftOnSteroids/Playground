"""
Calular una fecha deseada a partir de una fecha ingresada y 
la cantidad de días a sumar o restar.
"""
from datetime import datetime, timedelta

start_date_input = input("Ingrese una fecha (aaaa-mm-dd): ").strip()
days = int(input("Ingrese la cantidad de días a sumar (usar signo - para restar ;-) : ").strip())

start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
expiration_date = start_date + timedelta(days=days)

print(f"Para la fecha dada {start_date.date()} + {days} días, la fecha resultante es: {expiration_date.date()}")