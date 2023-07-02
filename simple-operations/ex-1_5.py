"""*------------------------------ ex-1_5.py ------------------------------*
   *            Ejercicio 1.5 de la guía de Operaciones Simples            *
   *                                                                       *
   * - Consigna:                                                           *
   *   Elaborar un programa en el que se ingrese una cantidad expresada en *
   *   segundos y luego la exprese en días, horas, minutos y segundos.     *
   *                                                                       *
   * - Ejemplo:                                                            *
   *   Ingrese tiempo en segundos:                                         *
   *   87708                                                               *
   *   1 día(s), 0 hora(s), 21 minuto(s), 48 segundo(s).                   *
   *-----------------------------------------------------------------------*"""

# Inicializar variables.
days = 0
hours = 0
minutes = 0

# Solicitar al usuario ingresar el tiempo en segundos.
seconds = int(input('Ingrese tiempo en segundos:\n'))

# Calcular los minutos dividiendo los segundos entre 60.
minutes = seconds // 60

# Obtener los segundos restantes después de calcular los minutos.
seconds = seconds % 60

# Calcular las horas dividiendo los minutos entre 60.
hours = minutes // 60

# Obtener los minutos restantes después de calcular las horas.
minutes = minutes % 60

# Calcular los días dividiendo las horas entre 24.
days = hours // 24

# Obtener las horas restantes después de calcular los días.
hours = hours % 24

# Imprimir los días, horas, minutos y segundos.
print('%d día(s), %d hora(s), %d minuto(s), %d segundo(s).' % (days, hours, minutes, seconds))