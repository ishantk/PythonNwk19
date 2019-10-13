num = 10  # Global Variable

def update():

    global num # this will use global num in update function and will not re-create a new num for update function

    # num = num % 3 # Local Variable : A new container num will be created in update function
    num = 7
    print(">> 1. num is:", num)

update()

print(">> 2. num is:", num)

