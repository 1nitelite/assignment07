"""
Title: LAB06_B.py
Desc: simple demonstrator for classes
Change Log: (Who, When, What)
DBiesinger, 2030-Jan-01, Created File
NToulas, 2022-Jun-05, Modified code
"""

import pickle

# -- DATA -- #
STR_FILE_INPUT = 'numbers.dat'
STR_FILE_OUTPUT = 'results.dat'

# -- PROCESSING -- #
class SimpleMath:
    """A collection of simple math processing functions """

    @staticmethod
    def get_sum(val1=0.0, val2=0.0):
        """Function for adding two values


        Args:
            val1: the first number to add
            val2: the second number to add


        Returns:
            A float corresponding to the sum of val1 and val2
        """
        return float(val1 + val2)

    @staticmethod
    def get_difference(val1=0.0, val2=0.0):
        """Function for subtracting two values


        Args:
            val1: the number to subtract from
            val2: the number to subtract


        Returns:
            A float corresponding to the difference of val1 and val2
        """
        return float(val1 - val2)

    @staticmethod
    def get_product(val1=0.0, val2=0.0):
        """Function for multiplying two values


        Args:
            val1: the first number to multiply
            val2: the second number to multiply


        Returns:
            A float corresponding to the product of val1 and val2
        """
        return float(val1 * val2)

    @staticmethod
    def get_quotient(val1=0.0, val2=0.0):
        """Function for dividing two values


        Args:
            val1: the number to divide
            val2: the number to divide by


        Returns:
            A float corresponding to the quotient of val1 and val2
        """
        return float(val1 / val2)

class IO:
    """A collection of the Input / Output operations """

    def read_file(file_name):
        """
        function to read in two numbers from file fileName and return these

        Args:
            file_name (string): file name to read the numbers from

        Returns:
            num_a (int): first number in file fileName.
            num_b (int): second number in file fileName.

        """

        with open(file_name, 'rb') as file:
            data = pickle.load(file)
        return data

    def write_file(data, file_name):
        """
        function to write the math results to file fileName

        Args:
            file_name (string): file Name to write the results to.
            data (list): The results

        Returns:
            None.

        """

        with open(file_name, 'wb') as file:
            pickle.dump(data, file)

    def append_file(data, file_name):
        """
        function to append the math results to file fileName

        Args:
            file_name (string): file Name to write the results to.
            data (list): The results

        Returns:
            None.

        """

        with open(file_name, 'ab') as file:
            pickle.dump(data, file)

# -- PRESENTATION (Input/Output) -- #
print('Basic Math script. Calculating the Sum, Difference, Product and Quotient of two numbers.')
try:
    numbers = IO.read_file(STR_FILE_INPUT)
    results_table = []
    counter = 0
    while counter < len(numbers):
        int_a, int_b = float(numbers[0]), float(numbers[1])
        result_list = []
        result_list.append(SimpleMath.get_sum(int_a, int_b))
        result_list.append(SimpleMath.get_difference(int_a, int_b))
        result_list.append(SimpleMath.get_product(int_a, int_b))
        result_list.append(SimpleMath.get_quotient(int_a, int_b))
        results_table.append(result_list)
        counter += 1
    IO.write_file(results_table, STR_FILE_OUTPUT)
except EOFError as error:
    print("There are no numbers to compute")
    int_a = float(input('Please type in a number: '))
    int_b = float(input('Please type in another number: '))
    numbers = [int_a, int_b]
    IO.write_file(numbers, STR_FILE_INPUT)
    result_list = []
    result_list.append(SimpleMath.get_sum(int_a, int_b))
    result_list.append(SimpleMath.get_difference(int_a, int_b))
    result_list.append(SimpleMath.get_product(int_a, int_b))
    result_list.append(SimpleMath.get_quotient(int_a, int_b))
    IO.append_file(result_list, STR_FILE_OUTPUT)
print('Computing completed!')