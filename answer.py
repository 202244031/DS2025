import random

number = random.randint(1, 100)

print("1~100 사이 숫자 맞추기 게임")
print("기회는 10번입니다.")

count = 0
chance = 10

while count < chance:
    try:
        answer = int(input("1~100 사이의 숫자를 입력하시오: "))
        count += 1

        if answer < number:
            print("더 큰 숫자입니다.")
        elif answer > number:
            print("더 작은 숫자입니다.")
        else:
            print("정답입니다.")
            break
    except ValueError:
        print("1~100 사이의 숫자를 입력하시오")