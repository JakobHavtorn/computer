import struct


# TODO Custom data type / class for bit?


def int2binary(integer: int, precision: int):
    return bin(integer)[2:].zfill(8)


def binary2int(binary: str):
    """Convert binary representation of integer as a string to an integer type"""
    return int(binary, 2)


def float2binary(number, precision: int):
    """Convert float to binary
    
    https://ryanstutorials.net/binary-tutorial/binary-floating-point.php
    """
    sign_bit = 1 if number < 0 else 0
    whole, dec = str(number).split(".")
    whole_bit = bin(int(whole))



# # Function returns octal representation
# def float2binary(number, places = 3):

#     # Function converts the value passed as
#     # parameter to it's decimal representation
#     def decimal_converter(num):
#         while num > 1:
#             num /= 10
#         return num
 
#     # split() separates whole number and decimal
#     # part and stores it in two separate variables
#     whole, dec = str(number).split(".")
 
#     # Convert both whole number and decimal 
#     # part from string type to integer type
#     whole = int(whole)
#     dec = int (dec)
 
#     # Convert the whole number part to it's
#     # respective binary form and remove the
#     # "0b" from it.
#     res = bin(whole).lstrip("0b") + "."
 
#     # Iterate the number of times, we want
#     # the number of decimal places to be
#     for x in range(places):
 
#         # Multiply the decimal value by 2
#         # and separate the whole number part
#         # and decimal part
#         whole, dec = str((decimal_converter(dec)) * 2).split(".")
 
#         # Convert the decimal part
#         # to integer again
#         dec = int(dec)
 
#         # Keep adding the integer parts
#         # receive to the result variable
#         res += whole
 
#     return res


def binary2utf8(binary: str):
    """Convert binary representation of a string to UTF-8"""
    # TODO
    pass


def utf8tobinary(string: str, precision: int):
    """Convert UTF-8 representation of a string to binary"""
    '{:b}'.format(int(string.encode('utf-8').encode('hex'), precision))