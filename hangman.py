import pandas as pd
import random

df = pd.read_csv('./words.csv')
word = df.iloc[random.randint(0, len(df))][0].upper()
chances = 7
guess = ""

for i in range(len(word)):
    guess += "_"

guess = list(guess)
for i in range(len(guess)):
    print(guess[i], end=" ")

print()
print()

while (chances > 0):
    letter = input("Enter a letter: ").upper()

    if (len(letter) > 1):
        print("Enter only one charecter.")
        print()
        continue

    if (letter in word):
        for i in range(len(word)):
            if (letter == word[i]):
                guess[i] = letter
    else:
        chances = chances - 1
    
    count = 0
    for i in range(len(guess)):
        if (guess[i] == "_"):
            count = count + 1

        if (i == len(word)-1):
            print(guess[i])
        else:
            print(guess[i], end=" ")

    if (count == 0):
        break
    
    print("Chances Remaining:", chances)
    print()

if (chances == 0):
    print(word)
    print("You Lose")
else:
    print("You Win")