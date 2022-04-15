answer = 44

question = 'What number am I thinking of?  '
print ("Let's play the guessing game!")

while True:
    guess = int(input(question))

    if guess < answer:
        print('Little higher')
    elif guess > answer:
        print('Little lower')
    else:  # guess == answer
        print('Are you a MINDREADER!!!')
        break

#guessing game  :


for i in range(1,5) :

  tahmin = int(input("tahmin "))

  print(f"{4-i} tahmin hakkınız kaldı")
 

  if 4-i ==0 :
      print("tekrar deneyin ")
  elif tahmin < sayı :

    print("biraz yukseltın")

  elif tahmin > sayı :

    print("biraz azaltın") 

  elif tahmin == sayı :

    print("aklımı okudunuz")
    break