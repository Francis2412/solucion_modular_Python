import os

def main():
    mensaje = "Bienvenido a Comercial VAle Todo!"
    nombre = None
    cantidad = 0
    precio = subtotal = descuento = iva = total = 0.0
    impuesto = 0.15

    #Invocar a leer_datosVentas()
    nombre_cliente, nombre_producto1, nombre_producto2, precio_producto1, precio_producto2, cantidad_producto1, cantidad_producto2 = leer_datosVentas(mensaje)

    #Invacar a calcular_total()
    porcentaje = float(input("Digite el porcentaje de descuento: "))
    porcentaje = porcentaje / 100
    total, subtotal, descuento, iva = calcular_total(precio_producto1, precio_producto2, cantidad_producto1, cantidad_producto2, porcentaje, impuesto)
  

def calcular_total(precio_producto1, precio_producto2, cantidad_producto1, cantidad_producto2, porcentaje, impuesto):

    # Subtotal
    subtotal_producto1, subtotal_producto2 = calcular_subtotal(cantidad_producto1, cantidad_producto2, precio_producto1, precio_producto2)

    #Subtotal Acumulado 
    subtotal = calcular_total_productos (subtotal_producto1, subtotal_producto2)

    # Descuento
    descuento = calcular_descuento(subtotal, porcentaje)

    #IVA
    iva = calcular_iva(subtotal, impuesto)
    total = subtotal - descuento + iva
    return total, subtotal, descuento, iva

def calcular_subtotal (cantidad_producto1, cantidad_producto2, precio_producto1, precio_producto2):
    subtotal_producto1 = cantidad_producto1 * precio_producto1 
    subtotal_producto2 = cantidad_producto2 * precio_producto2
    return subtotal_producto1, subtotal_producto2

def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * porcentaje
    return descuento

def calcular_iva(subtotal, impuesto):
    iva = subtotal * impuesto 
    return iva

def leer_datosVentas(msj):
    print(msj)
    print("*"*40)
    nombre_cliente = input("Digite el nombre del cliente: ")
    nombre_producto1 = input("Ingrese el nombre del producto #1: ")
    precio_producto1 = float(input("Ingrese el precio del producto #1"))
    cantidad_producto1 = float(input("Ingrese la cantidad del producto #1"))
    nombre_producto2 = input("Ingrese el nombre del producto #2: ")
    precio_producto2 = float(input("Ingrese el precio del producto #2"))
    cantidad_producto2 = float(input("Ingrese la cantidad del producto #2"))

    return nombre_cliente, nombre_producto1, nombre_producto2, precio_producto1, precio_producto2, cantidad_producto1, cantidad_producto2

def calcular_total_productos(subtotal_producto1, subtotal_producto2):
    subtotal = subtotal_producto1 + subtotal_producto2 
    return subtotal

def calcular_promedio_precio(precio_producto1, precio_producto2):
    promedio_precio = (precio_producto1 + precio_producto2) / 2
    return promedio_precio

def mostrar_factura (nombre_cliente, nombre_producto1, nombre_producto2, precio_producto1, precio_producto2, cantidad_producto1, cantidad_producto2, subtotal, descuento, iva, total, promedio_precio):
    print("************** FACTURA **************")
    print(f"Nombre del cliente: {nombre_cliente}")
    print("Productos: ")
    print(f"{nombre_producto1} x{cantidad_producto1}... {precio_producto1}")
    print(f"{nombre_producto2} x{cantidad_producto2}... {precio_producto2}")
    print(f"Subtotal: {subtotal}")
    print(f"Descuento: {descuento}")
    print(f"IVA: {iva}")
    print(f"Promedio de los precios: {promedio_precio}")
    print(f"Total: {total}")
main()