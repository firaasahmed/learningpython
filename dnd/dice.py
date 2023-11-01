import random

dice_roll=None

class classic_dice:
    def dice6():
        first=random.randint(1,6)
        print(f'Dice roll : {first}')
        return first


    def dice8():
        first=random.randint(1,8)
        print(f'Dice roll : {first}')
        return first

    
    def dice12():
        first=random.randint(1,12)
        print(f'Dice roll : {first}')
        return first

    
    def dice16():
        first=random.randint(1,16)
        print(f'Dice roll : {first}')
        return first


    def dice20():
        first=random.randint(1,20)
        print(f'Dice roll : {first}')
        return first
    

class adv_dice:
    def dice6():
        first=random.randint(1,6)
        second=random.randint(1,6)
        print(f'first : {first} , second : {second}')
        return max(first,second)


    def dice8():
        first=random.randint(1,8)
        second=random.randint(1,8)
        print(f'first : {first} , second : {second}')
        return max(first,second)

    
    def dice12():
        first=random.randint(1,12)
        second=random.randint(1,12)
        print(f'first : {first} , second : {second}')
        return max(first,second)

    
    def dice16():
        first=random.randint(1,16)
        second=random.randint(1,16)
        print(f'first : {first} , second : {second}')
        return max(first,second)


    def dice20():
        first=random.randint(1,20)
        second=random.randint(1,20)
        print(f'first : {first} , second : {second}')
        return max(first,second)
    

class dis_dice:
    def dice6():
        first=random.randint(1,6)
        second=random.randint(1,6)
        print(f'first : {first} , second : {second}')
        return min(first,second)


    def dice8():
        first=random.randint(1,8)
        second=random.randint(1,8)
        print(f'first : {first} , second : {second}')
        return min(first,second)

    
    def dice12():
        first=random.randint(1,12)
        second=random.randint(1,12)
        print(f'first : {first} , second : {second}')
        return min(first,second)

    
    def dice16():
        first=random.randint(1,16)
        second=random.randint(1,16)
        print(f'first : {first} , second : {second}')
        return min(first,second)


    def dice20():
        first=random.randint(1,20)
        second=random.randint(1,20)
        print(f'first : {first} , second : {second}')
        return min(first,second)


def ask():
    while True:
        try:
            n=int(input('Choose regular(1) , advantage(2) or disadvantage(-1) : '))
            break
        except:
            print("Invalid input! , Enter 1 , 2 or -1")

    if n==1:
        dice_roll=classic_dice.dice20()
    elif n==2:
        dice_roll=adv_dice.dice20()
    elif n==-1:
        dice_roll=dis_dice.dice20()

    return dice_roll()
        