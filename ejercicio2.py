productos = {
    "Arroz": 10.0,
    "Frijoles": 20,
    "Azucar": 5,
    "Pizza": 5,
    "Sal": 0.25
}

name_product = input("Ingrese el nombre de un producto: ")

if name_product in productos:
    quantity_product = int(input("Ingrese la cantidad que desea comprar: "))
    precio_Unidad = productos[name_product]
    total_a_pagar = precio_Unidad * quantity_product
    print(f"El total a pagar por {quantity_product} {name_product} es: ${total_a_pagar:.2f}")
else:
    print(f"El producto {name_product} no se encuentra disponible en la tienda.")