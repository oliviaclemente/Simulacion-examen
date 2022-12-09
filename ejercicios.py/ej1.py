#ejercicio 1
#jugs=("BANANA") #consonates
#jugk=("BANANA") #vocales
#palabra=("BANANA")


def minion_game(string):
  s= 0
  k= 0
  vocal=["a","e", "i", "o", "u"]
  for i in range(0,len(string)):
    pal=string[:i]
    if vocal in "banana":
      k += string.count(pal)
      print(k)
    else:
      s += string.count(pal)
  if k>s:
    print("Kevin:", k)
  elif k<s:
    print("Stuart:",s)
  else:
    print("Draw")

if __name__ == '__main__':
  string = input()
  minion_game(string)