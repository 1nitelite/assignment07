"""
Title: LAB06_A.py
Desc: simple demonstrator for classes
Change Log: (Who, When, What)
DBiesinger, 2030-Jan-01, Created File
NToulas, 2022-Jun-05, Modified code
"""

# -- DATA -- #
STR_FILE_INPUT = 'mathIn.txt'
STR_FILE_OUTPUT = 'mathOut.txt'

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

        with open(file_name, 'r') as file:
                data = file.read()
                data = data.split("\n")
                return data

    def write_file(file_name, results):
        """
        function to write the math results to file fileName

        Args:
            file_name (string): file Name to write the results to.
            results (list): The results

        Returns:
            None.

        """

        with open(file_name, 'w+') as file:
            for data in results:
                file.write(f'{data}\n')

# -- PRESENTATION (Input/Output) -- #
print('Basic Math script. Calculating the Sum, Difference, Product and Quotient of two numbers.')
int_table = IO.read_file(STR_FILE_INPUT)
results_table = []
counter = 0
while counter < len(int_table):
    int_list = int_table[counter].split(",")
    int_a, int_b = float(int_list[0]), float(int_list[1])
    result_list = []
    result_list.append(SimpleMath.get_sum(int_a, int_b))
    result_list.append(SimpleMath.get_difference(int_a, int_b))
    result_list.append(SimpleMath.get_product(int_a, int_b))
    result_list.append(SimpleMath.get_quotient(int_a, int_b))
    results_table.append(result_list)
    counter += 1
IO.write_file(STR_FILE_OUTPUT, results_table)
print('Computing completed!')