#! /usr/bin/python
#!encoding: UTF-8

#Importamos la librería sys para permitir el uso de sys.argv.
import sys 
# Comprobamos que el usuario haya introducido como argumento el número de intervalos, y en caso contrario, lo solicitamos por pantalla.
if (len(sys.argv) == 1):
    n = int(raw_input("Introduzca el número de intervalos utilizados para aproximar pi: "))
else:
    n = int(sys.argv[1])
#Si el número de intervalos es nulo o negativo, pedimos al usuario un reintento hasta obtener una respuesta válida.
while (n <= 0):
    n = int(raw_input("Debe introducir una cantidad positiva de intervalos. Inténtelo de nuevo: "))

#Inicializamos la variable suma y el valor de referencia de pi con 35 decimales.
suma = 0.0
PI = 3.1415926535897931159979634685441852

#Realizamos el cálculo aproximado de pi de acuerdo con la fórmula proporcionada.
for i in range (1, n+1):
    xi = (i-0.5)/n
    fxi = 4/(1+xi**2)
    suma += fxi
    # Mostramos la información relativa a cada elemento del sumatorio.
    print "Subintervalo: (%3.4f, \t %3.4f) \t xi = %3.4f, \t fi = %3.4f" % ((i-1.)/n, (i+0.)/n, xi, fxi)
pi = suma/n 

#Mostramos en pantalla el valor resultante de pi y su valor real con 35 decimales.
print "El valor resultante de pi es:", pi
print "El valor de pi con 35 decimales es: %1.35g" % PI
