"""*------------------------------ ex-1_3.py ------------------------------*
   *            Ejercicio 1.3 de la guía de Operaciones Simples            *
   *                                                                       *
   * - Consigna:                                                           *
   *   Confeccionar un programa en el que se ingresen 5 notas de examenes  *
   *   y luego imprima el promedio general redondeando a una cifra         *
   *   decimal.                                                            *
   *                                                                       *
   * - Ejemplo:                                                            *
   *   Ingrese las 5 notas de exámenes:                                    *
   *   10                                                                  *
   *   8                                                                   *
   *   4.75                                                                *
   *   9                                                                   *
   *   6.5                                                                 *
   *   El promedio general es: 7.6                                         *
   *-----------------------------------------------------------------------*"""

# Crear una lista vacía para almacenar los valores ingresados.
valores = []

# Solicitar al usuario que ingrese 5 valores y agregarlos a la lista.
print('Ingrese las 5 notas de exámenes:')

for _ in range(5):

    valor = float(input())
    valores.append(valor)

# Calcular el promedio sumando los valores y dividiendo entre la cantidad de elementos en la lista.
promedio = sum(valores) / len(valores)

# Imprimir el promedio.
print("El promedio general es:", promedio)