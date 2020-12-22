# 행맨 미니 게임 제작
# 기본 프로그램 제작 및 테스트

import time
import csv
import random
import winsound

name = input('What is your name?')  # 유저이름 입력
print('Hi, ' + name, 'Time to play hangman game!')
print()
time.sleep(1)

print('Start Loading...')
print()
time.sleep(0.5)

# CSV 단어 리스트
words = []

# 문제 CSV 파일 로드
with open('word_list.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    # Header skip
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)
q = random.choice(words)
# print(q)

word = q[0].strip()  # 정답단어

guesses = ''  # 추측 단어

turns = 10  # 기회

# 핵심 loop. 찬스가 남아 있는 경우
while turns > 0:
    failed = 0  # 실패 횟수
    for char in word:
        if char in guesses:
            print(char, end=' ')  # 추측단어출력
        else:
            print('_', end=' ')  # 틀린 경우
            failed += 1
    if failed == 0:  # 추측이 성공한 경우
        print()
        print()
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations! The Guesses is correct')
        break
    print()

    #추측 단어 문자 단위 입력
    print()
    # 힌트
    print('Hint : {}'.format(q[1].strip()))
    guess = input('guess a character : ')

    guesses += guess  # 단어 더하기

    if guess not in word:
        turns -= 1
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
        print('Ooops')  # 오류 메시지
        print("You have", turns, "more guesses!")

        if turns == 0:
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print('You hanman game fails. Bye!')
