# functions go here
def statement_generator(statement, decoration):
    print(f"\n\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions Of Use", "-")

    print('''
Please select file type:
'integer', 'int' for Integer
'image', 'picture', 'img', 'p' for Image
'text', 'txt', 't' for Text
Or enter 'xxx', 'i' to cancel
    ''')



# asks users for file type (integer / image / text / xxx)
def get_filetype():

    while True:
        response = input("\nFile type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check for an image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check for text
        elif response in ['text', 'txt', 't']:
            return "text"

        # if response is invalid
        else:
            print("Please enter a valid file type")


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

    # calculates the number of pixels and number of bits by multiplying by 24
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it
    answer = (f"\nNumber of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# calculates how many bits are required to represent an integer
def integer_calc():
    # Ask the user to enter an integer (more than / equal to 0)
    integer = int_check("Integer: ", 0)

    # convert the integer to binary and calculate the number of bits needed
    raw_binary = bin(integer)

    #remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # Set up answer and return it
    if integer == 21:
        print('\nU stoopid\n')
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."

    return answer

# Calculates number of bits needed to represent text in ascii
def calc_text_bits():
    # Get text from user
    response = input("Enter some text: ")

    if response == "no":
        print("\nToo bad")
        print("So sad")


    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"\n{response} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it "
              f"\nwhich is {num_bits} bits.")

    return answer



# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()



while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # if user chose 'i', ask if they want image or integer
    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        elif want_image == 'integer':
            file_type = "integer"
        elif want_image == 'int':
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)

