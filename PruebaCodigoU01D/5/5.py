def fun2(pal,y):
   res=None
   n=len(pal)-1
   for x in pal:
      if x==y:
         res= n
      n-=1
   return res

def main():
   print(fun2("hola","o"))
main()