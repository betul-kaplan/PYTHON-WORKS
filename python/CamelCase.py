# Complete the solution so that the function will break up camel casing, using a space between words.

# Example "camelCasing" => "camel Casing" "identifier" => "identifier" "" => ""



def func(x) :
  y = ""
  for i in x :
    if i == i.upper() :
      y += " "
    y += i
  return y

a = "camelCasing"
b = "identifier"
c = "jackCan"
d = ""
e = "lovePhython"

print(func(e))