def fun (cad):
   band=True
   res=""
   for i in range(0,len(cad)):
      print(range(0,len(cad)))
      if band:
         res=res+"-"+cad[i]
         band=False
      else:
         res+="+"+cad[i]
      return res
def main():
   cad="246"
   nuevaCadena=fun(cad)
   print(nuevaCadena)
main()