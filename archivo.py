import csv

def guardar_csv(inventory, path, include_header=True):

    if not inventory:
        print("No se puede guardar, el inventario esta vacio")
        return

    try:
        with open(path, "w", newline="", enconding="utf-8") as file:
           writer = csv.writer(file)

           if include_header:
                writer.writerow(["name","price","quantity"])

                for product in inventory:
                    writer.writerow([product["name"]],[product["price"]],[product["quantity"]]) #writerow significa escribir una fila
                
        print(f"Inventario guardado en: {path}")

    except PermissionError:
        print("No tienes permiso para escribir en este archivo")
    except Exception as e:
        print(f"Error: {e}")

def cargar_csv(path):

    productos_cargados = []
    errores = 0

    try: 
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            encabezado = next(reader, None)

            if encabezado != ["name", "price", "quantity"]:
                print("El encabezado no es valido")
                return None, 0
            
            for fila in reader:

                if len(fila) != 3:
                    errores += 1
                    continue
                
                name, price_str, quantity_str = fila

                try:
                    price = float(price_str)
                    quantity = int(quantity_str)

                    if price < 0 or quantity < 0:
                        raise ValueError
                    
                except ValueError:
                    errores += 1
                    continue

                productos_cargados.append({
                    "name": name, 
                    "price": price,
                    "quantity": quantity
                })

        return productos_cargados, errores
    except FileNotFoundError:
        print("Archivo no encontrado")
        return None, 0
    
    except UnicodeEncodeError:
        print("El archivo tiene otro formata")
        return None, 0
    
    except Exception as e:
        print(f"Error: {e}")
        return None, 0
    