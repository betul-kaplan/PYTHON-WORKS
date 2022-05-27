#!/bin/bash
COUNT=0
until [[ $COUNT -eq 5 ]] # This command will run until it returns truthy
do
    read -p “Enter a number to find greatest of them :” NUMBER
    echo $NUMBER >> text.txt
    (( COUNT++ ))
done
sort -n text.txt | tail -1




num_list =(input("Enter five numbers separated by space please!  : ").strip().split())
if len(num_list) < 5:
    print ("You should enter", 5-len(num_list), "more number(s)")
elif len(num_list) > 5:
    print ("You entered", len(num_list)-5, "more number(s) than 5")
else:
#   print("Largest element is:", max(num_list))
    print(sorted(num_list)[-1])