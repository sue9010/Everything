from random import *
from re import A

words = ["apple","banana","orange"]
word = choice(words)
print("answer = " + word)
letters = ""
num = 10

while True:
    succeed = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()
    
    if succeed:
        print("Success")
        break

    letter = input("Input letter >")
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("correct")
    else:
        print("wrong")
        num -= 1
        print(f"기회가 {num}회 남았습니다.")
        if num == 0:
            print("Fail. 게임이 종료되었습니다.")
            break
        else:
            continue
        
