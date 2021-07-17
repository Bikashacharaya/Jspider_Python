'''
Output: [2,1,4,3,6,5,8,7,10,9]
'''

print([i-1 if i % 2 == 0 else i+1 for i in range(1, 11)])
