started = False
stopped = False
while True:
    command = input(">").lower()
    if command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
            ''')
    elif command == 'start':
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started...Ready to go")
    elif command == 'stop':
        if stopped:     
            print("Car already stopped!")
        else:
            stopped = True
            print("Car stopped ")
    elif command == 'quit':
        exit()
    else:
        print("I don't understand")