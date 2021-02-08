"""
Student Name:           Lisa Luff
Student ID:             16167920

assignment_grids.py:    Holds all the classes , and functions for use in
                        COMP1005 Assignment for working with grids

Dependencies:           random

Classes:                Grid()

Methods:                Grid -
                            __init__(self, height, width)
                                Creates an instance with information for working with grids
                            intialise_grid(self)
                                Creates the initial grid
                            check_barriers(self, row, column)
                                Checks the row and column values are within the bounds
                                of the grid
                            add_object(self, obj, row, column)
                                Adds an object to a given position in the grid
                            get_objects(self, row, column)
                                Gets a list of objects from a location
                            remove_object(self, obj)
                                Removes an object from the grid
                            object_movement(self, object, p_change))
                                Moves an object one step in the grid
                            interactions(self)
                                Initialised
                            print_grid(self)
                                Prints grid nicely

Revisions:              19/10/2020 -    Created
                                        Preamble written
                                        Grid class started
                        23/10/2020 -    Amended for file reorganisation
                                        Removed superfluous functions
                                        Removed functions that will be parameter sweeps
                                        Added all functions except movement and interaction
                        24/10/2020 -    Revised adding functions
                                        Add movement function
                        26/10/2020 -    Added get_objects for use in find interactions
"""

import random

class Grid():

    """All functions used with grids"""

    # Grid directions
    NORTH = [0, -1]
    SOUTH = [0, 1]
    EAST = [1, 0]
    WEST = [-1, 0]
    COMPASS = [NORTH, SOUTH, EAST, WEST]

    def __init__(self, height, width):
        """
            height -    number of rows
            width -     numbers of columns"""

        self.rows = height
        self.columns = width

        # Grid rows and columns set up
        self.grid = [[]]

    def initialise_grid(self):
        """Initialises the grid"""

        for _ in range(self.rows-1):
            self.grid.append([0])

        for i in range(self.rows):
            self.grid[i] = []
            for _ in range(self.columns):
                self.grid[i].append([0])

        return self.grid

    def check_barriers(self, row, column):
        """Ensure the position is within the grid"""

        if 0 <= row <= self.rows - 1 and 0 <= column <= self.columns - 1:
            can_add = 1
        else:
            can_add = 0

        return can_add

    def add_object(self, obj, row, column):
        """Add an object to a specific location on the grid"""

        add_valid = self.check_barriers(row, column)

        try:
            if add_valid == 1:
                obj.obj_row = row
                obj.obj_column = column
                self.grid[row][column].append(obj)
        except IndexError as error:
            print(f'Row or column value outside of range: {error}')
            print('Object not added')

        return self.grid

    def get_objects(self, row, column):
        """Allow objects at i, j to be pulled out"""

        objects = self.grid[row][column]

        return objects

    def remove_object(self, obj):
        """Removes a specific object"""

        row = obj.obj_row
        column = obj.obj_column

        self.grid[row][column].remove(obj)

        return self.grid

    def object_movement(self, obj, p_change):
        """Moves an object in the grid"""

        start_direction = obj.obj_direction
        current_row = obj.obj_row
        current_column = obj.obj_column
            # Probability of changing direction
        p_straight = 1 - p_change
        p_change = p_change/3
            # Initiate probability weights for directions
        w_change = []

        # Set weights to use p_change
        for item in self.COMPASS:
            if item == start_direction:
                w_change.append(p_straight)
            else:
                w_change.append(p_change)

        # Move object in random direction, and remove from previous position
        # Try again if outside of boundaries
        try_again = 0
        while try_again == 0:
            new_direction = random.choices(self.COMPASS, weights=w_change, k=1)
            new_row = current_row + new_direction[0][0]
            new_column = current_column + new_direction[0][1]
            if self.check_barriers(new_row, new_column) == 1:
                self.remove_object(obj)
                obj.obj_row = new_row
                obj.obj_column = new_column
                obj.obj_direction = new_direction
                self.grid[new_row][new_column].append(obj)
                try_again = 1
            else:
                continue

        return self.grid

    def print_grid(self):
        """Prints self.grid in a grid shape"""

        printit = [print(i) for i in self.grid]

        return printit
