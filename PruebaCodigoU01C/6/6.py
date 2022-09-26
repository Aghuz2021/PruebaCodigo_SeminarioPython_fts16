def fun(num):
   if (num <= -10):
         res= "#"
   elif (num==0):
         res= "@"
   elif (num>0 and num<=10):
         res = "&"
   else:
         res = "?"
         
   return res

def main():
   print(
      fun(11),
      fun(0),
      fun(-30),
      fun(-1),
      fun(0)
      
   )
main()