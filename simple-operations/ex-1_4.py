"""*------------------------------ ex-1_4.py ------------------------------*
   *            Ejercicio 1.4 de la guía de Operaciones Simples            *
   *                                                                       *
   * - Consigna:                                                           *
   *   Confeccionar un programa en el que se ingrese un monto expresado en *
   *   bitcoins y la cotización del bitcoin al dólar y luego imprima dicho *
   *   monto en dólares.                                                   *
   *   2.a- Deberá aceptarse los datos con precisión decimal y mostrar el  *
   *   resultado del mismo modo.                                           *
   *   2.b- Deberá aceptarse datos enteros y mostrar un resultado con      *
   *   precisión decimal.                                                  *
   *   2.c- Deberá aceptarse datos con precisión decimal y mostrar un      *
   *   resultado entero.                                                   *
   *-----------------------------------------------------------------------*"""

# Solicitar al usuario que ingrese el monto de bitcoins y guardarlo en una variable.
bitcoins = float(input('Ingrese el monto de bitcoins:\n'))

# Similar a lo hecho en el anterior input, pero para la cotización del bitcoin al dólar.
bitcoin_dollar_price = float(input('Ingrese la cotización del bitcoin al dólar:\n'))

# Calcular el monto en dólares.
dollars = bitcoins * bitcoin_dollar_price

# Verificar si el monto en dólares es un número entero.
if dollars.is_integer():

    # Formatear a 0 decimales en caso de que sea entero para lograr precisión decimal.
    format_str = "%.0f USD"
    
    # Imprimir el resultado con el formato adecuado.
    print(format_str % dollars)

else:

    # Obtener la parte decimal como una cadena.
    decimal_part = str(dollars).split('.')[1]

    # Obtener el número de decimales escritos.
    num_decimals = len(decimal_part)

    # Crear el formato de impresión con el número de decimales.
    format_str = '%.' + str(num_decimals) + 'f USD'

    # Imprimir el resultado con el formato adecuado.
    print(format_str % dollars)