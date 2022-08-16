
import random
ans= random.randint(0,20)

#print(ans)

def guess():
    print('Guess a number between 0 and 20')
    innn = input()
    i=1
    while i<6:
        if int(innn) == ans:
            print('You guessed the correct answer in ' + str(i) +' tries')
            break
        elif int(innn) < ans:
            print('Your answer is too low')
            innn = input()
        elif int(innn) > ans:
            print('Your answer is too high')
            innn = input()
        i= i+1
        
guess()
