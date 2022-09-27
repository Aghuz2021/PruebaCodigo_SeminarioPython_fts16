def fun(txt):
   i=len(txt)-1
   while i>=0:
      txt += txt[i]
      i-=1
   return txt
def main():
   print(fun("hola"))
main()