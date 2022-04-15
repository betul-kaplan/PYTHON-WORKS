#strong password 

import random

random.randint(10,20)

uppers=[chr(random.randint(65,90)) for i in range(3)]
uppers

lowers=[chr(random.randint(97,122)) for i in range(3)]
lowers

numbers=[chr(random.randint(48,57)) for i in range(3)]
numbers

chars = chr(random.randint(33,47)) + chr(random.randint(58,64))
chars

pasword="".join(numbers)+"".join(lowers)+"".join(uppers)+"".join(chars)
pasword
