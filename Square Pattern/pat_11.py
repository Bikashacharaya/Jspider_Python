'''
* * * * *
* * *   *
* * * * *
*   * * *
* * * * *


'''
n = int(input("Enter any number: "))

for row in range(1, n+1):
    for col in range(1, n+1):
        if row*col == n+3:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
