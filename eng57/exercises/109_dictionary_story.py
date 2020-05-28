# Dictionary basics :D



#1 - Define a dictionary call story1, it should have the followign keys:

        # 'start', 'middle' and 'end'

story1 = {'start': 'Long ago in a galaxy far far away ', 'middle': '"That\'s no moon!" ', 'end': 'I am your father. '}

#2 - Print the entire dictionary

print(story1)

#3 - Print the type of your dictionary

# print(type(story1))
# # print(type(story1['start']))
# #4 - Print only the keys
# print(story1.keys())
# #
# #
# # #4 - print only the values
# #
# print(story1.values())
#
# print(type(story1.keys()))
#
# for key in story1.keys():
#     print(key)
# # #5 - print the individual values using the keys (individually, lots of printi commands)
# print(story1['start'])
# print(story1['middle'])
# print(story1['end'])
# #
# #
# # #6 - Now let's add a new key:value pair.
# #
#     # 'hero': yourSuperHero
# story1['hero'] = 'Anakin Skywalker'
#
# print(story1)

# for item in story1.keys():
#     print(item)

# this one is more idomatic and make more sense - hence better
for key in story1.keys():
    print(key)
    print(story1[key])

for key in story1:
    print(key)
    print(story1[key])