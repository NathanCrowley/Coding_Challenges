'''
1/10/20 - Nathan Crowley
This is a program to convert Hexadecimal to Binary in python.

A9 -> Binary
A = 10 in decimal
B = 11
C = 12
D = 13
E = 14
F = 15

A9 -> 10 , 9
10 ->   1010
9 - >   1001
A9 = 10101001
'''
import sys


def hex2binary():
    # message to be printed on completion of the program
    program_finish = "\n*** Program closed ***\n"
    # error message
    error_msg = "\n\t ERROR - Invalid user input - Hexidecimal: 0-F"
    hex_digits = "123456789ABCDEFabcdef"
    # get the users hex
    user_hex = input("\n>>>Enter Hex value to be converted to Binary [ENTER to exit]: ")
    # error checking
    for digit in user_hex:
        if digit not in hex_digits:
            sys.exit(error_msg)
    # let user exit if they press enter.
    if user_hex == "":
        sys.exit(program_finish)
    # Once user_hex passes the above checks, convert hex to decimal
    user_dec = int(user_hex, 16)
    # convert decimal to binary
    user_binary = ""
    while user_dec > 0:
        user_binary += str(user_dec % 2)
        user_dec = user_dec // 2
    # flip the string of bits (they are to be read in reverse)
    user_binary = user_binary[::-1]
    # output answer
    print("\t\t{} Hex = {} Binary.\n".format(user_hex.upper(), user_binary))


# -----------------Run function---------------
while True:
    hex2binary()
