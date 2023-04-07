max = 1

count = 1
for i in range(1,10):
    now = int(input())

    if(max < now):
        max = now
        count = i

print(max)
print(count)