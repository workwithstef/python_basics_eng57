# Strings

# a way to used apostrophes in a string with single quotes
string_fixed = 'This is Stefan\'s string'  # silly "\" method, wouldn't recommend
print(string_fixed)

# slicing strings
hw = "Hello World!"
print(hw[:5])  # prints 'Hello' from "Hello World!"
print(hw[6:])  # prints 'World!' from "Hello World!"

# strip
white_space = "lot's and lot's of space at the end        "
print(len(white_space))
white_space.strip()  # strip() removes all trailing spaces
print(len(white_space.strip()))

ex_text = "some text here"
print(ex_text.count("e"))  # counts how many instances of "e" in 'ex_text' (=0)
print(ex_text.count("text"))  # counts how many instances of "text" in 'ex_text' (=0)
print(ex_text.count("Text"))  # counts how many "Text" (=0)

print(ex_text.upper())  # returns all uppercase
print(ex_text.lower())  # returns all lowercase
print(ex_text.capitalize())  # returns first character capitalized

print(ex_text.replace("text", "words"))  # replaces "text" with "words"

# exercises
x = 2
y = 5.4
z = str(x) + str(y)
print(z)

x = "2005008001"
type(x)  # returns type of variable
int(x)  # returns integer form
float(x)  # returns float form

print(type(x), int(x), float(x))

# Booleans
a = True
b = False
c = 2
d = 1
print(c==d)  # returns False since c is not equal to d

greeting = "Hi Stefan"
print(greeting.startswith("H"))  # startswith() checks if string starts with specific character
print(greeting.endswith("."))  # endswith() does the opposite; both return True or False

# Lists

my_list = ["hi", 234, True, 567, "stefan"]

my_list[1] = "my"
my_list[2] = "name"
my_list[3] = "is"

print(my_list)
name = my_list.pop()
print(my_list)
my_list.remove("hi")
print(my_list)
my_list.append("Filipe Paiva")
my_list.pop(0)  # removes list entry corresponding to index specified in pop()
print(my_list)