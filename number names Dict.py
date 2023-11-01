digits={
    '1':'one ',
    '2':'two ',
    '3':'three ',
    '4':'four ',
    '5':'five ',
    '6':'six ',
    '7':'seven ',
    '8':'eight ',
    '9':'nine ',
    '0':'',
}

tens={
    '1':'ten ',
    '2':'twenty ',
    '3':'thirty',
    '4':'fourty ',
    '5':'fifty ',
    '6':'sixty ',
    '7':'seventy  ',
    '8':'eighty ',
    '9':'ninety ',
    '0':'',
}

number=input("enter number")
output=''
count=-1
place=0
flag=0
for x in number:
    if count==-1:
        output=digits[number[count-place]]+output
        count=count-1
    elif count==-2:
        output=tens[number[count-place]]+output
        count=count-1
    elif count==-3:
        if int(x)!=0:
            output=f'hundred and '+output
        output=f'{digits[number[count-place]]}'+output
        count=count-1
    elif count==-4:
        if int(x)==0:
             continue
        elif place>=3 & place<6:
            output=f'million , '+output
        elif place>=6 & place<9:
            output=f'billion , '+output
        elif place>=0 & place<3:
            output=f'thousand , '+output
        output=f'{digits[number[count-place]]}'+output
        count=-2
        place=place+3


print(output)
    

    
