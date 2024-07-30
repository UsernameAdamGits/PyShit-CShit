command = ""
is_car_up = False
namer = 'Shit'
while True:
    command = input('> ').lower()
    if command == "start" and is_car_up is False:
        print('car started')
        is_car_up = True
    elif command == "start" and is_car_up is True:
        print('car is already running dumbfuck')
    elif command == "stop" and is_car_up is True:
        print('car stopped')
        is_car_up = False
    elif command == "stop" and is_car_up is False:
        print('car is already stopped dumbfuck')
    elif command == "help":
        print(""" 
start - to start the car
stop - to stop the car
quit - to exit
""")
    elif command == "quit":
        break
    else:
        print('i dont understand...')