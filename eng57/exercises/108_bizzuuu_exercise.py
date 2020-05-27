# Write a bizz and zzuu game ##project



# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'

# write a program that take a number

# prints back each individual number, but

    # if it is a multiple of 3 it returns bizz

    # if a multiple of 5 it return zzuu

    # if a multiple of 3 and 5 it return bizzzzuu


def bizzbuzz(num1, num2):
    for digit in range(1, (int(number) + 1)):
        if digit % (num1*num2) == 0:
            print('bizzzzuu')
        elif digit % num2 == 0:
            print('zzuu')
        elif digit % num1 == 0:
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
        bizzbuzz(bizz, buzz)

    else:
        print("It's a Yes or No question.")
        start = input('Are you ready to play BIZZBUZZ? >>(Y/N)<< ')






#  EXTRA:

#  Make it functional

#  make it so I can it so it can work with 4 and 9 insted of 3 and 5.

    #      make it so it can work with any number!


