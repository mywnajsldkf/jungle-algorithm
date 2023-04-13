x,y,w,h = map(int, input().split())

distance = 0

if(x > y):
    distance = y
else:
    distance = x

if(distance > w-x):
    distance = w-x

if(distance > h-y):
    distance = h-y

print(distance)