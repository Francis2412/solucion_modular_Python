import os

def main():
    mensaje = "Bienvenido a Comercial VAle Todo!"
    nombre = None
    cantidad = 0
    precio = subtotal = descuento = iva = total = 0.0
    impuesto = 0.15

    #Invocar a leer_datosVentas()
    nombre = leer_datosVentas(mensaje)

    #Invacar a calcular_total()
    calcular_total(cantidad, precio, porcentaje, impuesto)
    cantidad= int(input("Digite la cantidad comprada: "))
    porcentaje = float(input("Digite el porcentaje de descuento: "))
    total, subtotal, descuento, iva = calcular_total(cantidad, precio, porcentaje, impuesto)

def calcular_total(cantidad, precio, porcentaje, impuesto):
    subtotal = calcular_subtotal(cantidad, precio)
    descuento = calcular_descuento(subtotal, porcentaje)
    iva = calcular_iva(subtotal, impuesto)
    total = subtotal - descuento + iva

def calcular_subtotal (precio_producto1, precio_producto2, cantidad_producto1, cantidad_producto2):
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

main()