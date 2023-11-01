weight = input("enter weight :")
unit=input("lbs (enter L) or kgs (enter K)? : ")
if unit.lower()=='l':
    print(int(weight)*0.45)
elif unit.lower()=='k':
    print(int(weight)/0.45)
