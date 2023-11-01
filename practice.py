lists=[[True,True,True,False,False],
       [True,True,False,False,False],
       [True,True,True,True,True],
       [True,True,True,True,False],
       [True,True,True,False,False],
       [True,True,False,False,False],
    ]

final=[]
for x in lists:
    count=0
    t=0
    for y in x:
        count=count+1
        
        if y == True:
            t+=1

    final.append(t/count)

print(final)
    
        
