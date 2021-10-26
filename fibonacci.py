def numb():
    global id
    id = int(input('Enter the number: '))
    if id < 0: 
        print('Wrong Input') 
        numb()
    return int(id)

numb()

f0 = 0
f1 = 1
i = 2

if id == 0: print(0)
elif id == 1: print(1)
else:
    while i <= id:
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        i = i + 1
    print(f2)
