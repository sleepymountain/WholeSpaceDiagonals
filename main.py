import math
import random
import logging
import os

# Some thing for Ryan
# Asa Kaczynski | 07/2021

def get_numbers():
    # where are we getting the values for length, width, and height? are we using a random function to generate them
    # once this is established we will pass these values to my space diagonal method

    r_length = random.randint(0, 9999)
    r_width = random.randint(0, 9999)
    r_height = random.randint(0, 9999)
    # print("Random Length: " + str(r_length))
    # print("Random Width: " + str(r_width))
    # print("Random Height: " + str(r_height))
    space_diagonal(r_length, r_width, r_height)


def space_diagonal(length, width, height):
    # formula for space diagonal of a rectangular prism
    # d = sqrt l^2 + w^2 + h^
    # assign variable sd as an integer to the base equation
    # then pass sd to the square root function of math to return a value
    sd = math.pow(length, 2) + math.pow(width, 2) + math.pow(height, 2)
    diag = math.sqrt(sd)

    # pass the value of the equation and parameters of the equation to the whole number check method
    whole_num_check(diag, length, width, height)


def whole_num_check(value, length, width, height):
    x = value
    status = 0
    if x - int(x) == 0:
        # first check if whole number
        # if whole number set status to 1 and print values to text file
        # or display the rectangular prism with the values
        found = (str(value) + " is a whole number, a cross sectional diagonal of " + "Length " + str(length) + " | Width " + str(width) + " | Height " + str(height))
        logging.info(' | ' + found)
        status = 1
        # print(found)
    else:
        # print(str(x) + " is not a whole number")
        status = 0


if __name__ == '__main__':
    # start
    if not os.path.exists('log'):
        os.makedirs('log')
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M %p', filename='log/log.txt', level=logging.INFO)
    print("[i] Checking randomly generated rectangular prisms for whole number space diagonals..")
    print("[i] Check log/log.txt for results.")
    print("[!] Close/stop interpreter to stop generating and checking.")
while True:
    get_numbers()

