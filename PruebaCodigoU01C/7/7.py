def fun(num):
   if(num>=0):
      if(num==0):
         res="|"
      else:
         res = "+"
   else:
      res = "-"
   return res 

def main():
   print(fun(1),
         fun(0),
         fun(-3),
         fun(-1),
         fun(-0)
         )   
main()