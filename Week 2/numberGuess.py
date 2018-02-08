print("Please think of a number between 0 and 100!")
number=input()
lower=0
higher=100
guess=50
while(guess!=number):
    guess=(higher+lower)//2
    print("Is your secret number "+str(guess)+"?")
    response=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if(response=='h'):
        higher=guess
    elif(response=='l'):
        lower=guess
    elif(response=='c'):
        print("Game over. Your secret number was: "+str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
