import math
def areaTriangulo(base,altura):
        res = (base * altura)/2
        return res

def areaCirculo(radio):
        res=math.pi*(radio**2)
        return res

def areaNegra(diametro):
        area_triangulo= areaTriangulo(diametro,diametro/2)
        area_circulo = areaCirculo(diametro/2)
        area_negra= area_triangulo+((area_circulo/2)-area_triangulo)
        return area_negra


def main():
        diametro = int(input("ingresar diametro: "))
        res = areaNegra(diametro)
        print("para diametro: {:.2f}".format(diametro))
        print("El area negra es: {:.2f}".format(res))

main()
