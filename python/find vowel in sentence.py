#find vowels in the sentence :

sentence=input("enter any sentence")
def vowel(letter):
  vowels="a e ı i o ö u ü".split()
  if letter.lower()in vowels:
    return True
  else:
    return False
a=list(filter(vowel,sentence))
print(a)