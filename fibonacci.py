fibo=[0,1]
n=int(input("Enter which number you want in the series"))
x=2
for x in range(2,n):
    fibo.append(fibo[x-1]+fibo[x-2])

print(fibo[n-1])
print(fibo)

