from datetime import datetime

fecha_hora_actual = datetime.now()
print("Fecha y hora actual:", fecha_hora_actual)
print("Solo la fecha:", fecha_hora_actual.strftime("%d-%m-%Y"))
print("Solo la hora:", fecha_hora_actual.strftime("%H:%M:%S"))
print("Fecha legible:", fecha_hora_actual.strftime("%d de %B de %Y"))