
def cube():
    x = input("Enter a number to cube: ")
    print("\n")
    try:
        val = int(x)
        print(val**3)
    except NameError:
        try:
            val = float(x)
            print(val**3)
        except NameError:
            print("Your Input MUST be a number, DUMBASS!!!")
