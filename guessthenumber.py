#This code imports the random range
import random

#Sets variable to 0
guesses_made = 0

#Asks user their name and stores it as "name"
name = input('Hello! What is your name?\n')

# set variable to random interger between 1 and 20
number = random.randint(1, 20)

#Print text
print ('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))


while guesses_made < 6:

    guess = int(input('Take a guess: '))

    guesses_made += 1

    if guess < number:
        print ('Your guess is too low.')

    if guess > number:
        print ('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    print ('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
else:
    print ('Nope. The number I was thinking of was {0}'.format(number))