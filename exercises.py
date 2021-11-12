import sys
from math import pow, sqrt, atan, degrees


def ex1():
    print("Exercise 1 - Get the height and width of a right-angled triangle "
          "then work out the degrees of the other two angles\n")
    running = True
    while running:
        try:  # prompt the user to input the height of the triangle - checks if it is positive
            triangle_height = float(input("Please enter the height of the triangle: "))
            triangle_height = check_if_input_is_positive(triangle_height, "height")
            # prompt the user to input the width of the triangle - checks if it is positive
            triangle_width = float(input("Please enter the width of the triangle: "))
            triangle_width = check_if_input_is_positive(triangle_width, "width")
            running = False
        except ValueError as e:
            print(e)
        else:  # calculate the hypotenuse of the triangle and round it to 1dp - prints result to screen
            triangle_hypotenuse = round(sqrt(pow(triangle_height, 2) + pow(triangle_width, 2)), 1)
            print(f"The hypotenuse of the triangle  is {triangle_hypotenuse} cm")
            #  divide height and width to calculate the radian
            radian = atan(triangle_height / triangle_width)
            #  converts radian to degrees 1dp
            degree_of_angle_a = round(degrees(radian), 1)
            print(f"The angle of A is : {degree_of_angle_a}\u0080")
            #  get the degree of the other unknown angle by subtracting right angle by angle A
            degree_of_angle_b = round(90 - degree_of_angle_a, 1)
            print(f"The angle of B is : {degree_of_angle_b}\u0080")


def ex2():  # prompts user for input - then checks if the input is valid
    print("Exercise 2 - Enter a number and display all the fibonacci sequence to that nth")
    user_input = int(input("How many numbers of the fibonacci sequence should be displayed? "))
    user_input = check_if_input_is_positive(user_input, "fibonacci")
    first_number = 0
    second_number = 1
    #  swap numbers to be printed and calculate the sum of the next number in the sequence
    if user_input == 0: return print(0)
    while user_input > 0:
        print_value = first_number
        first_number = second_number
        second_number = print_value + second_number
        user_input = user_input - 1
        if user_input != 0:
            print(print_value, end=', ')
        else:
            print(print_value)
    print("\n")


def ex3():
    print("Enter two integers and calculate their binomial coefficients ")
    running = True
    while running:
        try:  # gets input from the user and checks if it is valid
            n = int(input("Enter the value of integer n: "))
            n = check_if_input_is_positive(n, "binomial_n")
            k = int(input("Enter the value of integer k: "))
            k = check_if_input_is_positive(k, "binomial_k")
            running = check_value_of_k(k, n)
        except ValueError:
            print(ValueError)


def ex4():
    running = True
    shortest_word = ""
    longest_word = ""
    while running:
        try:
            user_input = input("Please input a line of text: ").split()
            if len(user_input) == 0:
                raise IOError("Invalid input")
            for word in user_input:
                if len(shortest_word) == 0 or len(word.casefold()) < len(shortest_word.casefold()):
                    shortest_word = word
                if len(longest_word) == 0 or len(word) > len(longest_word.casefold()):
                    longest_word = word
                print(word)
            running = False
        except IOError as e:
            print(e)
            continue
    print(f"The length of the shortest word '{shortest_word}' is {len(shortest_word)}")
    print(f"The length of the shortest word '{longest_word}' is {len(longest_word)}")


def ex5():
    running = True
    vowels = "aeiou"
    store_occurrence_of_vowels = {}
    while running:
        try:
            user_input = input("Please input a line of text: ")
            if len(user_input) == 0:
                raise IOError("Invalid input")
            print(f"The following line was inputted by the user: \"{user_input}\"")
            for char in user_input.casefold():
                if char in vowels:
                    if char not in store_occurrence_of_vowels:
                        store_occurrence_of_vowels[char] = 1
                    else:
                        store_occurrence_of_vowels[char] += 1
            if not bool(store_occurrence_of_vowels):
                return print("no vowels found in the line of text")
            print(f"visual display of all the vowels found within the text: {store_occurrence_of_vowels}")
            print("The least occurring vowel(s) from the text is; ", end='')
            for occ in store_occurrence_of_vowels:
                if store_occurrence_of_vowels[occ] == min(store_occurrence_of_vowels.values()):
                    print(f"{occ} with {store_occurrence_of_vowels[occ]} occurrences")
            running = False
        except IOError as e:
            print(e)


def ex6():
    listOfNumbers = []
    running = True
    print("Enter a positive integer (- 1 integer to stop adding number to the list )")
    while running:
        try:
            user_input = int(input("Enter next number: "))
            if user_input < 0:
                running = False
                break
            listOfNumbers.append(user_input)
        except ValueError:
            print("Invalid input - Please enter a positive integer")
    bubble_sort(listOfNumbers)


def bubble_sort(listOfNumbers):
    if len(listOfNumbers) == 0:
        print("empty list")
        return
    elif len(listOfNumbers) <= 1:
        print(f"Only one element stored inside the list, which is: {listOfNumbers}")
        return
    print(f"The unsorted list looks like this: {listOfNumbers}")
    running = True
    while running:
        running = False
        for n in range(len(listOfNumbers) - 1):
            if listOfNumbers[n] > listOfNumbers[n + 1]:
                running = True
                temp = listOfNumbers[n]
                listOfNumbers[n] = listOfNumbers[n + 1]
                listOfNumbers[n + 1] = temp
    print(f"The sorted list looks like this: {listOfNumbers}")


def check_if_input_is_positive(user_input, token):
    #  checks if user input is a positive integer = if not prompts user to do so and then returns result
    if user_input < 0:
        running = True
        while running:
            print("Please enter a positive integer")
            user_input = determine_message_to_be_shown(token)
            if user_input > 0.0:
                running = False
    return user_input


def determine_message_to_be_shown(token):
    match token:
        case "height" | "width":
            return float(input(f"Please enter the {token} of the triangle: "))
        case "fibonacci":
            return int(input("How many numbers of the fibonacci sequence should be displayed? "))
        case "binomial_n":
            return int(input("Enter the value of integer n: "))
        case "binomial_k":
            return int(input("Enter the value of integer k: "))
        case "line of text":
            return input("Please input a line of text: ")


def binomial(n, k):
    b = 1
    for i in range(min(k, n - k)):
        b *= n
        b //= i + 1
        n -= 1
    return b


def check_value_of_k(k, n):
    if k > n:
        print("When k > n the value is 0")
        print("This is because the n number must be larger or equal to k")
        running = False
    elif k == 1:
        print(f"The expression simplifies to {n}")
        print(f"In which n is {n} and k is {k}")
        running = False
    elif k == n or k == 0:
        print("The expression simplifies to 1")
        print(f"In which n is {n} and k is {k}")
        running = False
    else:
        result = binomial(n, k)
        print(f"The binomial coefficient of {n} and {k} is : {result}")
        running = False
    return running


def select_exercise():
    # list_of_exercises = [None, ex1, ex2, ex3, ex4, ex5, ex6]
    # running = True
    # while running:
    #     line = input("Select an exercise (0 or 'q' to quit): ")
    #     if line == "0" or line == "q":
    #         running = False
    #     elif len(line) == 1 and "1" <= line <= "6":
    #         list_of_exercises[int(line)]()
    #     else:
    #         print("Invalid input - try again")
    ex6()


if __name__ == '__main__':
    select_exercise()
