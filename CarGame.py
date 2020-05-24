command = ""
lastCommand = ""
while True:
    command = input(">").lower()
    if command == "start":
        if lastCommand == command:
            print("the car has already started")
        else:
            print("car started...")
            lastCommand = command
    elif command == "stop":
        if lastCommand == command:
            print("the car has already STOPPED")
        else:
            print("car stopped.")
            lastCommand = command
    elif command == "quit":
        break
    elif command == "help":
        print("""
        start to start car.
        stop to stop the car
        quit to quit""")
