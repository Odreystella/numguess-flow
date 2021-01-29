
#ver1.0.0

import random

answer = random.randint(1,20)
print(answer)
guess = int(input("Enter the number: "))
print(guess)

if guess-answer == 0:
    print("정답입니다.")
else:
    print("오답입니다.")
