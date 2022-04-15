#comfortable word :

left=set("qwertgfdsazxcvb")
right=set("yuıopğühjklşinmöç")
word =input("enter a word :")

comf_word= (set(word) & left )and (set(word) & right)

if comf_word:
  print(f"{word} is a comfortable word")
else:
  print(f"{word} is not a comfortable word")