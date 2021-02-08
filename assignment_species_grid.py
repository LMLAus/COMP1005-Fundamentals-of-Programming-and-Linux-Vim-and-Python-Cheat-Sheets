"""
Student Name:           Lisa Luff
Student ID:             16167920

assignment_species_grid.py:
                        Holds the classes and methods specific to species for
                        the COMP1005 assignment

Dependecies:            random
                        assignment_grids.py
                        assignment_species.py

Classes:                SpeciesSimulation()
                        SpeciesGrid(SpeciesSimulation)

Modules:                SpeciesSimulation -
                            __init__(self)
                                Holds counters
                            new_object(self, gridi, obj_type, name, pos)
                                Creates new instance of specific species and adds to grid
                            make_baby(self, gridi, obj1, obj2)
                                Creates baby of two objs using new_object
                            have_fight(self, gridi, obj1, obj2)
                                Runs fight simulation and removes object that dies
                            obj_interaction(self, gridi, obj1, obj2)
                                Decides what interaction to run based on object info
                        SpeciesGrid -
                            __init__(self, n_list, grid_height, grid_length)
                                Input variables
                                Grid info
                            grid_setup(self)
                                Initiate the grid
                            initial_objects(self)
                                Place first species in the grid using new_object
                                - get_pos()
                                    Randomises position of initial objects
                            obj_movement(self, obj)
                                Moves object around the grid based on species info,
                                and removes them from the simulation if too old
                            find_interaction(self)
                                Finds interactions, and runs obj_interaction when found
                            grid_fullness(self)
                                Checks how full the grid is, and increases aggression/
                                decreases breeding at set points using internal function,
                                indicates to end simulation if grid becomes full
                                - skill_current(obj, skill, value)
                                    Find the amount to change the skill by
                                - apply_skill(skill, value)
                                    Applies the skill change accross the board
                            print_grid(self)
                                Prints grid nicely

Revisions:              19/10/2020 -    Created
                                        Preamble written
                        23/10/2020 -    Classes created
                                        Class variables set
                                        Added grid setup methods
                        24/10/2020 -    Added SpeciesSimulation class
                                        Added movement, interactions and fullness
                                        Separated species and species grid classes
                        25/10/2020 -    Amended for output of random.choices giving
                                            lists, or strings instead of objects
                                        Amended small issues found when testing
                                        Added functions within functions to break up
                                            long functions
                        26/10/2020 -    Amended to match new species options
                                        Added breed skill changes to fullness
                                        Broke up fullness into functions
                                        Added find_interaction
                                        Tested all
                                        Changed grid height and width to input
                                        Changed species start numbers to input
                                        Moved obj_interaction to SpeciesSimulation
"""

import random

from assignment_grids import Grid

from assignment_species import Human, Vulcan, Klingon

