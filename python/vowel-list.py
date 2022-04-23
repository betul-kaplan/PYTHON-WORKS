vowel_list = ['a', 'e', 'i', 'o', 'u']
first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

vowels=filter(lambda x :True if x in vowel_list else False, first_ten)

print("vowels are :",list(vowels))