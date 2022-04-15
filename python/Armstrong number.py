#Armstrong_number  :


while True:
  w = input("Enter number: ")
  t = len(w)
  total = 0
  if w.isnumeric():
    for i in w:
      total += (int(i)**t)
    if total == int(w):
      print(f"{w} is an armstrong number")
      break
    else:
      print(f"{w} is not an armstrong number")
  else:
    print("invalid")

#2.way  :

while True :
    
    number = input("Enter a positive integer number :")
    digits = len(number)
    summ = 0
    
    if not number.isdigit() :
        
        print(number, " is invalid entry. Please enter valid input.")
        
    elif int(number) >= 0 :
        
        for i in range(digits) :
            
            summ = summ + int(number[i]) ** digits
            
        if summ == int(number) :
            print(number, " is an Armstrong Number.")
            break
        else :
            print(number, " is not an Armstrong Number.")
            break
            