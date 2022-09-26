import random
""" programa que genera numeros ramdom entre un limite inferior y sup 
con una condicion de que sean par y multiplo de 3 
Imprime por pantalla los numeros par y multiplo de tres conprendidos entre limite inferior y sup 
la cantidad de veces que nosotros declaramos en el main"""
def aleatorio(inf,sup):
   return random.randint(inf, sup)
def condicion(num):
   return num %2 == 0 and num %3 == 0
def imprimirLinea(cant,inf,sup):
   imprimo=0
   numAle = aleatorio(inf, sup)
   while imprimo < cant:
      if condicion(numAle):
         print("{:5d}".format(numAle),end=" ")
         imprimo= imprimo + 1
      numAle = aleatorio(inf, sup)



def main():
   cantidad = 4
   limInf=100
   limSup=3000
   imprimirLinea(cantidad,limInf,limSup)
main()