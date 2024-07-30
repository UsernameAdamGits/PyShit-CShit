weight = input('How many pounds are you, you fat fuck? ')
chooser = input('(k)g or (p)ounds ')
kilo_weight = int(weight) / 2.205
kilo_weight2 = int(weight) * 2.205
if 'p' in chooser:
    print(kilo_weight)
elif 'k' in chooser:
    print(kilo_weight2)
else:
    print('fuck you')