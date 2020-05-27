# Write a bizz and zzuu game ##project



# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'

# write a program that take a number

# prints back each individual number, but

    # if it is a multiple of 3 it returns bizz

    # if a multiple of 5 it return zzuu

    # if a multiple of 3 and 5 it return bizzzzuu

def bizzbuzz(bizz, zzuu):
    number = input('Please enter number: ')
    for digit in range(1, (int(number) + 1)):
        if digit%(bizz*zzuu) == 0 & zzuu%bizz == 0:
            print('bizzzzuu')
        elif digit%zzuu == 0:
            print('zzuu')
        elif digit%bizz == 0:
            print('bizz')
        else:
            print(digit)



#  EXTRA:

#  Make it functional

#  make it so I can it so it can work with 4 and 9 insted of 3 and 5.

    #      make it so it can work with any number!

bizzbuzz(2, 4)
