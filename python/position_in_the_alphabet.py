you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

#first solution  :


print(ord("A"))


sentence = "Ali ata bak"

def func(sentence) :
  result = ""
  for i in sentence :
    if i.isalpha() :
      result += str(ord(i.upper()) - 64 ) + " "
  return result.strip()

func(sentence)


#second solution  :

def func(sentence) :
  return " ".join(str(ord(n.upper()) - 64) for n in sentence if n.isalpha())

sentence = "Ali, ata bak"

print(func(sentence))
