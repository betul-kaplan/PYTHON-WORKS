#You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

#Note: you will always receive a valid array (string in COBOL) containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
 
#solition - 1 :

walk =  "nsseweens"

def is_valid_walk(walk) :
  dicti = {"n" : 1 , "s" : -1, "w" : 1, "e" :-1}
  ns, we = 0, 0
  for i in walk :
    if len(walk) != 10 :
      return False
    elif i == "n" or i == "s" :
      ns += dicti[i]
    elif i == "w" or i == "e" :
      we += dicti[i] 
  return not ns and not we


#solition - 2 :

def is_valid_walk(walk):
    ns, ew = 0, 0
    if len(walk) == 10:
        for i in walk:
            if i == 'n': ns+=1
            if i == 's': ns-=1
            if i == 'w': ew+=1
            if i == 'e': ew-=1
    else:
        return False
    return ns == 0 and ew == 0
is_valid_walk("esew")


#solition - 3 :

# walk == 10
# north == south
# west == east

walk = "wweennsnns"

def func(walk) :
  return len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")

print(func(walk))

#solition - 4 :

from collections import Counter

def is_valid_walk(walk):
    a = Counter(walk)
    print(a)
    vertical = a['n'] - a['s']
    horizontal = a['e'] - a['w']
    if len(walk) != 10:
        return False
    else:
        if vertical == 0 and horizontal == 0:
            return True
        else:
            return False

print(is_valid_walk('nneesswwsn'))

