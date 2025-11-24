from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas
)
from archivos import guardar_csv, cargar_csv

def pedir_opcion():
    while True:
        option = int(input("Ingresa una opcion: "))
        if option in [int(i) for i in range(1, 10)]:
            return option
        print("Opción inválida, vuelve a intentarlo")


def pedir_float(mensaje):
    while True:
        valor = input(mensaje)
        try:
            v = float(valor)
            if v < 0:
                print("El valor no puede ser negativo.")
                continue
            return v
        except:
            print("Debes ingresar un numero válido")


def pedir_int(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            v = int(float(valor))
            if v < 0:
                print("El valor no puede ser negativo.")
                continue
            return v
        except:
            print("Debes ingresar un número entero válido (ej: 3).")


def mostrar_estadisticas_legible(inventario):
    calcular = calcular_estadisticas(inventario)
    if calcular is None:
        print("No hay datos para calcular estadísticas.")
        return
    print("\n--- Estadísticas del Inventario ---")
    print("Unidades totales:", calcular["total_unidades"])
    print("Valor total del inventario: {:.2f}".format(calcular["total_valor"]))
    pmc = calcular["producto_mas_caro"]
    pms = calcular["producto_mayor_stock"]
    print("Producto más caro: {} — Precio: {:.2f}".format(pmc["nombre"], pmc["precio"]))
    print("Producto con mayor stock: {} — Cantidad: {}".format(pms["nombre"], pms["cantidad"]))
    print("-----------------------------------\n")


def main():
    inventario = []

    while True:
        print("\n-------- Menú inventario --------")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Buscar Producto")
        print("4. Actualizar Producto")
        print("5. Eliminar Producto")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")
        print("---------------------------------")

        opcion = pedir_opcion()

        if opcion == 1:
            nombre = input("Nombre del producto: ")
            precio = pedir_float("Precio del producto: ")
            cantidad = pedir_int("Cantidad: ")
            agregar_producto(inventario, nombre, precio, cantidad)
            print("Producto agregado con éxito.")

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            nombre = input("Nombre a buscar: ")
            p = buscar_producto(inventario, nombre)
            if p is None:
                print("Producto no encontrado.")
            else:
                print("Producto encontrado:", p)

        elif opcion == 4:
            nombre = input("Nombre del producto a actualizar: ")
            if buscar_producto(inventario, nombre) is None:
                print("El producto no existe.")
            else:
                print("Deja vacío si no quieres cambiar nada.")
                precio_new = input("Nuevo precio: ")
                cantidad_new = input("Nueva cantidad: ")

                nuevo_precio = None
                nueva_cantidad = None

                if precio_new != "":
                    try:
                        val = float(precio_new)
                        if val < 0:
                            print("Precio no puede ser negativo. No se actualizará ese campo.")
                        else:
                            nuevo_precio = val
                    except:
                        print("Precio inválido. No se actualizará ese campo.")

                if cantidad_new != "":
                    try:
                        val = int(float(cantidad_new))
                        if val < 0:
                            print("Cantidad no puede ser negativa. No se actualizará ese campo.")
                        else:
                            nueva_cantidad = val
                    except:
                        print("Cantidad inválida. No se actualizará ese campo.")

                ok = actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
                if ok:
                    print("Producto actualizado.")
                else:
                    print("Error al actualizar el producto.")

        elif opcion == 5:
            nombre = input("Nombre del producto a eliminar: ")
            if eliminar_producto(inventario, nombre):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == 6:
            mostrar_estadisticas_legible(inventario)

        elif opcion == 7:
            ruta = input("Ruta donde guardar CSV (ej: inventario.csv): ")
            guardar_csv(inventario, ruta)

        elif opcion == 8:
            ruta = input("Ruta del CSV a cargar (ej: inventario.csv): ")
            productos_cargados, errores = cargar_csv(ruta)
            if productos_cargados is None:
                print("No se cargaron productos.")
                continue

            print(f"Se cargaron {len(productos_cargados)} productos. Filas inválidas: {errores}")

            # preguntar sobrescribir 
            while True:
                resp = input("¿Sobrescribir inventario actual? (S/N): ")
                if resp in ("S", "N"):
                    break
                print("Ingresa S o N.")

            if resp == "S":
                inventario.clear()
                inventario.extend(productos_cargados)
                accion = "reemplazado"
            else:
                cont_nuevos = 0
                cont_actualizados = 0
                for p in productos_cargados:
                    existente = buscar_producto(inventario, p["nombre"])
                    if existente is None:
                        inventario.append(p)
                        cont_nuevos += 1
                    else:
                        existente["cantidad"] = existente["cantidad"] + p["cantidad"]
                        if existente["precio"] != p["precio"]:
                            existente["precio"] = p["precio"]
                        cont_actualizados += 1
                accion = f"fusionado (nuevos: {cont_nuevos}, actualizados: {cont_actualizados})"

            print(f"Carga finalizada — Inventario {accion}. Productos cargados: {len(productos_cargados)}, filas inválidas: {errores}.")

        elif opcion == 9:
            print("Saliendo")
            break

if __name__ == "__main__":
    main()
