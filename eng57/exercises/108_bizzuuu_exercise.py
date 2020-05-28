# Write a bizz and zzuu game ##project



# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'

# write a program that take a number

# prints back each individual number, but

    # if it is a multiple of 3 it returns bizz

    # if a multiple of 5 it return zzuu

    # if a multiple of 3 and 5 it return bizzzzuu
def check_if_digit_div_num(digit, num_div):
    if digit % num_div == 0:
        return True
    else:
        return False

def bizzbuzz(num1, num2, number):
    for digit in range(1, (int(number) + 1)):
        if check_if_digit_div_num(digit, num1) and check_if_digit_div_num(digit, num2):
            print('bizzzzuu')
        elif check_if_digit_div_num(digit, num2):
            print('zzuu')
        elif check_if_digit_div_num(digit, num1):
            print('bizz')
        else:
            print(digit)




start = input('Are you ready to play BIZZBUZZ? (Y/N) ')
while True:
    if start.upper() == 'N':
        print('Maybe next time...')
        break

    elif start.upper() == 'Y':
        number = input('Please enter number: ')
        if number == 'penpinapplespen':
            break
        bizz = int(input('Choose your BIZZ: '))
        buzz = int(input('Choose your ZZUU: '))
        bizzbuzz(bizz, buzz, number)

    else:
        print("It's a Yes or No question.")
        start = input('Are you ready to play BIZZBUZZ? >>(Y/N)<< ')






#  EXTRA:

#  Make it functional

#  make it so I can it so it can work with 4 and 9 insted of 3 and 5.

    #      make it so it can work with any number!


