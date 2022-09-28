#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/09/28
# Takes user input for the diameter and calculates a pizza cost

# importing the HST constant in the constants.py file
import constants


def main():
    # variables
    labour_cost = 2
    rental_cost = 2.25
    ingredients = 1.5

    # title
    print("// " "--.._")
    print("||  (_)  _ -._")
    print("||    _ (_)    '-.")
    print("||   (_)   __..-'")
    print("\\__..--" "")
    print("Pizza Cost")
    diameter = int(input("Enter the diameter of your pizza (cm): "))

    # calculation
    cost = labour_cost + rental_cost + (ingredients * diameter)
    tax = cost * constants.HST
    total = cost + tax

    # display the calculation back to the user
    print("Your pizza will cost ${}!".format(total))


if __name__ == "__main__":
    main()
