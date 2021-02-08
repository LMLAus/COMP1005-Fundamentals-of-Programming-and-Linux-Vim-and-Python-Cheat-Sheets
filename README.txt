
Student Name:		Lisa Luff
Student ID:		16167920

Synopsis:		Programs are for the COMP1005 Fundamentals of Programming
			assignment.
			
			Group of files together, take command line input
			from the user to run a simulation. The simulation consists of 
			three different species of alien travelling around a grid, 
			breeding, fighting and dying. It outputs a graph and a csv with
			information about what occurred during the simulation.

Use:			To run a simulation, the user will only interact with assignment_main.py
			Command line input will assign in order:
				Number of Humans starting on the grid
				Number of Vulcans starting on the grid
				Number of Klingons starting on the grid
				How many rows the grid should have
				How many columns the grid should have
				How many times the simulation should run
			So to use, in the command line enter:
	$ python3 assignment_main.py <n_humans> <n_vulcans> <n_klingons> <n_rows> <n_columns> <n_times>

Dependencies:		random
			sys
			pandas
			time
			plotly

Files:			README.txt
				Readme file with information for the package
			assignment_grids.py
				File holds functions needed to work with the grid
				system, can be used independently of the simulation.
				- Classes:
					Grid()
				- Grid methods:
					__init__(self, height, width)
					initialise_grid(self)
					check_barriers(self, row, column)
					add_object(self, obj, row, column)
					get_objects(self, row, column)
					remove_object(self, obj)
					object_movement(self, obj, p_change)
					print_grid
			assignment_species.py
				File holds the preset information, instance variables
				and functions for all three alien species.
				- Classes:
					Species()
					Human(Species)
					Vulcan(Species)
					Klingon(Species)
				- Species methods:
					__init__(self, name)
					decide_lifespan(self)
					decide_gender(self)
				- Human methods:
					__repr__(self)
				- Vulcan methods:
					__repr__(self)
				- Klingon methods:
					__repr__(self)
			assignment_species_grid.py
				Most import file for simulation, holds everything that
				links assignment_grids.py to assignment_species.py
				- Classes:
					SpeciesSimulation()
					SpeciesGrid(SpeciesSimulation)
				- SpeciesSimulation methods:
					__init__(self)
					new_object(self, gridi, obj_type, name, pos)
					make_baby(self, gridi, obj1, obj2)
					have_fight(self, gridi, obj1, obj2)
					obj_interaction(self, gridi, obj1, obj2)
						baby_prob(obj1, obj2)
				- SpeciesGrid methods:
					__init__(self, n_list, grid_height, grid_length)
					grid_setup(self)
					initial_objects(self)
						get_pos()
					obj_movement(self, obj)
					find_interaction(self)
					grid_fullness(self)
						skill_current
						apply_skill
					print_grid
			assignment_data.py
				Does all the data manipulation for printing, and saving to data.csv
				- Classes:
					None
				- Methods:
					data_collector(usergrid)
			assignment_data.csv
				Holds the most recent simulation data in the form of a dataframe
			assignment_main.py
				Runs everything with input from the user
				- Classes:
					None
				- Methods:
					run_simulation()

Versions:		18/10/2020 - 	Created an input checking program, to check for 
					valid input
			19/10/2020 - 	Created grids.py
					Created the the grid method, for initialisation,
					 adding and removing, including a position
					 randomiser
					Created species.py
			23/10/2020 - 	Had some overlap between species.py file and 
					 the grids.py file, so deleted any too specific 
					 from assignment_grid.py
					Finished grids.py except for movement, and tested
					Created species, and alien classes
					Set what they would hold and their presets
					Created relationship between species and the aliens
					Tested species.py
					Created SpeciesGrid class
					Created the methods for setting up a grid through
					 the species specific grid class, and adding the 
					 first aliens
			24/10/2020 - 	Removing random position adding method from 
					 grids.py, as it was unnecessary with the 
					 species_grids.py initising method
					Created grids.py movement method
					Gave species instances names
					Enabled species to hold instance grid position 
					 information
					Separated species.py and species_grid.py as
					 there was too much in one file
					Created SpeciesSimulation to break up the 
					 SpeciesGrid methods
					Created species movement, interaction and 
					 fullness methods
			25/10/2020 -	Tested species_grid.py
					Amended anywhere using random.choices to fix
					 issues due to output being in lists, or strings
					 instead of the associated object
					Small amendments made from testing
					Broke up extra long methods into nested smaller
					 functions
			26/10/2020 - 	Program had been designed to run through a user 
					 interface, and allow for settings to be changed,
					 and saved. After re-reading assignment instructions, 
					 I realised this was incorrect. So:
					  I removed the input checking program
					  Removed if statements that allowed certain values 
					   to be toggled
					Number of variables changed in species.py:
					 Increased lifespan
					 Removed non-binary gender
					 Removed child-free/infertile/non-hetero 
					 Amended species rates
					 Amendments made to avoid simulation ending due to
					  lack to remaining aliens in species_grid.py tests
					Amended species.grid.py to match species.py changes
					Added breed skill changes to fullness to encourage
					 aliens to have more babies
					Broke fullness method down into nested functions
					Start numbers for species were preset, amended
					 to be based on user input
					Moved obj_interation from SpeciesGrid to 
					 SpeciesSimulation
					Created main.py
					Completed run_simulation function and instructions
					 for running it and tested them
					Added get_object method to grids.py for use in 
					 interaction finding
			27/10/2020 -  	Moved data_collection to separate file to keep
					 main program succinct
					Added plot
					Enabled input to be taken from command line
					Testing ran
					Simulation program complete	
