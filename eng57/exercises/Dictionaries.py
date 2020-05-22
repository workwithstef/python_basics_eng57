print("Let's make a character!")
print(" ")

character = {"Name": " ", "Alias": " ", "Special Ability": " ", "Weakness": " "}

character['Type'] = input("Hero or Villain? ").title()
character['Name'] = input("What is your character's name? ").title()
character['Alias'] = input("What's " + character['Name'] + "'s alias? ").title()
character['Special Ability'] = input("What's " + character['Name'] + "'s special ability? ").title()
character['Weakness'] = input("What's " + character['Name'] + "'s greatest weakness? ").title()

print(" ")
print("Character Details:")
for key, value in character.items():
    print(key, "=", value)
