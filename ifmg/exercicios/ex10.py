s1 = {1,2,3,4}
s2 = {4,5,6}
s3 = {4,5}

print(s1.union(s2))
print(s1.difference(s2))
print(s3.issubset(s2))
print(s1.issuperset(s3))
