# Ask the user for their response and loop until they
# enter a number that is more than zero
def int_check(question, low):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))
            # check that the number is more than low
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# calculates how many bits are needed to represent an integer
def image_calc():
    # Retrieves image dimensions
    width = int_check("Width: ",  1)
    height = int_check("Height: ", 1)

    # calculates the number of pixels and number
    # of bits by multiplying by 24
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it
    answer = (f"\nNumber of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer

# main routine goes here
image_ans = image_calc()
print(image_ans)
