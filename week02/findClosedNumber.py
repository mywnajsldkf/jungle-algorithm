a = [1, 4, 5, 9, 10, 11, 11, 3]
a.sort()    # 이진탐색을 하려면 정렬해야 한다.
print(a)
def binary_search(numbers, key):
    left = 0
    right = len(numbers)-1

    while left <= right:
        middle = (left + right) // 2

        if key == numbers[middle]:
            print(middle)
            return middle
            break
        elif key < numbers[middle]:
            right = middle -1
        elif key > numbers[middle]:
            left = middle + 1

    # Not key in the list
    if right == -1:
        print(numbers[0])
    elif left == len(a):
        print(numbers[len(a)-1])
    else:
        prev_num = numbers[left-1]
        next_num = numbers[right+1]

        prev_step = abs(key - prev_num)
        next_step = abs(key - next_num)

        if prev_step == next_step:
            print(prev_num, next_num)
        elif prev_step > next_step:
            print(next_num)
        elif prev_step < next_step:
            print(prev_num)

binary_search(a, 8)