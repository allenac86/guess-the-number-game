import random

player_name = input('Hello, what is your name?')

secret_number = random.randint(1, 20)

print('Hi ' + player_name + ', I\'m thinking of a number between 1 and 20.')

# the player gets 5 guesses
for guesses_taken in range(1, 6):
    guess = int(input('Take a guess: '))

    if guess > secret_number and guess < 21:
        print('Too high, try again.')
    elif guess < secret_number and guess > 0:
        print('Too low, try again.')
    elif guess < 1 or guess > 20:
        print('Very funny ...')
    else:
        break

if guess == secret_number:
    print('Congratulations, ' + player_name +
          '. You guessed the secret number in ' + str(guesses_taken) + ' guesses.')
else:
    print('You failed to guess the secret number. It was ' +
          str(secret_number) + '.')
