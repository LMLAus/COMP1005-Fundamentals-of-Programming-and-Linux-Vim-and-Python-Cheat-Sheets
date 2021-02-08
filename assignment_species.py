"""
Student Name:           Lisa Luff
Student ID:             16167920

assignment_species.py:  Holds the classes and methods specific to species classes
                        for the COMP1005 assignment

Classes:                Species()
                        Human(Species)
                        Vulcan(Species)
                        Klingon(Species)

Modules:                Species -
                            Class variables
                            __init__
                                Variable for use in grids and interactions
                            decide_gender(self)
                                Sets gender of the instance
                            decide_have_babies(self, gender)
                                Set whether the instance will have babies
                        Human(Species) -
                            __repr__
                                What to show as instance
                            Class variables
                        Vulcan(Species) -
                            __repr__
                                What to show as instance
                            Class variables
                        Klingon(Species) -
                            __repr__
                                What to show as instance
                            Class variables

Revisions:              19/10/2020 -    Created
                                        Preamble written
                        23/10/2020 -    Classes created
                                        Class variables set
                                        Added species/child functions
                        24/10/2020 -    Added name variable to species
                                        Added grid and direction holders in species
                                        Separated species and species grid classes
                        26/10/2020 -    Increased lifespan
                                        Removed non-binary gender
                                        Removed childfree
                                        Increased breed_skill rates
                                        Decreased fight rates
                                        Amendments made to avoid running out of
                                            species so quickly
"""

import random

class Species():

    """Holds all general variables and functions for running simulation"""

    def __init__(self, name):
        """Class instance variables"""
        self.name = name
            # Intiate gender
        self.gender = 0
            # Initiate lifespan
        self.lifespan = 0
            # Initial age of instance
        self.age = int(0)
            # Store object location in grid
        self.obj_row = []
            # Store object location in grid
        self.obj_column = []
            # Store direction object is facing starting North
        self.obj_direction = [0, -1]

    def decide_lifespan(self):
        """Decides a lifespan for an instance"""

        lifespan = random.randint(70, 100)

        self.lifespan = lifespan

        return self.lifespan

    def decide_gender(self):
        """Assigns gender for creating a new object"""

        gender_options = ['m', 'f']
            # Male, or Female

        # Decide gender
        gender = random.choice(gender_options)

        self.gender = gender[0]

        return self.gender

class Human(Species):

    """Holds all variables for Humans"""

    SPECIES_TYPE = "Human"

    def __repr__(self):
        return f'Human: {str(self.name)}'

    # Setting default variables for Humans
        # How many moves they make per step
    SPEED = 2
        # How likely they are to change direction
    IMPULSIVENESS = 0.4
        # How likely they are to have a baby from an interaction
    BREED_SKILL = 0.7
    START_BREED = 0.7
        # How likely they are to have a fight with interacting
    AGGRESSIVENESS = 0.5
    START_AGGRESSIVENESS = 0.5
        # How likely they are to win a fight (fights are to the death)
    FIGHT_SKILL = 0.2

class Vulcan(Species):

    """Holds all variables for Vulcans"""

    SPECIES_TYPE = "Vulcan"

    def __repr__(self):
        return f'Vulcan: {str(self.name)}'

    # Setting default variables for Vulcans
        # How many moves they make per step
    SPEED = 1
        # How likely they are to change direction
    IMPULSIVENESS = 0.25
        # How likely they are to have a baby from an interaction
    BREED_SKILL = 0.1
    START_BREED = 0.1
        # How likely they are to have a fight with interacting
    AGGRESSIVENESS = 0.4
    START_AGGRESSIVENESS = 0.4
        # How likely they are to win a fight (fights are to the death)
    FIGHT_SKILL = 0.4

class Klingon(Species):

    """Holds all variables for Klingons"""

    SPECIES_TYPE = "Klingon"

    def __repr__(self):
        return f'Klingon: {str(self.name)}'

    # Setting default variables for Klingons
        # How many moves they make per step
    SPEED = 3
        # How likely they are to change direction
    IMPULSIVENESS = 0.6
        # How likely they are to have a baby from an interaction
    BREED_SKILL = 0.6
    START_BREED = 0.6
        # How likely they are to have a fight with interacting
    AGGRESSIVENESS = 0.6
    START_AGGRESSIVENESS = 0.6
        # How likely they are to win a fight (fights are to the death)
    FIGHT_SKILL = 0.9
