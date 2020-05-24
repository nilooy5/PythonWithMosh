def car_game():
    last_command = ""
    while True:
        command = input(">").lower()
        if command == "start":
            if last_command == command:
                print("the car has already started")
            else:
                print("car started...")
                last_command = command
        elif command == "stop":
            if last_command == command:
                print("the car has already STOPPED")
            else:
                print("car stopped.")
                last_command = command
        elif command == "quit":
            break
        elif command == "help":
            print("""
            start to start car.
            stop to stop the car
            quit to quit""")
