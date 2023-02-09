#create a phonebook with the following names and their numbers respectively. print now the phonebook.
#Andrew Parson = 8806336
#Emily Everett = 6784346
#Peter Power = 7658344
#Lewis Lame = 1122345
#do the necessary modifications to the phonebook as follows
# 1. Andrew's number is wrongs update it to 8806334 and show phone book
# 2. add Gingerbread John to phonebook yet he doesn't have any phone number so keep it None and show
# 3. show all the persons
# 4. show all the phonenumbers
# 5. now create addressbook for the users from phonebook


phonebook = {
    'Andrew Parson':8806336,
    'Emily Everett':6784346,
    'Peter Power':7658344,
    'Lewis Lame':1122345
    }

print(phonebook, end='\n\n')

#1. Andrew's number is wrongs update it to 8806334 and show phone book
phonebook['Andrew Parson'] = 8806334
print(phonebook, end='\n\n')

#2. Add the person 'Gingerbread Man' to the phonebook:
phonebook['Gingerbread John'] = None
print(phonebook, end='\n\n')

#3. show all the persons
for person in phonebook.keys():
    print(person)

print()

#4. show all the phonenumbers
for number in phonebook.values():
    print(number)

print()

#5. now create addressbook for the users from phonebook
addressbook = dict.fromkeys(phonebook)
print(addressbook)