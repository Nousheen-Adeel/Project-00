# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0


def main():
    number = float(input("Enter a number you want to see a square: "))

    square = number * number

    print(f"Square of {number} is {square}")

if __name__=='__main__':
    main()    

