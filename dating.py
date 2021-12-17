#!/usr/bin/env python3
# Created by: Zack Isingoma
# Created on: 15th,december 2021

def main():
    user_age_as_string = input("Enter your age: ")
    try:
        user_age_as_int = int(user_age_as_string)

        if user_age_as_string <= 25:
            print("Your too young")
        if user_age_as_string >= 45:
            print("Your too old")

    except Exception:
        print("This input was invalid")
    finally:
        print("Thanks for participating ")


if __name__ == "__main__":
    main()
