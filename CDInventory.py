"""
Title: Assignment06_Starter.py
Desc: Working with classes and functions.
Change Log: (Who, When, What)
DBiesinger, 2030-Jan-01, Created File
NToulas, 2022-Jun-06, Modified script
"""

import pickle

# -- DATA -- #
strChoice = ''  # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
STR_FILE_NAME = 'CDInventory.dat'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:

    @staticmethod
    def add_cd(str_id, str_title, str_artist, table):
        """Function to add CD data to inventory

        Args:
            str_id (string): ID number
            str_title (string): CD title name
            str_artist (string): artist name
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        row = {'ID': str_id, 'Title': str_title, 'Artist': str_artist}
        table.append(row)

    @staticmethod
    def delete_cd_by_id(int_id_to_delete, table):
        """Function to delete CD data from inventory by ID

        Args:
            int_id_to_delete: ID of CD to be deleted
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        int_row_number = -1
        is_cd_removed = False
        for row in table:
            int_row_number += 1
            if row['ID'] == int_id_to_delete:
                del table[int_row_number]
                is_cd_removed = True
                break
        if is_cd_removed:
            print('The CD was removed')
        else:
            print('Could not find this CD!')


class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            with open(file_name, 'rb') as file:
                data = pickle.load(file)
            for line in data:
                table.append(line)
            return table
        except FileNotFoundError:
            print('File does not exist')

    @staticmethod
    def write_file(file_name, table):
        """Function to write data to file

        Writes the data to file identified by file_name into CSV format

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'wb') as file:
            pickle.dump(table, file)


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def ask_for_cd_info():
        """Prompts user for CD info

        Returns:
            result: list of user input (ID, CD title, artist)

        """
        str_id = int(input('Enter ID: ').strip())
        str_title = input('What is the CD\'s title? ').strip()
        st_artist = input('What is the Artist\'s name? ').strip()
        return str_id, str_title, st_artist


# 1. When program starts, read in the currently saved Inventory
try:
    FileProcessor.read_file(STR_FILE_NAME, lstTbl)
except EOFError as error:
    print('There is nothing in your inventory')

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(STR_FILE_NAME, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        result = IO.ask_for_cd_info()
        # 3.3.2 Add item to the table
        DataProcessor.add_cd(result[0], result[1], result[2], lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        DataProcessor.delete_cd_by_id(intIDDel, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(STR_FILE_NAME, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
