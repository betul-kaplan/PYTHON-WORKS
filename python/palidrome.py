#palindrome  :

list1=[1,2,3,2,1]
list2=list1.copy()
list2.reverse()
if list1 == list2:
  print("palindrome")

else:
  print("not palindrome") 


  #palindrome  :

  input = "1221"
liste=[]
for i in input:
  if i.isalnum():
    liste.append(i)

if liste == liste[::-1]:
  print(f"{[input]} is a palindrome")
else:
  print("no palindrome")  


#palindrome word  :
def is_palindrome(word):
  return word == word[::-1]
print(is_palindrome("anna"))