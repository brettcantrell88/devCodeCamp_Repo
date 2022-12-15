# 1) Create a function called 'run_calculations()'. As we build a few additional functions, 
# we will end up calling them inside of this 'run_calculations()' function. Consider it your "master function"!

# 2) Call this function on the very last line of your .py file. This way, every time you rerun the application, 
# the 'run_calculations()' function will run, executing all of the code that we add to the inside!

# 3) Next, let's build a function like the first one in the above Demo Video. This function should be called 
# 'add_two_numbers', and should have two parameters, so that we can pass in two values when we call it!

# 4) Give the inside of this function the logic to add the parameters together, store the sum in a variable called 
# 'result', and return that 'result' variable!

# 5) Next, we'll want to call this function inside of the 'run_calculations()' function. Because the 
# 'add_two_numbers()' function we are calling has two parameters, we need to provide two values, just like in the 
# demo video! Provide whatever two numbers you like. Be sure to capture the result that is returned from 
# 'add_two_numbers()', and print it to the console on the following line!

# 6) Next, we will write two more functions:
#     a) Write a function that takes in two numbers, and returns the difference between the two numbers.
#     b) Write a function that takes in three numbers. This function should multiply the first two numbers together, 
#        divide that value by the third number, and return the final result.
#     c) You can name these two functions whatever you like. Keep in mind that the name of a function should be an 
#        "action phrase", and should accurately describe what job the function performs!

# 7) Call your two new functions inside of your 'run_calculations()' function as well, capturing and printing the 
#    result of each function call!

def add_two_numbers(number_one, number_two):
     result = number_one + number_two
     return result

result_from_function_1 = add_two_numbers(5, 10)
print(result_from_function_1)

def subtract_two_numbers(number_one, number_two):
     result = number_one - number_two
     return result

result_from_function_2 = subtract_two_numbers(5, 10)
print(result_from_function_2)

def multiply_and_divide_three_numbers(number_one, number_two, number_three):
     result = number_one * number_two / number_three
     return result 

result_from_function_3 = multiply_and_divide_three_numbers(5, 10, 2)
print(result_from_function_3)

user_input = int(input("Pick a number. "))

name = "Brett"
print("My name is " + 3/6 + " Cantrell.")
print(f"My name is {['P']}.")