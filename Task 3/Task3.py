#1 Guess the number

import random

n = random.randint(1, 10)

while True:
    g = int(input("Guess: "))
    if g == n:
        print("Correct")
        break
    elif g > n:
        print("High")
    else:
        print("Low")



#2 Word Scramble

import random

w = ['python','java','guvi','selenium','pytest','javascript']
word = random.choice(w)

s = ''.join(random.sample(word, len(word)))
print(s)

while True:
    g = input("Guess: ")
    if g == word:
        print("Correct")
        break
    else:
        print("Wrong")