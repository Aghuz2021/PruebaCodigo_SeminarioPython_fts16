def extrae (txt,pos,sep):
   cont=0
   i=1
   res=""
   while i<len(txt) and cont!=pos:
      if txt[i]==sep:
            cont+=1
      i+=1
   while i<len(txt) and txt[i] != sep:
      res+= txt[i]
      i+=1
   return res

def main():
   meses="""
enero,febrero,marzo,abril,mayo,
junio,julio,agosto,septiembre,
octubre,noviembre,diciembre
"""
   res=extrae(meses,0,",")
   print(res)
   res=extrae(meses,6,",")
   print(res)
   res=extrae(meses,11,",")
   print(res)
main()   