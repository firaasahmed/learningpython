for item in range(5,15,2):
    print(item)
for item in ['firaas','nibras','nabiha']:
    print(item)

sum=0
for item in [10,20,30]:
    sum=sum+item

print(f'sum is {sum}')
numbers=[5,2,5,2,2]
print(len(numbers))


n = int(input("enter n"))

for x in range(1,n+1):
    output=''
    k=int(n)-x
    for y in range(x):
        output= ' '*(int(k)) + 'x'*x +'x'*(x-1)
    print(output)