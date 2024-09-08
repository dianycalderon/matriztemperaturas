
# Definir la estructura de datos para almacenar temperaturas
# Ciudades -> Semanas -> Días de la semana
temperaturas = [
    [  # Ciudad 1
        [("Lunes", 72), ("Martes", 74), ("Miércoles", 75), ("Jueves", 73), ("Viernes", 70), ("Sábado", 72), ("Domingo", 71)],  # Semana 1
        [("Lunes", 74), ("Martes", 75), ("Miércoles", 76), ("Jueves", 74), ("Viernes", 72), ("Sábado", 73), ("Domingo", 70)],  # Semana 2
        [("Lunes", 70), ("Martes", 71), ("Miércoles", 69), ("Jueves", 72), ("Viernes", 73), ("Sábado", 70), ("Domingo", 68)],  # Semana 3
        [("Lunes", 72), ("Martes", 74), ("Miércoles", 76), ("Jueves", 73), ("Viernes", 72), ("Sábado", 71), ("Domingo", 70)]   # Semana 4
    ],
    [  # Ciudad 2
        [("Lunes", 60), ("Martes", 62), ("Miércoles", 63), ("Jueves", 65), ("Viernes", 64), ("Sábado", 61), ("Domingo", 60)],  # Semana 1
        [("Lunes", 63), ("Martes", 65), ("Miércoles", 64), ("Jueves", 66), ("Viernes", 68), ("Sábado", 67), ("Domingo", 65)],  # Semana 2
        [("Lunes", 61), ("Martes", 62), ("Miércoles", 64), ("Jueves", 63), ("Viernes", 65), ("Sábado", 66), ("Domingo", 64)],  # Semana 3
        [("Lunes", 62), ("Martes", 64), ("Miércoles", 66), ("Jueves", 65), ("Viernes", 63), ("Sábado", 62), ("Domingo", 61)]   # Semana 4
    ],
    [  # Ciudad 3
        [("Lunes", 85), ("Martes", 86), ("Miércoles", 88), ("Jueves", 87), ("Viernes", 85), ("Sábado", 84), ("Domingo", 83)],  # Semana 1
        [("Lunes", 87), ("Martes", 88), ("Miércoles", 89), ("Jueves", 87), ("Viernes", 86), ("Sábado", 85), ("Domingo", 84)],  # Semana 2
        [("Lunes", 86), ("Martes", 87), ("Miércoles", 88), ("Jueves", 86), ("Viernes", 85), ("Sábado", 83), ("Domingo", 82)],  # Semana 3
        [("Lunes", 84), ("Martes", 85), ("Miércoles", 86), ("Jueves", 87), ("Viernes", 85), ("Sábado", 84), ("Domingo", 83)]   # Semana 4
    ]
]

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"Promedios de temperaturas para la Ciudad {ciudad_idx + 1}:")
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = 0
        print(f"  Semana {semana_idx + 1}:")
        for dia in semana:
            dia_semana, temp = dia
            suma_temperaturas += temp
            print(f"    {dia_semana}: {temp}°F")
        promedio = suma_temperaturas / len(semana)
        print(f"  Promedio de la semana {semana_idx + 1}: {promedio:.2f}°F")
    print()
