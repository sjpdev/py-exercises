"""*------------------------------ ex-1_2.py ------------------------------*
   *            Ejercicio 1.2 de la guía de Operaciones Simples            *
   *                                                                       *
   * - Consigna:                                                           *
   *   Hacer un programa en el que se ingresen dos números positivos y se  *
   *   muestre un común múltiplo de ambos.                                 *
   *                                                                       *
   * - Ejemplos:                                                           *
   *   Ingrese primer número positivo:                                     *
   *   10                                                                  *
   *   Ingrese segundo número positivo:                                    *
   *   3                                                                   *
   *   30 es múltiplo de 10 y de 3                                         *
   *                                                                       *
   *   Ingrese primer número positivo:                                     *
   *   7                                                                   *
   *   Ingrese segundo número positivo:                                    *
   *   5                                                                   *
   *   35 es múltiplo de 7 y de 5                                          *
   *-----------------------------------------------------------------------*"""

while True:

    # Solicitar al usuario que ingrese el primer número positivo y guardarlo en una variable.
    number1 = int(input('Ingrese primer número positivo:\n'))

    # Similar a lo hecho en el anterior input, pero esta vez para el segundo número positivo.
    number2 = int(input('Ingrese segundo número positivo:\n'))

    # Imprimir y calcular el común múltiplo de los dos números ingresados si son positivos.
    if number1 >= 0 and number2 >= 0:

        # Multiplicar el primer número positivo con el segundo.
        multiple = number1 * number2

        # Imprimir el múltiplo, el primer número positivo y el segundo dentro de la oración, como pide la consigna.
        print('%d es múltiplo de %d y de %d' % (multiple, number1, number2))

        # Finalizar el programa.
        break

    else:

        # Interrumpir el bucle while si alguno de los dos números no es positivo.
        break