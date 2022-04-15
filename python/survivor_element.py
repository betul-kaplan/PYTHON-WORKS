#survivor element  :

def survivor(element,step):
    liste = [i for i in range(1,element+1)]
    count = 0
    while len(liste) > 1:
      new = liste.copy()
      for i in liste:
        count += 1
        if count == step:
          new.remove(i)
          count = 0
          print(new)
      liste = new
survivor(21,6)