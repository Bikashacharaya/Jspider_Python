'''
* * * * * 
* * * *   
* * *     
* *       
* 

'''

n = int(input("Enter any number: "))

for row in range(1, n+1):
    for col in range(n, row-1, -1):
        print("*", end=" ")
    print()
