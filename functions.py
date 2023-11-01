def greet(name="",last=""):
    return f'Hi There {name} {last}'


print(greet(last="ahmed",name='firaas'))

def square(n):
    return n*n
try:
    print(square(6))
except :
    print('invalid value')