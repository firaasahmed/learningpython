command="stop"
print("commands are start,stop or quit")
while True:
    prev=command
    command=input("Enter command : ").lower()
    if command==prev:
        print(f'car is already in {command} mode ')
    elif command=='start':
        print("car started")
    elif command=='stop':
        print("car stopped")
    elif command=='quit':
        print(" you quit the simulation")
        break    
    else:
        print("sorry enter again")

    
    