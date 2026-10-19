def registrar_pedido():

    # VALIDAR EL NOMBRE DEL CLIENTE
    cliente = " ".join(
        input("Nombre del cliente: ").strip().split()
    )

    if len(cliente) < 2:
        print("Error: Ingrese un nombre válido.")
        return

    if not all(
        caracter.isalpha() or caracter in " -'"
        for caracter in cliente
    ):
        print("Error: El nombre contiene caracteres no permitidos.")
        return

    print("Cliente válido:", cliente)


# Ejecutar la función para comprobar que funciona
if __name__ == "__main__":
    registrar_pedido()