class SpeciesSimulation():

    """The functions for running the simulation"""

    def __init__(self):
        self.humans = []
        self.human_total = 0
        self.vulcans = []
        self.vulcan_total = 0
        self.klingons = []
        self.klingon_total = 0

        # Total objects
        self.current_total = 0
        self.total = 0

        # Baby counts
        self.baby_counts = [0, 0, 0, 0]
            # 0 - Human babies
            # 1 - Vulcan babies
            # 2 - Klingon babies
            # 3 - Total babies

        # Fight counts
        self.fight_counts = [0, 0, 0, 0, 0, 0, 0]
            # 0 - Human fights
            # 1 - Human losses
            # 2 - Vulcan fights
            # 3 - Vulcan losses
            # 4 - Klingon fights
            # 5 - Klingon losses
            # 6 - Total fights

    def new_object(self, gridi, obj_type, name, pos):
        """Creates a new object"""

        row = pos[0]
        column = pos[1]

        # Create instance
        if obj_type == "Human":
            name = Human(name)
            self.humans.append(name)
            self.human_total += 1
        elif obj_type == "Vulcan":
            name = Vulcan(name)
            self.vulcans.append(name)
            self.vulcan_total += 1
        else:
            name = Klingon(name)
            self.klingons.append(name)
            self.klingon_total += 1

        self.total += 1
        self.current_total += 1

        # Set instance gender and lifespan
        name.decide_gender()
        name.decide_lifespan()

        # Add to grid
        gridi.add_object(name, row, column)

        return name, gridi

    def make_baby(self, gridi, obj1, obj2):
        """Make a baby for if interaction leads to baby"""

        # What species
        baby_species = random.randint(1, 2)

        if baby_species == 1:
            baby_species = obj1.SPECIES_TYPE
        else:
            baby_species = obj2.SPECIES_TYPE

        pos = [obj1.obj_row, obj1.obj_column]

        # Make baby
        if baby_species == "Human":
            name = f'Human {str(self.human_total + 1)}'
            self.baby_counts[0] += 1
            self.new_object(gridi, "Human", name, pos)

        elif baby_species == "Vulcan":
            name = f'Vulcan {str(self.vulcan_total + 1)}'
            self.baby_counts[1] += 1
            self.new_object(gridi, "Vulcan", name, pos)

        else:
            name = f'Klingon {str(self.klingon_total + 1)}'
            self.baby_counts[2] += 1
            self.new_object(gridi, "Klingon", name, pos)

        self.baby_counts[3] += 1

    def have_fight(self, gridi, obj1, obj2):
        """Have fight for if interaction leads to fight"""

        # Probability of either winning as a percentage
        obj1_p_lose = 1 - (obj1.FIGHT_SKILL/(obj1.FIGHT_SKILL + obj2.FIGHT_SKILL))
        obj2_p_lose = 1 - (obj2.FIGHT_SKILL/(obj1.FIGHT_SKILL + obj2.FIGHT_SKILL))

        # Choose a loser
        choose_loser = random.choices([1, 2],
                                      weights=[obj1_p_lose, obj2_p_lose],
                                      k=1)

        loser_n = choose_loser[0]

        if loser_n == 1:
            loser = obj1
        else:
            loser = obj2

        #print(f'Loser: \t{loser}\
        #        \nGrid position: {(loser.obj_row, loser.obj_column)}')

        # It is a fight to the death, so the loser is removed from the grid
        gridi.remove_object(loser)
        if loser.SPECIES_TYPE == "Human":
            self.humans.remove(loser)
        elif loser.SPECIES_TYPE == "Vulcan":
            self.vulcans.remove(loser)
        else:
            self.klingons.remove(loser)

        # Add to counters
        if obj1.SPECIES_TYPE == 'Human':
            self.fight_counts[0] += 1
        elif obj1.SPECIES_TYPE == 'Vulcan':
            self.fight_counts[2] += 1
        elif obj1.SPECIES_TYPE == 'Klingon':
            self.fight_counts[4] += 1

        if obj2.SPECIES_TYPE == 'Human':
            self.fight_counts[0] += 1
        elif obj2.SPECIES_TYPE == 'Vulcan':
            self.fight_counts[2] += 1
        elif obj2.SPECIES_TYPE == 'Klingon':
            self.fight_counts[4] += 1

        if loser.SPECIES_TYPE == 'Human':
            self.fight_counts[1] += 1
        elif loser.SPECIES_TYPE == 'Vulcan':
            self.fight_counts[3] += 1
        else:
            self.fight_counts[5] += 1

        self.fight_counts[6] += 2
        self.current_total -= 1

        return gridi

    def obj_interaction(self, gridi, obj1, obj2):
        """Determines what to do if an interaction occurs,
            if there are more than 2 objs, 2 will be randomly chosen"""

            # Interaction type ('b' - have baby, 'f' - fight, 'n' - nothing)
        int_types = ['b', 'f', 'n']

        def baby_prob(obj1, obj2):
            """Runs calculations to find the probability of having a baby"""

            paired_p_baby = obj1.BREED_SKILL * obj2.BREED_SKILL

            if obj1.gender == 'm' and obj2.gender == 'f':
                p_baby = paired_p_baby
            elif obj1.gender == 'f' and obj2.gender == 'm':
                p_baby = paired_p_baby
            else:
                p_baby = 0

            return p_baby

        # Probability of baby
        p_baby = baby_prob(obj1, obj2)

        # Probability of fight
        p_fight = obj1.AGGRESSIVENESS * obj2.AGGRESSIVENESS

        # Make sure total less than 1
        if p_baby + p_fight > 1:
            p_baby = (p_baby/(p_baby + p_fight))
            p_fight = (p_fight/(p_baby + p_fight))

        # Probability of nothing
        p_nothing = 1 - (p_baby + p_fight)

        # Decide type of interaction
        int_selection = random.choices(int_types,
                                       weights=[p_baby, p_fight, p_nothing],
                                       k=1)
        int_type = int_selection[0]

        if int_type == 'b':
            self.make_baby(gridi, obj1, obj2)
        elif int_type == 'f':
            self.have_fight(gridi, obj1, obj2)

        return gridi


