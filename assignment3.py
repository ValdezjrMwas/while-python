def check_odd_even(number):
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


try:
    user_input = int(input("Enter a number: "))
    check_odd_even(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")
