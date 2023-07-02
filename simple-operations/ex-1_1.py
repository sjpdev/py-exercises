"""*------------------------------ ex-1_1.py ------------------------------*
   *            Ejercicio 1.1 de la guía de Operaciones Simples            *
   *                                                                       *
   * - Consigna:                                                           *
   *   Confeccionar un programa en el que se ingrese la base y la altura   *
   *   de un triángulo e informe su superficie.                            *
   *                                                                       *
   * - Ejemplo:                                                            *
   *   Ingrese base del triángulo:                                         *
   *   20                                                                  *
   *   Ingrese altura del triángulo:                                       *
   *   4.6                                                                 *
   *   Para una base de 20.00 y una altura de 4.60 la superficie del       *
   *   triángulo será de: 46.00                                            *
   *                                                                       *
   * - Nota: Sup=(base*altura)/2                                           *
   *-----------------------------------------------------------------------*"""

# Solicitar al usuario que ingrese la base del triángulo y guardarlo en una variable.
base = float(input('Ingrese base del triángulo:\n'))

# Similar a lo hecho en el anterior input, pero esta vez para la altura del triángulo.
height = float(input('Ingrese altura del triángulo:\n'))

# Calcular la superficie del triángulo usando la fórmula: Sup=(base*altura)/2
surface = (base * height / 2)

# Imprimir la base, la altura y la superficie dentro de la oración, como pide la consigna, además agregar un formateo de dos decimales para que los valores conserven dos decimales luego de la coma.
print('Para una base de %.2f y una altura de %.2f la superficie del triángulo será de: %.2f' % (base, height, surface))