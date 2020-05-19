# DEFINE THE FOLLOWING VARIABLES
# first_name, last_name, age, eye_color, hair_color
# first_name = ''
# last_name = ''
# eye_color = ''
# hair_color = ''
# age = ''
# Prompt user for input and Re-assign these

first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
age = input("How old are you? ")
bday_soon = input("Has it been your birthday yet this year? (Y/N) ")

full_name = first_name + ' ' + last_name

print(type(age))
age_int = int(age)
print(type(age_int))

if bday_soon.upper() == 'N':
    birth_year = 2019 - age_int
else:
    birth_year = 2020 - age_int

sentence = full_name + ' is ' + age + ' years old. ' \
           + "Since you're " + age + ", you were born in " + str(birth_year) + "."
print(sentence)

# Calculate birthyear
# Cast your input