h, b, c, s = map(int, input().split())
A = h * b * c * s
B = 8 * 1024 * 1024
print(round(A / B, 1), 'MB')
