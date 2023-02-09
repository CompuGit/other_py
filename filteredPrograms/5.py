#WAP to get a input number and verify it is valid or not
#valid if it starts with 9,8,7,6 and having exactly 10 digits
num = input('Enter a Phone Number : ')

if len(num)==10 and (num[0] == '9' or '8' or '7' or '6'):
    print('It is a valid number.')

else:
    print('It is a spam number.')
