name = input("what is your name ")

if len(name) < 4:
    print('name must be bigger than 3 letters')
elif len(name) > 50:
    print('name can only be maximum of 50 letters')
else:
    print('your name is' + name)