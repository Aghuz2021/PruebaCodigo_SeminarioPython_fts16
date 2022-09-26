#figura 1
""" def figura (b,car):
   for f in range(0,b):
      for c in range(0,b):
         if true:
            
            print(car,end="");
         else:
               print(end="  ");
      print()
def main ():
   figura(7," *")
   
main() """
#figura 2
""" def figura (b,car):
   for f in range(0,b):
      for c in range(0,b):
         if f==c:
            
            print(car,end="");
         else:
               print(end="  ");
      print()
def main ():
   figura(7," *")
main() """

#figura 3
""" def figura (b,car):
   for f in range(0,b):
      for c in range(0,b):
         if f==b-1 or f==c:
            
            print(car,end="");
         else:
               print(end="  ");
      print()
def main ():
   figura(7," *")
main() """
#figura 4
# def figura (b,car):
#    for f in range(0,b):
#       for c in range(0,b):
#          if f==c or f+c==b-1:
            
#             print(car,end="");
#          else:
#                print(end="  ");
#       print()
# def main ():
#    figura(7," *")
# main()
#figura 5
""" def figura (b,car):
   for f in range(0,b):
      for c in range(0,b):
         if f==c or f+c>=b-1:
            
            print(car,end="");
         else:
               print(end="  ");
      print()
def main ():
   figura(7," *")
main() 
"""
#figura 6
def figura (b,car):
   for f in range(0,b):
      for c in range(0,b):
         if (f<=c and f+c<=b-1)or c==b//2:
            
            print(car,end="");
         else:
               print(end="  ");
      print()
def main ():
   figura(7," *")
main() 
