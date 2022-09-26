def fun(d,c,b,a):
   largo=len(a)
   r=""
   i=0
   while i < largo and i <3:
      r=r+a[i]
      i+=1
   txt="{} {} de {} de {}".format(r,b,c,d)
   return txt
def main():
   res=fun(2022,"Mayo",30,"Lunes")
   print(res)
main()