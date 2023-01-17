import random 

# user guesses num
def guess(x):
    # chooses a random int between 1 and x
    rando_num = random.randint(1, x)
    # give guess an initial value that is bound to be incorrect to start loop
    guess = 0
    #  while loop starts when your guess doesnt match
    while guess != rando_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > rando_num:
            print("Guess again! Your number is too high")
        elif guess < rando_num:
            print("Guess again! Your number is too low") 
    # while loop breaks when you've guessed correct
    print(f"Congrats, you've guess correctly! the number was {rando_num}")           



guess(10)    
   
# comp guesses num
def comp_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess}, too High (H), too Low (L), or Correct(C): ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay, the computer, guessed your number {guess}, correctly! ")

comp_guess(200)
      


