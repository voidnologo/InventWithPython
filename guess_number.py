import random

guessesTaken = 0

print('Hello! What is your name? :> ')
name = input()

start = 1
end = 1000
guesses_taken = 0
number_of_guesses = 15

number = random.randint(start, end)
print(name + ' , guess a number between ' + str(start) + ' and ' + str(end) + '.')

while guesses_taken < number_of_guesses:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guesses_taken += 1

    if guess < number:
        print('Too low.')
    elif guess > number:
        print ('Too high.')
    else:
        break

if guess == number:
    guesses_taken = str(guesses_taken)
    print('Good Job, ' + name + '! You guessed the number in ' + guesses_taken + ' guesses!')
else:
    print('Sorry, ' + name + '. The number was ' + str(number) + '.')
