print()
print("Ejercicio 1 - Diccionarios\n")

hotel_data = {
    "name": "Hotel Solana",
    "star_rating": 4,
    "rooms": [
        {"room_number": 101, "type": "single", "price": 100, "floor": 1},
        {"room_number": 102, "type": "double", "price": 150, "floor": 2},
        {"room_number": 103, "type": "suite", "price": 300, "floor": 3}
    ],
}
print("Nombre del hotel:", hotel_data["name"])
print("Calificación del hotel:", hotel_data["star_rating"])
print("Número de habitaciones:", len(hotel_data["rooms"]))
print("\nDetalles de las habitaciones:")
for room in hotel_data["rooms"]:
    print("\nNúmero de habitación:", room["room_number"])
    print("Tipo de habitación:", room["type"])
    print("Precio por noche:", room["price"])
    print("Ubicada en el piso:", room["floor"])
    print()