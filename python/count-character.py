#Count the character in the given senrences :

nput("please enter any sentence  :")
my_dict = {}
  
  for i in text:
          if i in my_dict:
                      my_dict[i] += 1
                          else:
                                      my_dict[i] = 1
                                      print ("Count of all characters in your entered sentence is :\n "
                                                                                      +  str(my_dict))
