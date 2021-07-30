n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

storage = a[0]
for i in range(n):
    if a[i] < storage:
        storage = a[i]

print(storage)
