# Magic number game!

# I want you to use operators

# equate something



# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.





# We should define/assign number to a variable called magic_number

magic_number = 10



# I need to ask user for input

# I need to check if this input matches a magic_number
guess_count = 0
guess_limit = 3
while True:
    guess = input("Guess what number's in my head ")
    guess_count += 1
    if int(guess) == magic_number:
        print("Wow! You're psychic!! A*")
        break
    elif guess_count == guess_limit:
        print('Game Over...')
        print('Better luck next time')
        break
    else:
        print("Uh-oh, wrong answer!")


# I need to let the user know if the response was write or not

#self five