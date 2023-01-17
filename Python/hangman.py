# 리스트에 3개 이상의 단어를 추가
# 단어의 길이에 맞게 밑줄 출력
# 사용자로부터 1글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct', 아니면 'Wrong' 출력
# 매번 입력을 받을 때마다 현재까지 맞힌 글자들 표시 (맞히지 못한 글자는 밑줄 출력)
# 정답을 전부 맞추면 "Success" 출력 후 탈출.

print("[HangMan Game]")
from random import *

words = ["apple", "banana", "strawberrry", "melon"]

word = choice(words)

# print("answer :" + word)

Letters = ""


while True:
    succeed = True
    print()
    for w in word:
        if w in Letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("Success")
        break

    letter = input("put a character letter >")
    Letters += letter
    if letter in word:
        print("Correct")
    else:
        print("Wrong")
    
    