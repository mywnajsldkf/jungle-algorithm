T = int(input())

for i in range(T):
    quiz = list(input())
    count = 0
    reward = 0
    for i in quiz:
        if i == 'O':
            reward +=1
            count+= reward
        elif i == 'X':
            reward = 0
    print(count)