'''
count vovel in string

i/p: hey you beautiful

o/p: 8

'''
s1 = "hey you beautiful"
count = 0
for i in s1:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count = count+1
print(f"{s1} -> contain {count} vovel")
