print('Welcome to the test! Get ready!')
print('')
print('')
print('')
print('')
first_name = input('''What's your first name? ''')
last_name = input('''What is your last name? ''')
birth = input('''When were you born? ''')
age = 2024 - int(birth)
feel = input('''How do you currently feel? ''')
super = input('''You are ''' + first_name  + last_name + ''', you are ''' + str(age) + ''' years old, you currently feel ''' + feel + ''', is that correct?''')
if 'Yes' in super:
    print('Thanks!')
elif 'yes' in super:
        print('thanks')
elif 'y' in super:
      print('k')
elif 'No' in super:
      print('Oh my bad, restart the app.')
elif 'no' in super:
      print('oh my bad restart the app')
elif 'n' in super:
      print('restart')
else:
      print('wuh')
namer = 'Shit'


