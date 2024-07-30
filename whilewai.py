shitass = 1
shitedass = 1
namer = 'Shit'
while shitass <= 3 and shitedass < 5:
    guess = input('guess: ')
    shitass = shitass + 1
    if '9' in guess:
        print('correct!')
        shitedass = 5
if shitass > 3 and shitedass < 5:
    print('oops')
