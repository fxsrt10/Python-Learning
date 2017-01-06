from random import randint

def checknumber(guess,correctnumber):
    if guess == correctnumber:
        input("You win!")
    elif guess > correctnumber:
        guessagain = input("Your guess was to high")
        checknumber(int(guessagain), correctnumber)
    else:
        guessagain = input("Your guess was to low")
        checknumber(int(guessagain), correctnumber)

print("Welcome to the guessing game, type a number and guess what I'm thinking")
guess = input("Type your number")
correct = randint(0,10)
checknumber(int(guess),correct)