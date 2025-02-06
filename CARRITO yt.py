print("Bienvenido a tu carrito de compras\n")

print("Elige una de las siguientes opciones:")

nombres = []
precios = []

while True:
    print("1. Agregar objeto")
    print("2. Ver carrito")
    print("3. Eliminar objeto")
    print("4. Calcular el total")
    print("5. Salir")

    opcion = input("Ingresa tu elección: ")

    if opcion == "1":
        nombre = input("¿Qué objeto te gustaría agregar?: ")
        while True:
            precio_str = input(f"¿Cuál es el precio de {nombre}?: ")
            if precio_str.replace('.', '', 1).isdigit(): 
                precio = float(precio_str)
                if precio > 0:
                    nombres.append(nombre)
                    precios.append(precio)
                    print(f"{nombre} ha sido agregado al carrito.\n")
                    break 
                else:
                    print("El precio debe ser mayor que cero. Intenta de nuevo.")
            else:
                print("Precio inválido. Ingrese un número.")

    elif opcion == "2":
        if not nombres:
            print("El carrito de compras está vacío.")
        else:
            print("Los contenidos del carrito de compras son:")
            for i in range(len(nombres)):
                print(f"{i+1}. {nombres[i]} - ${precios[i]:.2f}\n")

    elif opcion == "3":
        if not nombres:
            print("El carrito de compras está vacío.")
        else:
            print("¿Qué artículo te gustaría eliminar?")
            for i in range(len(nombres)):
                print(f"{i+1}. {nombres[i]} - ${precios[i]:.2f}")
            while True:
                indice_str = input("Ingresa el número del artículo que deseas eliminar: ")
                if indice_str.isdigit():
                    indice = int(indice_str)
                    if 1 <= indice <= len(nombres):
                        articulo_eliminado = nombres.pop(indice - 1)
                        precio_eliminado = precios.pop(indice - 1)
                        print(f"{articulo_eliminado} ha sido eliminado.\n")
                        break
                    else:
                        print("Número inválido. Por favor, ingresa un número de artículo válido.")
                else:
                    print("Entrada inválida. Ingrese un número.")

    elif opcion == "4":
        total = sum(precios)
        print(f"El precio total de los artículos en el carrito de compras es ${total:.2f}\n") 

    elif opcion == "5":
        print("Adiós, ¡esperamos que vuelvas pronto!")
        break

    else:
        print("Opción no válida. Por favor, inténtalo de nuevo.")