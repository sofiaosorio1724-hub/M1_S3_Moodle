def add_products(inventory, name, price, quantity):
    product = {"name": name,
                "price": price, 
                "quantity": quantity
    }
    inventory.append(product)

def show_inventory(inventory):
    if not inventory:
        print("Inventario vacio")
        return              # se utiliza para salir de la funcion o retornar algo
    
    print("----Inventario----")
    for product in inventory:
        print(product)

def search_product(inventory, name):
    for product in inventory:
        if product["name"] == name:
            return product #si se encuentra lo muestra
        
    return None #por si no se encuentra

def update_product(inventory, name, new_price=None, new_quantity=None):
    product = search_product(inventory, name)

    if product is None:
        return False #is compara identidad (si es literalmente el mismo objeto en memoria). 
                    #mejorar dicho si lleva none va con is
    
    if new_price is not None: #si nuevo precio SI existe
        product["price"] = new_price

    if new_quantity is not None:
        product["quantity"] = new_quantity

    return True

def delete_product(inventory, name):
    product = search_product(inventory, name)

    if product is None:
        return False
    
    else: 
        inventory.remove(product)
        return True

def calculate_statistics(inventory):
    if not inventory:
        return None
    
    sub_total = lambda product: product["price"] * product["quantity"]

    total_units = sum(product["quantity"] for product in inventory)
    total_value = sum(product["quantity"] for product in inventory)

    exprensive_product = max(inventory, key=lambda product: product["price"])
    product_stock = max(inventory, key=lambda product: product["quantity"] )

    return {"sub_total": sub_total,
            "total_units": total_units,
            "total_value": total_value,
            "exprensive_product": exprensive_product,
            "product_stock": product_stock
    }