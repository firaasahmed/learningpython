list=[65,7,34.65,11,34,76,34,45]
largest=list[0]
for x in list[1:]:
    if x>largest:
        largest=x

print(f'largest numbers is {largest}')