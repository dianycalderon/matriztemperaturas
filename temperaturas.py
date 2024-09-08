import random

# Definición de la matriz 3D (ejemplo con 3 ciudades, 7 días y 4 semanas)
ciudades = 3
dias = 7
semanas = 4
temperaturas = [[[random.randint(10, 30) for _ in range(dias)] for _ in range(semanas)] for _ in range(ciudades)]

# Función para calcular el promedio de temperaturas por ciudad y semana
def calcular_promedio(ciudad, semana):
    suma = sum(temperaturas[ciudad][semana])
    promedio = suma / len(temperaturas[ciudad][semana])
    return promedio

# Impresión de los resultados
for ciudad in range(ciudades):
    for semana in range(semanas):
        promedio_actual = calcular_promedio(ciudad, semana)
        print(f"Ciudad {ciudad+1}, Semana {semana+1}: {promedio_actual:.2f}°C")