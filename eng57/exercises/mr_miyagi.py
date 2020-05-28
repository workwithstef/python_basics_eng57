# mr Miyagi trainee



# make a mr miyagi virtual assistant



# as a user I should be able to speak with mr miyagi and get appropriate response s as I go



# Ask for user input and depending on the response, mr Miyagi will respond.

#

# prompt user for input

# Evaluate each input and print the appropriate responses
def miyagi_response():
    if question.endswith('?'):
        print('Mr Miyagi: Questions are wise, but for now. Wax on, and Wax off!')
    elif not question.startswith("Sensei"):
        print('Mr Miyagi: You are smart, but not wise - address me as Sensei please')
    elif question.count('block') >= 1:
        print('Mr Miyagi: Remember, best block, not to be there..')
    else:
        print('Mr Miyagi: Do not lose focus. Wax on. Wax off.')


while True:
    question = input("Me: ")
    if question == 'Sensei, I am at peace.':
        print('Mr Miyagi: Sometimes, what heart know, head forget')
        break
    miyagi_response()


