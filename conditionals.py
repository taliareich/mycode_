#!/usr/bin/env python3
'''TReich | Alta3Research 
   Simple guessing game using if-elif-else'''

# assign secret number variable
secret_num = 42

# collect user guess
guess = int(input("What's the magic number? "))

# evaluate if guess is equal to secret number
if secret_num == guess:
    print("Correct!")

# evaluate if guess is within +/-5 of secret number
elif secret_num-5<guess<secret_num+5:
    print("Almost!")

# catchall condition
else:
    print("Sorry :( that's wrong")



