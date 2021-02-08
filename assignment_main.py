"""
Student Name:           Lisa Luff
Student ID:             16167920

assignment_main.py:     The user interface for COMP1005 assignment, automates the program

Dependencies:           sys
                        time
                        pandas
                        plotly
                        assignment_species_grid.py
                        assignment_data.py

Functions:              run_simulation()
                            Runs through one round of movement and interactions
                            To be used repeatedly until desired amount of time

Revisions:              26/10/2020 -    Created
                                        Completed
                                        Run numerous times, with no issues
                        27/10/2020 -    Moved data to assignment_data.py to ensure
                                        program isn't too long
                                        Added plot
                                        Enabled input to be from command line
"""

import sys

import time

import pandas as pd

import plotly.express as px

from assignment_species_grid import SpeciesGrid

from assignment_data import data_collector

# Make sure input is valid
try:
    n_humans = int(sys.argv[1])
    n_vulcans = int(sys.argv[2])
    n_klingons = int(sys.argv[3])
    grid_height = int(sys.argv[4])
    grid_length = int(sys.argv[5])
    years = int(sys.argv[6])
except (IndexError, TypeError) as error:
    sys.exit(f'Sorry, your input is invalid, input should be: \
            \n\tStart number of humans, \
            \n\tStart number of vulcans, \
            \n\tStart number of Klingons, \
            \n\tNumber of grid rows, \
            \n\tNumber of grid columns, and \
            \n\tNumber of times to run the simulation. \
            \n Please try again. \
            \n{error}')
except Exception as error:
    sys.exit(f'Oh no! Something went wrong! \
            \n{error}')

# Welcome message
print(f'Welcome to PaSciRo. \
        \nA popular sector of the universe. \
        \nHere the Humans, Vulcans and Klingons live together \
        \nbut not quite in harmony...\n \
        \nToday we will looking at a section: \
        \n\t{grid_height} light years, by {grid_length} light years in size. \
        \nOver a period of: \
        \n\t{years} years.\n')

time.sleep(3)

# Let them know the simulation is now running
print("The simulation is now running. \
        \n Shortly you will see a graph showing their movement, \
        \n and will be able to see what they got up to.\n")

time.sleep(3)

# Create instance
usergrid = SpeciesGrid([n_humans, n_vulcans, n_klingons], grid_height, grid_length)

# Initiate grid
usergrid.grid_setup()

# Add first objects
usergrid.initial_objects()

# Lists for plot dataframe
date = []
s_type = []
s_name = []
s_row = []
s_column = []

def run_simulation():
    """Run this for each year to create movement, and find and run interactions"""

    # Move each of them
    for human in usergrid.humans:
        usergrid.obj_movement(human)
        date.append(run_count)
        s_type.append(human.SPECIES_TYPE)
        s_name.append(human.name)
        s_row.append(human.obj_row)
        s_column.append(human.obj_column)
    for vulcan in usergrid.vulcans:
        usergrid.obj_movement(vulcan)
        date.append(run_count)
        s_type.append(vulcan.SPECIES_TYPE)
        s_name.append(vulcan.name)
        s_row.append(vulcan.obj_row)
        s_column.append(vulcan.obj_column)
    for klingon in usergrid.klingons:
        usergrid.obj_movement(klingon)
        date.append(run_count)
        s_type.append(klingon.SPECIES_TYPE)
        s_name.append(klingon.name)
        s_row.append(klingon.obj_row)
        s_column.append(klingon.obj_column)

    # Find and run interactions
    usergrid.find_interaction()

    # Check if the grid is full (won't run if full or empty)
    continue_sim = usergrid.grid_fullness()

    if continue_sim == 0:
        print(f'\nCivilisation lasted for {run_count} years.\n')

    return continue_sim

# Actually run the program
continue_sim = 1
# Make sure the simulation only runs the specified time
run_count = 0
# Make sure it stops if grid fullness requires
while continue_sim == 1:
    continue_sim = run_simulation()
    run_count += 1
    if run_count >= years:
        continue_sim = 0

# Let them know the information is ready
print("Your graph and data are now ready. \
        \nI will open it for you now.\n")

time.sleep(3)

# Run data function
data = data_collector(usergrid)

print(data)

print('\nA copy of your data has been stored in assignment_data.csv.\n')

time.sleep(3)

print("\nThe graph will now pop up.\n")

# Create data from for graph
year_dict = {'Year': date}
graph = pd.DataFrame(year_dict)
graph['Species'] = s_type
graph['Name'] = s_name
graph['Row'] = s_row
graph['Column'] = s_column

# Create graph
fig = px.scatter(graph,
                 x="Row",
                 y="Column",
                 animation_frame="Year",
                 animation_group="Name",
                 color="Species",
                 hover_name="Name")

fig.show()

time.sleep(3)

# Say goodbye
print("\nThank you for visting PaSciRo. \
        \nHave a wonderful day, goodbye!")
