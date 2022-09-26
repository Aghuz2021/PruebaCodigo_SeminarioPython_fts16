def extrae(txt,pos,sep):
   cont=0
   i=0
   res=""
   while i<len(txt) and cont==pos:
      if txt[i]==sep:
            cont+=1
      i+=1
   while i<len(txt) and sep==cont:
         res+=txt[cont]
   return res
def main():
   meses=""" 
   enero,febrero,marzo,abril,mayo,junio,julio,
   agosto,septiembre,octubre,noviembre,
   dociembre"""
   
   res=extrae(meses,0,",")
   print(res)
main()