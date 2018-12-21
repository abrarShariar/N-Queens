i, j = 1, 2

N = 4

# for row left
# for y in range(j):
#     print(i, y)

# for diagonal top left
# for x,y in zip(range(i, -1, -1), range(j, -1, -1)):
#     print(x, y)

# for diagonal bottom left
for x,y in zip(range(i, N, 1), range(j, -1, -1)):
    print(x, y)
