#ejercicio 1
#jugs=("BANANA") #consonates
#jugk=("BANANA") #vocales
#palabra=("BANANA")


def minion_game(string):
  s= 0
  k= 0
  for i in range(len(string)):
    if string[i] in "banana":
      k += len(string)-i
    else:
      s += len(string)-i
  if k>s:
    print("Kevin:", k)
    
