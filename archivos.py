import csv #importa la impreria csv que viene con python

def guardar_csv(inventario, ruta, incluir_encabezado=True):
    #Guarda el inventario en CSV con encabezado
    if len(inventario) == 0:
        print("No se puede guardar porque el inventario está vacío.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as file:
            write = csv.writer(file)
            if incluir_encabezado:
                write.writerow(["nombre", "precio", "cantidad"])

            for producto in inventario:
                # Escribir una fila con 3 columnas
                write.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])

        print(f"Inventario guardado correctamente en: {ruta}")

    except PermissionError:
        print("Error: No tienes permiso para escribir en esa ubicación.")
    except Exception as error:
        print("Error al guardar el archivo:", error)


def cargar_csv(ruta):
    productos = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as file:
            read = csv.reader(file)
            encabezado = next(read, None) #lee linea por linea el encabezado

            # Valida encabezado 
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Encabezado invalido.")
                return None, 0

            for fila in read:
                # validar número de columnas
                if len(fila) != 3:
                    errores += 1
                    continue

                nombre = fila[0]

                try:
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    if precio < 0 or cantidad < 0:
                        raise ValueError("Valores negativos")
                except Exception:
                    errores += 1
                    continue

                productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

        return productos, errores

    except FileNotFoundError: #error para cuando no se encuentre un archivo
        print("Archivo no encontrado:", ruta)
        return None, 0 #el 0 es para decir que ninguna fila tuvo error
    except UnicodeDecodeError: #cuando intenta leer archivo pero tiene caracteres que no puede interpretar
        print("Error de codificación al leer el archivo.")
        return None, 0
    except Exception as error: #el exception carga errores inesperados
        print("Error al cargar el archivo:", error)
        return None, 0

    
