src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [num for n, num in enumerate(src) if num > src[n-1] and n != 0]

print(result)
