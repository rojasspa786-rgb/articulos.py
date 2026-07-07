
# Diccionarios de datos
items = {
    "HAM001": ["Clásica BBQ", "Clásica", "Legendaria", "Parrilla"],
    "HAM002": ["Doble Queso", "Especial", "Epica", "Horno"],
    "HAM003": ["Vegetariana", "Saludable", "Comun", "Vapor"],
    "HAM004": ["Hawaiana Suprema", "Especial", "Legendaria", "Parrilla"],
    "HAM005": ["Picante Infernal", "Picante", "Epica", "Parrilla"],
    "HAM006": ["Mini Slider", "Clásica", "Rara", "Plancha"],
}

inventario = {
    "HAM001": [5000, 3],
    "HAM002": [2500, 8],
    "HAM003": [100, 50],
    "HAM004": [10000, 1],
    "HAM005": [3500, 4],
    "HAM006": [800, 0],
}

# ─────────────────────────────────────────
# Opción 1: Stock por categoría
# ─────────────────────────────────────────
def stock_categoria(categoria):
    total = 0
    for codigo, datos in items.items():
        if datos[1].lower() == categoria.lower():
            total += inventario[codigo][1]
    print(f"El stock es: {total}")


# ─────────────────────────────────────────
# Opción 2: Búsqueda por precio
# ─────────────────────────────────────────
def busqueda_precio(p_min, p_max):
    resultado = []
    for codigo, inv in inventario.items():
        precio = inv[0]
        cantidad = inv[1]
        if p_min <= precio <= p_max and cantidad > 0:
            rareza = items[codigo][2]
            resultado.append(f"{rareza}--{codigo}")
    resultado.sort()
    print(resultado)


# ─────────────────────────────────────────
# Opción 3: Actualizar precio
# ─────────────────────────────────────────
def actualizar_precio(codigo, precio):
    if codigo in inventario:
        inventario[codigo][0] = precio
        return True
    else:
        return False


# ─────────────────────────────────────────
# Opción 4: Buscar hamburguesa por código
# ─────────────────────────────────────────
def buscar_codigo(codigo):
    if codigo in items:
        datos = items[codigo]
        inv = inventario[codigo]
        print("Hamburguesa encontrada")
        print("-" * 16)
        print(f"Nombre: {datos[0]}")
        print(f"Categoría: {datos[1]}")
        print(f"Rareza: {datos[2]}")
        print(f"Tipo cocción: {datos[3]}")
        print(f"Precio: {inv[0]}")
        print(f"Stock: {inv[1]}")
    else:
        print("La hamburguesa no existe!!")


# ─────────────────────────────────────────
# Opción 5: Mostrar todas las hamburguesas
# ─────────────────────────────────────────
def mostrar_todos():
    print("\n=== CATÁLOGO DE HAMBURGUESAS ===")
    for codigo, datos in items.items():
        inv = inventario[codigo]
        print(f"\nCódigo: {codigo}")
        print(f"Nombre: {datos[0]}")
        print(f"Categoría: {datos[1]}")
        print(f"Rareza: {datos[2]}")
        print(f"Tipo cocción: {datos[3]}")
        print(f"Precio: {inv[0]}")
        print(f"Stock: {inv[1]}")


# ─────────────────────────────────────────
# Menú principal
# ─────────────────────────────────────────
def mostrar_menu():
    print("\n=== HAMBURGUESERÍA EL ARCANO ===")
    print("1. Stock por categoría.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Buscar hamburguesa por código.")
    print("5. Mostrar todas las hamburguesas.")
    print("6. Salir.")


# ─────────────────────────────────────────
# Bucle principal
# ─────────────────────────────────────────
while True:
    mostrar_menu()
    opcion = input("Ingrese opción: ")

    if opcion == "1":
        categoria = input("Ingrese categoría: ")
        stock_categoria(categoria)

    elif opcion == "2":
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("Error: Debe ingresar valores enteros!!")
        busqueda_precio(p_min, p_max)

    elif opcion == "3":
        while True:
            codigo = input("Ingrese código de la hamburguesa: ")
            try:
                precio = int(input("Ingrese nuevo precio: "))
            except ValueError:
                print("Error: Debe ingresar valores enteros!!")
                continue
            resultado = actualizar_precio(codigo, precio)
            if resultado:
                print("Precio actualizado!!")
            else:
                print("La hamburguesa no existe!!")
            continuar = input("¿Desea actualizar otro precio? (s/n): ")
            if continuar.lower() != "s":
                break

    elif opcion == "4":
        codigo = input("Ingrese código de la hamburguesa: ")
        buscar_codigo(codigo)

    elif opcion == "5":
        mostrar_todos()

    elif opcion == "6":
        print("La hamburguesería ha cerrado. Hasta pronto, cliente.")
        break

    else:
        print("Debe seleccionar una opción válida!!")