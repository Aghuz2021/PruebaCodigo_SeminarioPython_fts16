def fun(cad,a,b):
   encontro=False
   res=""
   for i in range(0,len(cad)):
      aux=cad[i]
      if aux==a and not encontro:
         aux=b
         encontro=True
      res+=aux
   return res
def main():
   cad="Hola hoy es un dia de frio y lluvia"
   nuevaCadena=fun(cad,"a","A")
   print(nuevaCadena)
main()