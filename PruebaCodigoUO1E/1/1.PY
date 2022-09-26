def fun(cad,c):
   res=""
   i=0
   while i < len(cad):
      res=res+cad[i]+c
      i+=1
   return res
def main():
   cad="Domingo"
   nuevaCadena=fun(cad,"-")
   print(
      nuevaCadena
   )
main()