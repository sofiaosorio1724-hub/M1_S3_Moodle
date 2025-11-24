def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)


def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("\nEl inventario está vacío\n")
        return

    calcular_subtotal = lambda p: p["precio"] * p["cantidad"]

    print("\n--- INVENTARIO ---")
    for i in range(len(inventario)): #recorre toda la lista
        producto = inventario[i]  #dame el producto que esta en el inventario en la posion i
        subtotal = calcular_subtotal(producto) #calcula subtotal y lo pone en cada producto
        print(f"{i+1}. {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']} | Subtotal: {subtotal}")
    print("-------------------\n")


def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if producto == None:
        return False

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    return True


def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto == None:
        return False
    inventario.remove(producto)
    return True


def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]

    total_unidades = 0
    total_valor = 0

    producto_mas_caro = inventario[0] #inventario[0], empieza a comparar en la lista desde el 0 hasta encontarr en el mas alto valor
    producto_mayor_stock = inventario[0]

    for producto in inventario:
        total_unidades += producto["cantidad"]
        total_valor += subtotal(producto)

        if producto["precio"] > producto_mas_caro["precio"]:#Si el precio del producto actual es MAYOR que el del producto más caro encontrado hasta ahora actualizalo
            producto_mas_caro = producto 

        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    return {
        "total_unidades": total_unidades,
        "total_valor": total_valor,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
