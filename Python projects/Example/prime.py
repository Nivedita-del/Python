import random
guesses_made = 0
name = (input('Hello! What is your name?\n'))

print('Well, {0}, I am thinking of a number between 1 and20.'.format(name))
while guesses_made < 6:
    number = random.randint(1, 20)
    guess = int(input('Take a guess: '))
    guesses_made += 1
    if guess < number:
        print ('Your guess is too low.')
    if (guess > number):
        print ('Your guess is too high.')
    if guess == number:
        break
    if guess == number:
        print ('Good job, {0}! You guessed my number in {1}guesses!'.format(name, guesses_made))
    else:
        print ('Nope. The number I was thinking of was {0}'.format(number))
