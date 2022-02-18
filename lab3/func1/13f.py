import random
num = random.randint(1, 20)
def guess_game(guess):

    cnt =0

    while num > 0:
        cnt+=1
        if guess == num:
            print("Good job, " + a + "! You guessed my number in "+str(cnt)+" guesses!")
            break
        else:
            if guess < num:
                print("Your guess is too low.")
                print("Take a guess.")
                guess = int(input())
               
            elif guess > num:
                print("Your guess is too high.")
                print("Take a guess.")
                guess = int(input())
            # elif  guess == num:
            #     print("Good job, " + a + "! You guessed my number in "+cnt+"guesses!")
            #     break
               

print ('Hello! What is your name?')
a = input()
print('Well, '+a+', I am thinking of a number between 1 and 20.')
print ('Take a guess.')
guess = int(input())

guess_game(guess)