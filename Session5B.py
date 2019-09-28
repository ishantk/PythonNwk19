# Whatever we write in out python file/script it gets executed in a sequence
# i.e. line by line

# In our program all the instructions are part of main thread
# i.e. they will be executed by main thread in a sequence :)

# main function in python
def main():
    print(__name__)  # __main__

    # When we print the name we get output as main

    print(">> This is Instruction1")
    print(">> This is Instruction2")
    print(">> This is Instruction3")

if __name__ == "__main__":
    main()