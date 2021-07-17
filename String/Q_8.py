# Replace Letter in sentence

s1 = 'varun'
s2 = ""
rep = 'v'
replace = 't'

for i in s1:
    if i == rep:
        s2 = s2+replace
    else:
        s2 = s2+i
print(s2)
