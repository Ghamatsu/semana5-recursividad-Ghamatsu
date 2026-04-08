"""
Ejercicio 6:
Una tienda registra sus ventas diarias en una lista de números. Cada número representa el monto de ventas de un día.
Se solicita calcular el total de ventas acumuladas.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def total_ventas_ciclo(ventas):
    total = 0
    for venta in ventas:
        total += venta
    return total
print(total_ventas_ciclo([1500, 2000, 500, 1000]))

def total_ventas_recursivo(ventas):
    if len(ventas) == 0:
        return 0
    return ventas[0] + total_ventas_recursivo(ventas[1:])
print(total_ventas_recursivo([1500, 2000, 500, 1000]))