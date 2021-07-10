result = 0
i = 0
n = int(input())
while True:
    i += 1
    result += i
    if result >= n:
        print(i)
        break
