s1 = "virat"
s2 = "anushkha"
s3 = ""
n = len(s1)//2
for i in range(n):
    s3 = s3+s1[i]
s3 = s3+s2

for i in range(n, len(s1)):
    s3 = s3+s1[i]
print(s3)
