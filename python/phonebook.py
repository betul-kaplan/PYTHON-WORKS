# This  program creates a phonebook, adds requested contacts to the phonebook, finds them, and removes them
phonebook = {}

def find(keyword):
    return phonebook.get(keyword, f"Couldn't find phone number of {keyword}")

def add(name, phone_number):
    phonebook[name] = phone_number
    return f'Phone number of {name} is inserted into the phonebook'

def delete(name):
    try:
        phonebook.pop(name)
    except KeyError as err:
        return f'{err} is not in the phonebook'
    else:
        return f'{name} is deleted from the phonebook'

if __name__ == '__main__':
    print('Welcome to the phonebook application')
    print('1. Find phone number')
    print('2. Insert a phone number')
    print('3. Delete a person from the phonebook')
    print('4. Terminate')
    no = input('Select operation on Phonebook App (1/2/3) : ')
    while True:
        if no == '1':
            name = input('Find the phone number of : ')
            print(find(name))
            print(" ")
        elif no == '2':
            name = input('Insert name of the person : ')
            try:
                number = int(input('Insert phone number of the person: '))
            except ValueError as err:
                print('Invalid input format, cancelling operation ...')
            else:
                print(add(name, number))
            print(" ")
        elif no == '3':
            name = input('Whom to delete from phonebook : ')
            print(delete(name))
            print(" ")
        elif no == '4':
            print('Exiting Phonebook')
            break
        else:
            print('Wrong operation')

        print('1. Find phone number')
        print('2. Insert a phone number')
        print('3. Delete a person from the phonebook')
        print('4. Terminate')
        no = input('Select operation on Phonebook App (1/2/3) : ')



        #2. metod

# This  program creates a phonebook, adds requested contacts to the phonebook, finds them, and removes them.

numdict = {}

print("Welcome to the phonebook application")
print("1.Find phone number")
print("2.Insert a phone number")
print("3.Delete a person from the phonebook")
print("4.Please select 4 to exit")
 

menu = input("Select operation on Phonebook App (1/2/3):")

while True :
    
    if menu == '1':
        first = input("Find the phone number of:")
        if first in numdict:
            print(numdict[first])
            print(" ")
            print('1.Find phone number','2.Insert a phone number','3.Delete a person from the phonebook',
            '4.Please select 4 to exit', sep='\n')
            menu = input("Select operation on Phonebook App (1/2/3):")
        else :
            print("Couldn't find phone number of {}".format(first))
            print(" ")
            print('1.Find phone number','2.Insert a phone number','3.Delete a person from the phonebook',
            '4.Please select 4 to exit', sep='\n')
            menu = input("Select operation on Phonebook App (1/2/3):")
        
    elif menu == '2':
        person = input("Insert name of the person :")
        number = input("Insert phone number of the person :")
        
        if type(person) == str and  number.isdigit() :
            numdict[person] = number
            print("Phone number of {} is inserted into the phonebook".format(person))
            print(" ")
            print('1.Find phone number','2.Insert a phone number','3.Delete a person from the phonebook',
            '4.Please select 4 to exit', sep='\n')
            menu = input("Select operation on Phonebook App (1/2/3):")
        
        else :
            print("Invalid input format, cancelling operation ..")
            print(" ")
            print('1.Find phone number','2.Insert a phone number','3.Delete a person from the phonebook',
            '4.Please select 4 to exit', sep='\n')
            menu = input("Select operation on Phonebook App (1/2/3):")
            
    elif menu == '3':
        ex = input("Whom to delete from phonebook:")
        if ex in numdict:
            del numdict[ex]
            print("{} is deleted from the phonebook".format(ex))
            print(" ")
            print('1.Find phone number','2.Insert a phone number','3.Delete a person from the phonebook',
            '4.Please select 4 to exit', sep='\n')
            menu = input("Select operation on Phonebook App (1/2/3):")
        else :
            print("{} is not found, cancelling operation ..".format(ex))
            print(" ")
            print('1.Find phone number','2.Insert a phone number','3.Delete a person from the phonebook',
            '4.Please select 4 to exit', sep='\n')
            menu = input("Select operation on Phonebook App (1/2/3):")
            
    elif menu == '4':
        print("Exiting Phonebook. BYE!")
        break

    else:
        print("Invalid input format! Please input a valid value...")
        print(" ")
        print('1.Find phone number','2.Insert a phone number','3.Delete a person from the phonebook',
        '4.Please select 4 to exit', sep='\n')
        menu = input("Select operation on Phonebook App (1/2/3):")        