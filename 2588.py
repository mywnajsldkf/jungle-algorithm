number = int(input())

digit = list(map(int, input()))
digit.reverse()

result = 0

ten = 1

for i in digit:
    result += number * i * ten
    print(number * i)

    ten *= 10

print(result)