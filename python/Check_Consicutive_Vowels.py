string=input().strip().lower()
counter=0
for i in range(len(string)-1):
    if string[i] in 'aeiou' and string[i+1] in 'aeiou':counter+=1
     
if counter > 0 :
    print('Positif')
if counter==0:
    print('negatif')  

    another solution:

word = input("Please enter a string: ")
word = word.lower()

vowels = ["a", "e", "i", "o", "u"]
exist = False

for i in range(len(word)-1):
  if word[i] in vowels:
    if word[i+1] in vowels:
      exist = True
      break
      
if exist:
  print("Positive")
else:
  print("Negative")    