class SpeciesGrid(SpeciesSimulation):

    """The grid used in the simulation"""

    def __init__(self, n_list, grid_height, grid_length):
        super().__init__()
        # Number of objects for each species to be used in initial grid
        self.new_humans = n_list[0]
        self.new_vulcans = n_list[1]
        self.new_klingons = n_list[2]
        # How many grid rows
        self.grid_height = grid_height
        # How many grid columns
        self.grid_length = grid_length
        # Setup grid
        self.grid = []

    def grid_setup(self):
        """Setting grid default variables for the simulation"""

            # Initialise grid instance for simulation
        self.grid = Grid(self.grid_height, self.grid_length)
        self.grid.initialise_grid()

        return self.grid

    def initial_objects(self):
        """Creates initial group of objects and places them on the grid"""

        def get_pos():

            row = random.randint(0, self.grid_height - 1)
            column = random.randint(0, self.grid_length - 1)
            pos = [row, column]

            return pos

        for _ in range(self.new_humans):
            name = f'Human {str(self.human_total + 1)}'
            hpos = get_pos()
            self.new_object(self.grid, "Human", name, hpos)

        for _ in range(self.new_vulcans):
            name = f'Vulcan {str(self.vulcan_total + 1)}'
            vpos = get_pos()
            self.new_object(self.grid, "Vulcan", name, vpos)

        for _ in range(self.new_klingons):
            name = f'Klingon {str(self.klingon_total + 1)}'
            kpos = get_pos()
            self.new_object(self.grid, "Klingon", name, kpos)

        return self.grid

    def obj_movement(self, obj):
        """Runs objects through movement functions in grids and removes any
            objects that reach their lifespan"""

        p_change = obj.IMPULSIVENESS
        n_change = obj.SPEED

        for _ in range(n_change):
            self.grid.object_movement(obj, p_change)

        obj.age += 1
        if obj.age > obj.lifespan:
            self.grid.remove_object(obj)
            if obj.SPECIES_TYPE == "Human":
                self.humans.remove(obj)
            elif obj.SPECIES_TYPE == "Vulcan":
                self.vulcans.remove(obj)
            else:
                self.klingons.remove(obj)
            self.current_total -= 1

        return self.grid

    def find_interaction(self):
        """Grid sweep to find where two objects share a space"""

        for row in range(self.grid_height):
            for column in range(self.grid_length):
                objects = self.grid.get_objects(row, column)
                # Start at 1 because always contains 0
                # If more than 2, only choose first two
                try:
                    obj1 = objects[1]
                    obj2 = objects[2]
                    self.obj_interaction(self.grid, obj1, obj2)
                except IndexError as error:
                    continue

    def grid_fullness(self):
        """Increases aggression as the grid fills, and ends simulation if full"""

        fullness = self.current_total/(self.grid_height * self.grid_length)

        def skill_current(obj, skill, value):
            """Function for aggression and breeding increase"""

            if skill == "a":
                start_skill = obj.START_AGGRESSIVENESS
            else:
                start_skill = obj.START_BREED

            remaining = 1 - start_skill
            increase = remaining * (2 / 3)

            if value == 0:
                new_skill = 0
            elif value == 1:
                new_skill = 1
            elif value == 2:
                new_skill = start_skill - increase
            else:
                new_skill = start_skill + increase

            return new_skill

        def apply_skill(skill, value):
            """Applies new_agg to species"""

            if skill == 'a':
                for obj in self.humans:
                    obj.AGGRESSIVENESS = skill_current(obj, 'a', value)
                for obj in self.vulcans:
                    obj.AGGRESSIVENESS = skill_current(obj, 'a', value)
                for obj in self.klingons:
                    obj.AGGRESSIVENESS = skill_current(obj, 'a', value)
            else:
                for obj in self.humans:
                    obj.BREED_SKILL = skill_current(obj, 'b', value)
                for obj in self.vulcans:
                    obj.BREED_SKILL = skill_current(obj, 'b', value)
                for obj in self.klingons:
                    obj.BREED_SKILL = skill_current(obj, 'b', value)

        run = 1

        if  0 < fullness < 0.25:
            apply_skill(0, 'a')
            apply_skill(1, 'b')
            run = 1
        elif 0.25 <= fullness < 0.5:
            apply_skill(2, 'a')
            apply_skill(3, 'b')
            run = 1
        elif 0.5 <= fullness < 0.6:
            apply_skill(3, 'a')
            apply_skill(2, 'b')
            run = 1
        elif 0.6 <= fullness < 1:
            apply_skill(1, 'a')
            apply_skill(0, 'b')
            run = 1
        elif fullness >= 1:
            run = 0
            print("The planet has reached max capacity and civilisation has collapsed.")
        elif fullness <= 0:
            run = 0
            print("The planet no longer has any remaining species.")

        return run

    def print_grid(self):
        """Prints the grid nicely"""

        self.grid.print_grid()
