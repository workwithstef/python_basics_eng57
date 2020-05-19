box_variable = 'Hello hi'
another_box = 5

# type() prints out variable type
print(type(box_variable))
print(type(another_box))

favourite_colour = 'Blue'
best_team_in_the_world = 'Chelsea FC'

print(favourite_colour + " is the colour, football is the game... 'cause "
        + best_team_in_the_world + ', ' + best_team_in_the_world + ' is our name!!')

first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
digits = input("What's your number? ")

age = input("How old are you? ")
date_of_birth = input("When's your birthday? (dd/MM/yy) ")

full_name = first_name + ' ' + last_name

print(type(age))

age_int = int(age)
print(type(age_int))

sentence = full_name + ' is '+ age + ' years old. '+ first_name + ' was born on '+ date_of_birth + '.'
print(sentence)
