numbers=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,3,2,1]
unique=[]

for x in numbers:
    if x not in unique:
        unique.append(x)

print(unique)

