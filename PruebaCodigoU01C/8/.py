def mayorDetres(a,b,c):
   if (a>=b):
      if (a>=c):
            maxi = a
      else:
            maxi= c
   else:
      if(b>=c):
            maxi = b
      else:
            maxi=c
   return maxi


print(mayorDetres(3, 9, 10))