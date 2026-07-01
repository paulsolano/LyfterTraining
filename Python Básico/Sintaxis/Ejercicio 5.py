# Ejercicio 5 - Notas de estudiante
# Dada n cantidad de notas de un estudiante, calcular:
#   1. Cuantas notas tiene aprobadas (mayor a 70)
#   2. Cuantas notas tiene desaprobadas (menor a 70)
#   3. El promedio de todas
#   4. El promedio de las aprobadas
#   5. El promedio de las desaprobadas

notes = []
while True:
    try:
        note = input("Ingrese una nota (o 'fin' para terminar): ")
        if note == "fin":
            break
        note = float(note)
        if note < 0 or note > 100:
            print("Nota fuera de rango. Ignorando esa nota.")
            continue
        else:
            notes.append(note)
    except ValueError:
        print("Eso no es una nota válida. Intenta de nuevo.")

if not notes:
    print("No se ingresaron notas.")
else:
    approved = []
    failed = []
    for note in notes:
        if note >= 70:
            approved.append(note)
        else:
            failed.append(note)

        #    for note in notes if note >= 70: another way to do it with list comprehension
        #        approved.append(note)
        #    for note in notes if note <= 70:
        #        failed.append(note)

        #approved = [note for note in notes if note >= 70] and another way
        #failed = [note for note in notes if note < 70]

    if not approved:
        print("No hay notas aprobadas.")
    if not failed:
        print("No hay notas desaprobadas.")


    print(f"Cantidad de notas aprobadas: {len(approved)}")
    print(f"Cantidad de notas desaprobadas: {len(failed)}")
    print(f"Promedio de todas las notas: {sum(notes)/len(notes):.2f}")
    print(f"Promedio de las notas aprobadas: {sum(approved)/len(approved) if approved else 0:.2f}")
    print(f"Promedio de las notas desaprobadas: {sum(failed)/len(failed) if failed else 0:.2f}")
    print(f"Cantidad de notas ingresadas: {len(notes)}")