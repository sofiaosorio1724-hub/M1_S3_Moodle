from servicios import add_products, show_inventory, search_product, update_product, delete_product, calculate_statistics
from archivo import guardar_csv, cargar_csv

def main():

    inventory = []

    print("\n--------Menu inventario--------")
    print("1. Agregar Productos")
    print("2. Mostar Inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadisticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    option = input("Ingresa la opcion que deseas: ")
    
    while True:
        if option == "1":
            print("----Agregar Productos----")
            name = input("Nombre del producto: ") 

            try:
                price = float(input("Precio del producto: "))
                quantity = int(input("Cantidad: "))
                if price < 0 or quantity < 0:
                    print("Debes ingresar un valor mayor a 0")
                    continue
                add_products(inventory, name, price, quantity)

            except ValueError:
                print("Producto agregado con exito")
            

        elif option == 2:
            print("Mostrar Inventario")
            show_inventory(inventory)

if __name__=="__main__":
    main()