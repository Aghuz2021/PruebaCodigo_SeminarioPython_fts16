def fun(ini,inf,sup):
   sum = ini
   for d in range(inf, sup):
      sum += d
   return sum
def main():
   print(fun(0,0,4))
main()