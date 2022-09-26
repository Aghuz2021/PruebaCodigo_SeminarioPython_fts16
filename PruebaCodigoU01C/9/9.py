def getDia(mmdd):
   mmdd = mmdd%100
   return mmdd
def getMes(mmdd):
   return mmdd//100
def fVal(mmdd):
   res=None
   mes=getMes(mmdd)
   dia=getDia(mmdd)
   if (dia<=31 and (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes == 10 or mes==12)):
      res=True
   elif (dia<=30 and mes==4 or mes==6 or mes==9 or mes==11 ):
      res=True
   elif ( dia<=28 and (mes==2)):
      res=True
   else: res=False
   return res
def main():
   mmdd=1224
   print(mmdd,"->",fVal(mmdd))
   mmdd=1130
   print(mmdd,"->",fVal(mmdd))
   mmdd=701
   print(mmdd,"->",fVal(mmdd))
   mmdd=3106
   print(mmdd,"->",fVal(mmdd))
   mmdd=2513
   print(mmdd,"->",fVal(mmdd))
   mmdd=230
   print(mmdd,"->",fVal(mmdd))
   mmdd=2001
   print(mmdd,"->",fVal(mmdd))
   
   
   
   
main()