n = 5
for row in range(1, n+1):
    for spc in range(n, row, -1):
        print("-", end=" ")
    for star in range(row, 0, -1):
        print(spc, end=" ")
    print()
