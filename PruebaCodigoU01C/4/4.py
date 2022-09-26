def fun(nombre):
   msj = "hola"
   if nombre !="":
      msj = msj +" "+nombre
   return msj

def main():
   print(fun("")+", ",end="")
   print(fun("Augusto"))   
main()
