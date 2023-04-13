import sys
C = int(sys.stdin.readline())

for i in range(C):
    students = list(map(int, sys.stdin.readline().split()))
    number = students.pop(0)

    score = sum(students)
    avg = score / number

    count = 0
    for i in students:
        if i > avg:
           count += 1

    # print(str(f'{count/number*100: .3f}%'))
    print(f"{format(count/number*100, '.3f')}%")