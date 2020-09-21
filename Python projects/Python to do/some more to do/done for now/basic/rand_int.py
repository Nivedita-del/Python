import random
# works fine in idle
i=0
highest = 10
answer = random.randint(1,highest)

print("Please guess a number between 1 and {}: " .format((highest)))
guess = int(input())
while i != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        break

print("you got it!")


