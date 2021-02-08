"""
Student Name:           Lisa Luff
Student ID:             16167920

assignment_data.py:     Store the simulation data from the user interface for
                        COMP1005 assignment assignment_main.py to
                        assignment_data.csv as a dataframe

Dependencies:           sys
                        pandas
                        assignment_data.csv

Functions:              data_collector(usergrid)
                            Collects data in a dataframe and sends to csv

Revisions:              27/10/2020 -    Created
                                        Preamble written
                                        Data calculated
                                        Dataframe created
                                        Set to send to csv
"""

import sys

import pandas as pd

def data_collector(usergrid):
    """Collects and sends data for assignment_main.py to assignment_data.csv"""

    # Actual data
        # Current and total
    c_total = usergrid.current_total
    total = usergrid.total

        # Current per species
    h_current = len(usergrid.humans)
    v_current = len(usergrid.vulcans)
    k_current = len(usergrid.klingons)

        # Total per species
    h_total = usergrid.human_total
    v_total = usergrid.vulcan_total
    k_total = usergrid.klingon_total

    row_names = {'Names': ['Total', 'Human', 'Vulcan', 'Klingon']}
    data = pd.DataFrame(data=row_names)

    data['Current total'] = [c_total, h_current, v_current, k_current]
    data['Total'] = [total, h_total, v_total, k_total]

        # Species current total and total proportions
    try:
        h_prop_ct = h_current/c_total
        v_prop_ct = v_current/c_total
        k_prop_ct = k_current/c_total
    except ZeroDivisionError as error:
        h_prop_ct = 0
        v_prop_ct = 0
        k_prop_ct = 0

    try:
        h_prop_t = h_total/total
        v_prop_t = v_total/total
        k_prop_t = k_total/total
    except ZeroDivisionError as error:
        h_prop_t = 0
        v_prop_t = 0
        k_prop_t = 0

    data['% of current total'] = ['-', h_prop_ct, v_prop_ct, k_prop_ct]
    data['% of total'] = ['-', h_prop_t, v_prop_t, k_prop_t]

        # Babies born total
    b_total = usergrid.baby_counts[3]

        # Babies born per species
    h_baby = usergrid.baby_counts[0]
    v_baby = usergrid.baby_counts[1]
    k_baby = usergrid.baby_counts[2]

    data['Babies total'] = [b_total, h_baby, v_baby, k_baby]

        # Babies born proportion per species
    try:
        h_baby_prop = h_baby/b_total
        v_baby_prop = v_baby/b_total
        k_baby_prop = k_baby/b_total
    except ZeroDivisionError as error:
        h_baby_prop = 0
        v_baby_prop = 0
        k_baby_prop = 0

    data['% total babies'] = ['-', h_baby_prop, v_baby_prop, k_baby_prop]

        # Fights had total
    f_total = usergrid.fight_counts[6]

        # Human fight stats
    h_fights = usergrid.fight_counts[0]
    h_losses = usergrid.fight_counts[1]
    h_wins = h_fights - h_losses
    try:
        h_win_prop = h_wins/h_fights
    except ZeroDivisionError as error:
        h_win_prop = 0

        # Vulcan fight stats
    v_fights = usergrid.fight_counts[2]
    v_losses = usergrid.fight_counts[3]
    v_wins = v_fights - v_losses
    try:
        v_win_prop = v_wins/v_fights
    except ZeroDivisionError as error:
        v_win_prop = 0

        # Klingon fight stats
    k_fights = usergrid.fight_counts[4]
    k_losses = usergrid.fight_counts[5]
    k_wins = k_fights - k_losses
    try:
        k_win_prop = k_wins/k_fights
    except ZeroDivisionError as error:
        k_win_prop = 0

       # Species proportion of total fights
    try:
        h_fight_prop = h_fights/f_total
        v_fight_prop = v_fights/f_total
        k_fight_prop = k_fights/f_total
    except ZeroDivisionError as error:
        h_fight_prop = 0
        v_fight_prop = 0
        k_fight_prop = 0

    data['Fights total'] = [f_total, h_fights, v_fights, k_fights]
    data['Fight losses'] = ['-', h_losses, v_losses, k_losses]
    data['Fight wins'] = ['-', h_wins, v_wins, k_wins]
    data['% total fights'] = ['-', h_fight_prop, v_fight_prop, k_fight_prop]
    data['% total wins'] = ['-', h_win_prop, v_win_prop, k_win_prop]

        # Total loving vs fighting
    try:
        love_prop = b_total/(b_total + f_total)
    except ZeroDivisionError as error:
        love_prop = 0

    fight_prop = 1 - love_prop

        # Loving vs fighting per species
    try:
        h_love_prop = h_baby/(h_baby + h_fights)
    except ZeroDivisionError as error:
        h_love_prop = 0

    h_fight_prop = 1 - h_love_prop

    try:
        v_love_prop = v_baby/(v_baby + v_fights)
    except ZeroDivisionError as error:
        v_love_prop = 0

    v_fight_prop = 1 - v_love_prop

    try:
        k_love_prop = k_baby/(k_baby + k_fights)
    except ZeroDivisionError as error:
        k_love_prop = 0

    k_fight_prop = 1 - k_love_prop

    data['% interactions = babies'] = [love_prop, h_love_prop, v_love_prop, k_love_prop]
    data['% interactions = fights'] = [fight_prop, h_fight_prop, v_fight_prop, k_fight_prop]

    # Transpose for readability
    data = data.T

    try:
        data.to_csv('assignment_data.csv', header='columnnames')
    except FileNotFoundError as error:
        sys.exit("Oh no, it seems the file is missing. \
                You can make a file with the same name and try again.")

    return data
