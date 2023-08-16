# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Main routine goes here

# Introduction / heading print statements
print()
print("- Area Perimeter Calculator -")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area (width x height)
    area = width * height

    # Calculate perimeter (width + height) x 2
    perimeter = 2 * (width + height)

    # Output are and perimeter up to 2 dp
    print("Perimeter {:.2f} units" .format(perimeter))
    print("Area: {:.2f} square units" .format(area))

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter calculator!")
