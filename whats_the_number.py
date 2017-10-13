import random

print('-----------------------------')
print('   GUESS THAT NUMBER')
print('-----------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Please guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('Sorry {0}, guess of {1} was too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {0}, guess of {1} was too HIGH.'.format(name, guess))
    else:
        print('Excellent work {0}, you won! It was {1}.'.format(name,guess))

print('Done.')
