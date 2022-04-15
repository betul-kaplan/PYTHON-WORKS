def calculator(a,b,c):
  if c== "+":
    print(a+b)
  if c== "-" :
    print(a-b)
  if c== "*" :
    print(a*b)
  if c== "/" :
    print(a/b)
  else:
    print("invalid")

calculator(3,4,"*")

#calculator  :


def calculator(x, y, opr) :
    if opr == "+" :
        return(x + y)
        
    elif opr == "-" :
         return(x - y)
        
    elif opr == "*" :
         return(x * y)
        
    elif opr == "/" :
         return(x / y)
        
    else :
        print("Enter a valid operator.")
calculator(3,4,"*")