# count total number of word in strings

s1 = input("Enter any string: ")
count = 0
for i in s1:
    if i >= 'a' and i <= 'z':
        count = count+1
print(f"{s1} -> {count} ")
