'''
I/P : hey you beautiful
O/p : h$y y$$ b$$$t$f$l
'''
s1 = "hey you beautiful"
for i in s1:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        print('$', end="")
    else:
        print(i, end="")
