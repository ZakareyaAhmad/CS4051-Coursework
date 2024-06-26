# CS4051 Coursework: Statistical Calculator
# The code serves as a calculator, allowing the input of numbers and providing functions to calculate the mean, median, mode, and skewness of the data. 
# Author: Zakareya Ahmad
# Date: 14/04/2024

def mean(numbers): # This line defines a function (using def) named mean that calculates the arithmetic mean of a list of numbers using parameter numbers
    return sum(numbers) / len(numbers) if numbers else None # This line returns the arithmetic mean of the inputted list of numbers if it's not empty, otherwise, it returns None.

def median(numbers): # This line defines a function (using def) named median that calculates the arithmetic median of a list of numbers
    sorted_numbers = sorted(numbers) # Assigns the list of numbers to the variable sorted_numbers and places it in ascending order
    n = len(sorted_numbers) # Assigns the list of numbers to the variable n and gets the amount of numbers there are
    if n % 2 == 0: # Thid checks to see if the length of the sorted lsit of numbers is even
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2 # Calculates the average of the two middle numbers if the length of the list is even.
    else: # If the length of the list is odd
        return sorted_numbers[n // 2] # Returns the middle element of the list if its length is odd
    
def mode(numbers): # This line defines a function (using def) named mode that calculates the arithmetic mode of a list of numbers using a paramter named numbers
    occurrences = {} # Creates a dictionary named occurrences to store the frequency of each number
    for num in numbers: #Iterateion over each number within the list
        occurrences[num] = occurrences.get(num, 0) + 1 # Updates the number of occurrences for the current number in the dictionary
                                                       # If the number is not in the dictionary, its count is set to 1.
    max_count = max(occurrences.values()) # Find the most occurrunces amongst the numbers
    modes = [num for num, count in occurrences.items() if count == max_count] # Creates a list of the numbers with the most amount of occurences
    return modes # Returns the previous list

def skewness(numbers): # This line defines a function (using def) named skewness that calculates the arithmetic skewness of a list of numbers
    val_mean = mean(numbers) # Calculates the mean of the numbers inputted using the previous function
    if val_mean is None: # Checks if rhe mean value is None, seeing if the input list is empty
        return None # Returns None
    n = len(numbers) # Assigns the list of numbers to the variable n and gets the amount of numbers there are
    squared_distances = [(x - val_mean) ** 2 for x in numbers] # Calculates the squared distance of each number from the mean value
    sum_squared_distances = sum(squared_distances) # Calculates the sum of the squared distance from the mean value
    variance = sum_squared_distances / n # Calculates the variance by dividing the sum of the squared distance by the number of elements
    standard_deviation = variance ** 0.5 # Caclulates the standard deviation by taking the square root of the variance
    val_skewness = sum((x - val_mean) ** 3 for x in numbers) / (n * standard_deviation ** 3) # Calculate the skewness of the input list of numbers using the provided formula
    return val_skewness # Returns the skewness

def read_numbers_from_file(file_name): # This line defines a function (using def) named read_numbers_from_file that reads the numbers from a file using a parameter named file_name
    try: # Attempts to execute the following code 
        with open(file_name, 'r') as file:  # Open the file in read mode
            lines = file.readlines()  # Read all lines from the file
            numbers = []  # make an empty list to store the marks
            for line in lines:  # Go through each line in the file
                # Split each line by commas, strip whitespace from each mark, and convert them to floats
                numbers.extend([float(num.strip()) for num in line.split(',')])
            return numbers  # Return the list of marks read from the file
    except FileNotFoundError: # Handles any errors that occurs
        print("Error: File not found.")  # Handles file not found error
        return [] # Returns an empty list
    except Exception as e: # Catches any exceptions and assigns it to the variable e
        print("An error occurred:", e)  # Handle any other exceptions
        return []  # Return an empty list


def main(): # Uses def to define the main function that is responsible for carrying out the code
    numbers = [] # Generates an empty list named numbers to store any numbers that are inputted
    while True: # Starts an infinite loop until the user exits the program
        print("\nEnter a student's mark (if you have finished inputting, please type 'FINISHED'):") # Prints out a set of instructions for the user to complete
        user_input = input().strip() # Gets the inputted numbers and assigns it the variable user_input
        if user_input.lower() == 'finished': # Check if the user has inputted FINISHED 
            break # Exits the loop if the user has inputted FINISHED
        if ',' in user_input: # Checks for a comma in the inputted code
            try: # Attempts to execute the following code
                numbers.extend([float(num) for num in user_input.split(',')]) # Seprarates the inputted numbers and converts each one to a float
            except ValueError: # Deals with any invalid data 
                print("INVALID: Please enter valid numbers separated by commas.") # Prints an error message
        else: # Alternative if the input is a single number and does not contain any commas
            try: # Attempts to execute the following code
                number = float(user_input) # Assigns it the variablee number and converts it to a float
                numbers.append(number) # Adds the input to the numbers list
            except ValueError: # Deals with any invalid data 
                print("INVALID: Please enter a valid number.") # Prints an error message

    print("\nTotal numbers inputted:", len(numbers)) # Prints the total number of numbers inputted by using the length of the numbers list
    if len(numbers) < 2: # Checks to see if the length of the list is less than two
        print("A minimum of two numbers are required to conduct any calculations.") # Prints an error message
        return # Exits the function

    while True:# Starts an infinite loop until the user exits the program 
        print("\n(1) Print the mean") # Prints the option to calculate the mean
        print("(2) Print the median") # Prints the option to calculate the median
        print("(3) Print the mode") # Prints the option to calculate the mode
        print("(4) Print the skewness") # Prints the option to calculate the skewness
        print("(5) Enter more numbers") # Prints the option to add more numbers
        print("(6) Read data from a file") # Prints the option to read the data from a file 
        print("(7) Exit the application") # Prints the option to exit the application
        print("(8) Enter new numbers") # Prints the option to enter new numbers
        choice = input("\nEnter your choice: ").strip() # Makes the user enter their option, assigining it to the variable choice

        if choice == '1': # Checks to see if the user has selected 1
            val_mean = mean(numbers) # Calculates the value of the mean using the previous mean function
            if val_mean is not None: # Checks to see if the value of the mean is not None
                print("\nMean:", val_mean) # Prints the value of the mean
            else: # Situation where mean is equal to None
                print("INVALID: No numbers entered.") # Prints an error message
        elif choice == '2': # If the user selected 2
            if numbers: # Checks to see if the numbers list is not empty
                print("\nMedian:", median(numbers))# Prints the value of the median
            else: # Situation where mean is equal to None
                print("INVALID: No numbers entered.") # Prints an error message
        elif choice == '3': # If the user selected 3
            if numbers: # Checks to see if the numbers list is not empty
                print("\nMode:", mode(numbers)) # Prints the value of the mode
            else:  # Situation where mean is equal to None
                print("INVALID: No numbers entered.") # Prints an error message  
        elif choice == '4': # If the user selected 4
            if numbers: # Checks to see if the numbers list is not empty 
                val_skewness = skewness(numbers) # Caclulate the value of the skewness using the previous function and assign it to the variable
                if val_skewness is not None: # Checks to see if the value of the skewness is not None 
                    print("\nSkewness:", val_skewness) # Prints the value of the skewness
                else: # Situation where mean is equal to None
                    print("Cannot calculate skewness with less than two numbers.") # Prints an error message
            else: # Situation where mean is equal to None
                print("INVALID: no numbers entered.") # Prints an error message 
        elif choice == '5': # If the user selected 5
            while True: # Starts an infinite loop until the user exits the program
                print("\nEnter additional student marks separated by commas (if you have finished inputting, please type 'FINISHED'):") # Prints option to allow for more numbers to be input
                user_input = input().strip() # Get user input from the console and assign it to the variable
                if user_input.lower() == 'finished': # Check if the user has inputted FINISHED 
                    break # Exits the loop if the user has inputted FINISHED
                try: # Attempts to execute the following code 
                    numbers.extend([float(num) for num in user_input.split(',')]) # Converts each number to a float and makes the list longer with these extra numbers
                except ValueError: # Deals with any invalid data  
                    print("INVALID: please enter valid numbers separated by commas.") # Prints an error message 
        elif choice == '6': # If the user selected 6
                file_name = input("Enter the file name: ")  # Get the file name from the user
                marks = read_numbers_from_file(file_name)  # Read marks from the file
                print("\nNumbers obtained from file: ", marks)  # Print marks from the file
        elif choice == '7': # If the user selected 7
            print("\nExiting the application. Goodbye!") # Prints an exitiing message
            break # Exits the loop if the user has inputted FINISHED 
        elif choice == '8':  # Handling the case when the user wants to add new numbers, erasing the previous numbers
            numbers.clear()  # Clears the previous numbers
            while True: # Starts an infinite loop
                print("\nEnter new numbers separated by commas (if you have finished inputting, please type 'FINISHED'):") # Prints option to enter new numbers
                user_input = input().strip() # Get user input from the console and assign it to the variable
                if user_input.lower() == 'finished': # check if the user input 'FINISHED'
                    break # Exits the loop of the user input 'FINISHED'
                try: #Attemps too execute the following code
                    numbers.extend([float(num) for num in user_input.split(',')]) # Converts each number to a float and makes the list longer with these extra numbers 
                except ValueError: # Deals with any invalid data
                    print("INVALID: please enter valid numbers separated by commas.") # Prints an error messsage
        else: # Alternative if the user has entered an invalid number
            print("INVALID: Please enter a number from 1 to 7.") # Prints an error message  

main() # Starts the execution of the program
