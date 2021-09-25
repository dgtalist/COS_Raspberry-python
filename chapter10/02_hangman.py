'''chapter10_02.hangman.py v1.0'''


import time
import csv
import random
#import winsound

name = input('What is your name?')
print('Hi, ' + name, 'Time to play hangman game!')
print()
time.sleep(1)

print('Start Loading...')
print()
time.sleep(0.5)

words = []

with open('word_list.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    # Header skip
    next(reader)
    for c in reader:
        words.append(c)

random.shuffle(words)
q = random.choice(words)
#print(q)

word = q[0].strip()

guesses = ''

turns = 10

while turns > 0:
    failed = 0  # 실패 횟수
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1
    if failed == 0:
        print()
        print()
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations! The Guesses is correct')
        break
    print()

    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input('guess a character : ')

    guesses += guess

    if guess not in word:
        turns -= 1
        #winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
        print('Ooops')
        print("You have", turns, "more guesses!")

        if turns == 0:
            #winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print('You hanman game fails. Bye!')
