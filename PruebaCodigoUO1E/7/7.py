def fun(txt,x):
   i=0
   desp=len(x)
   band=False
   while i<len(txt) and not band:
      if txt[i:i+desp] == x:
         band=True
      i+=1
   return band
def main():
   print(fun("pruebas","ba"),fun("hola","ba"))
main()