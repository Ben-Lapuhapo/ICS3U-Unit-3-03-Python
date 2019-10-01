#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: September 30 2019
# This program is a guessing game

import random

random_number = (random.randint(0,8+1)) # a number between 0 and 9


def main():
    # input
    print("")
    user_input = int(input("Please enter a number from (0-9) : "))
    print("")

    # Process and Output
    if user_input > 9:
        print("Number Too High. Enter a Number from (0-9) only.")
    elif user_input == random_number:
        print("Correct Number!! ----->", random_number)

    else:
        print("Sorry Wrong Number, The Correct Number is:", random_number)
        print("")
        restart = input("Restart? Enter Y or N --->")
        if restart == "Y" or "y":
            print("OK")
            main()
            
if __name__ == "__main__":
    main()
