# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input())
nums = []
for i in range(n):
    a = int(input())
    nums.append(a)
x = int(input())
min_diff = abs(nums[0]-x)
el = nums[0]
for i in nums:
    if abs(i-x) < min_diff:
        min_diff = abs(i-x)
        el = i
print(el)
