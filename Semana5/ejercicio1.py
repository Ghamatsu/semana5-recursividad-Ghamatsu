"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    """
    # Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    lista = []
    for i in range(1, n + 1):
        lista.append(i)

    return lista
print(contar_ciclo(5))


def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    lista = []
    if n == 0:
        return []
    
    lista = contar_recursivo(n - 1)
    lista.append(n)
    return lista
print(contar_recursivo(6))
