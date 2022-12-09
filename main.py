#ejercicio 1
jugs=("BANANA") #consonates
jugk=("BANANA") #vocales
palabra=("BANANA")


def minion_game(string):
  consonantes=""
  vocales= ""
  pos=0
  while(letra != string and pos<len(palabra)-1):
    pos= pos +1
    letra=palabra[pos]
  if letra != string:
    return -1
  else:
    return pos
print(minion_game(string))
    
if __name__ == '__main__':