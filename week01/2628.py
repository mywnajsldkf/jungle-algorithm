from sys import stdin as s

w, h = map(int, s.readline().split())

n = int(s.readline())

width = [w]
height = [h]

for i in range(n):
    a, b = map(int, s.readline().split())
    if(a == 0):
        height.append(b)
    elif(a==1):
        width.append(b)

width.sort()
height.sort()

max_w = width[0]
max_h = height[0]

for i in range(1, len(width)):
    if(width[i]-width[i-1] > max_w):
        max_w = width[i]-width[i-1]

for i in range(1, len(height)):
    if(height[i]-height[i-1] > max_h):
        max_h = height[i] - height[i-1]

print(max_w, max_h)

print(max_w * max_h)