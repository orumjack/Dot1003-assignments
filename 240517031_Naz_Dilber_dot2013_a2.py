def go_left():
    print("There is a wild cat licking his paws. Better to be avoid.")

def go_right():
    print("You find a treasure chest!")
    print("Open it and find some gold coins!")

def idle():
    print("You can't start an adventure by waiting.")
    print("You're boring...")

def start_adventure():
    print("Welcome to the Simple Adventure Game!")
    choice = input(">Please make a choice -> idle, left, right: ")

    if choice == "left":
        go_left()
    elif choice == "right":
        go_right()
    elif choice == "idle":
        idle()
    else:
        print("invalid Input")
        start_adventure() 


start_adventure()