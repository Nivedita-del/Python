import random
# this program runs fine in idle
highest = 10
answer = random.randint(1,highest)

print("Please guess a number between 1 and {}: " .format((highest)))
guess = int(input())
if guess != answer:
    if guess< answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("you got it!")
    else:
        print ("not guessed correcly")
else:
    print("u got it the first time")
