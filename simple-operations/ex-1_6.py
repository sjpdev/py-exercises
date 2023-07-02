"""*------------------------------ ex-1_6.py ------------------------------*
   *            Ejercicio 1.6 de la guía de Operaciones Simples            *
   *                                                                       *
   * - Consigna:                                                           *
   *   Confeccionar un programa en el que se ingresen un par de números    *
   *   enteros. Calcular y mostrar la distancia entre ellos.               *
   *                                                                       *
   * - Ejemplos:                                                           *
   *   Ingresá un número entero: -133                                      *
   *   Ingresá otro número entero, además de -133: -3                      *
   *   (-133)->(-3)=130                                                    *
   *                                                                       *
   *   Ingresá un número entero: 33                                        *
   *   Ingresá otro número entero, además de 33: -33                       *
   *   (33)->(-33)=66                                                      *
   *-----------------------------------------------------------------------*"""

# Solicitar al usuario ingresar un número entero.
integer_number1 = int(input('Ingresá un número entero: '))

# Similar a lo hecho en el anterior input, pero para un seguno número entero.
integer_number2 = int(input('Ingresá otro número entero, además de %d: ' % integer_number1))

# Calcular módulo.
module = abs(integer_number1 - integer_number2)

# Imprimir los números ingresados y el módulo, como pide la consigna.
print('(%d)->(%d)=%d' % (integer_number1, integer_number2, module))