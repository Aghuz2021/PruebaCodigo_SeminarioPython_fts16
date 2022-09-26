import random
def saludo(val):
    msjA="Hola"
    msjB="Chau"
    res = msjA*(val)+ msjB*(1-val)
    
    return res
def main():
    ale=random.randint(0,1)
    print(saludo(ale))
main()