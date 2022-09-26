def fun2(a,c):
    return a+c
def fun(a,b):
    a=b+1
    b=2
    fun2(a,b)
print(fun(1,10))