'''
*           * 
  *       *
    *   *
      *
'''


n = int(input("Enter the number : "))

ls = 1
rs = n*2-1
for row in range(n):
    for col in range(1, n*2):
        if col == ls or col == rs:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    ls += 1
    rs -= 1
    print()
