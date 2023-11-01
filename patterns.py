n=5
output=''
def patsq():
    for x in range(1,n+1):
        output='x'*n
        print(output)


def rt():
    for x in range(1,n+1):
        output='x'*x
        print(output)


def tr():
    for x in range(1,n+1):
        k=n-x 
        output=' '*(k)+'x'*(x)+'x'*(x-1)
        print(output)


def tr2():
        for x in range(1,n+1):
            k=n-x 
            output=' '*(k)+(f'{x}')*(x)+(f'{x}')*(x-1)
            print(output)



def tr3():
        for x in range(1,n+1):
            k=n-x
            output=' '*k    
            for y in range(x):
                output+=f'{x-y}'
            for z in range(1,x):
                output+=f'{z+1}'
            print(output)
        for x in range(1,n):
            k=n-x
            output=' '*x    
            for y in range(k):
                output+=f'{k}'
                k=k-1
            for z in range(1,n-x):
                output+=f'{z+1}'
            print(output)

list=("1 : square","2 : traingle","3 : right triangle","4 : traingle 2 ","5:diamond", "6:quit")

def menu():
    print(list)


while True:
    try:
            menu()
            choice=int(input("choose option: "))
            if choice==1:
                patsq()
                continue
            elif choice==2:
                tr()
                continue
            elif choice==3:
                rt()
                continue
            elif choice==4:
                tr2()
                continue
            elif choice==5:
                tr3()
                continue
            elif choice==6:
                print('END')
            else:
                print("Invalid option, enter from option 1 to 6!")
                continue
    except:
        print("Invalid character , enter 1 digit numerical value")
        continue
    break              





