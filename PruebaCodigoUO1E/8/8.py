def f(p):
   v="aeiou"
   c="bcdfghjklmñpqrstvwxyz"
   r=""
   for x in p:
      if (x in v)or (x in c):
         r=r + chr(ord(x)-32)
      else:
         r=r+ x
   return r
def main():
   print(f("ab"),f("92"),f("2d"))
main()