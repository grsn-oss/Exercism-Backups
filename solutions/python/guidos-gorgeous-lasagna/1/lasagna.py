"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    result = (EXPECTED_BAKE_TIME - elapsed_bake_time)
    return result

#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation of time base on the number of layers of the lasagna

    :param number_of_layers: int - the number of layers
    :return: int - each layers takes to mins, therefore it return the multiplication of the layers * 2
    """
    return 2 * number_of_layers


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """"Calculate how much time has elapsed

    :param number_of_layers: int - How many layers does the lasagna has
    :param elapsed_bake_time: int - How much time has elapsed
    :return: int - The sum of the time to cook each layers and how much time has elapsed

    preparation_time_in_minutes function can be used to determine the time to cook each layer and the elapsed_bake_time can be 
    added to determined how much time has elapsed
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
