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
  print(k)

  if k>s:
    return("Kevin:", k)
  elif k<s:
    return("Stuart:",s)
  else:
    return("Draw")

print(minion_game("banan"))

if __name__ == '__main__':
  s1 = input()
  minion_game(s1)