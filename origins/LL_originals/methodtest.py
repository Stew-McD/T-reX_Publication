#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:45:29 2022

@author: stew
"""

import os
import brightway2 as bw
import pandas as pd

# USER VARIABLES
# the name of the impact category file:
file_name = 'TWDliquid.xlsx'
# the name of the Brightway project to add the impact category to:
project_name = 'cutoff38'
# the name of the biosphere database in above project:
biosphere_name = 'db_waste'


# find the right file and read it
cwd = os.getcwd()
file_path = os.path.join(cwd, file_name)
mthd = pd.read_excel(file_path)

# open the right BW project and biosphere database
bw.projects.set_current(project_name)
biosphere = bw.Database(biosphere_name)
bs = pd.DataFrame(biosphere)

#check if there are matching problems
print('+++ Checking if the flows of the file match the biosphere...')
new_method = []
errors = 0
for row in mthd.iterrows():
    matches = bs[(bs['name'] == row[1]['name'])]
    if matches.shape[0] == 0:
        # this TMR flow does not exist in the biosphere database
        print('    > no matches for:', row[1]['name'])
        errors += 1
    elif matches.shape[0] > 1:
        # this TMR flow is not well defined and could match multiple flows in the biosphere database
        print('    > too many matches for:', row[1]['name'])
        errors += 1
    else:
        # this TMR flow has 1 match, we add a tuple of the key and its flow value to our method list
        key = (biosphere_name, matches['code'].tolist()[0])
        value = row[1]['meanValue']
        new_method.append((key, value))

# If there were errors, ask user if they still want to add the impact category
if errors > 0:
    m = '\n+++ There were problems matching the TWD flows to the biosphere database'
    q = '\n+++ Would you still like to add the impact category? [y/n]: '
    cont = confirmation(question=q, message=m)
    if not cont:
        print("+++ There is likely a problem with the file or this version of the biosphere database"
              "    Check the file or contact the authors mentioning the names of the above flows")
        raise Exception('USER EXIT')
        exit()
else:
    print("+++ No problems found in matching the flows.")

# Add the data to Brightway:
try:
    pass
    method_name = ('Waste Footprint', 'Total Waste Demand', 'Liquid Waste')
    print('+++ Adding the new impact category to Brightway...')
    m = bw2data.Method(method_name)
    m.register(description="For Estimating Total Waste Demand of a Process", unit='m3')
    m.write(new_method)
    print('+++ Success!')
    print('    The impact category was added with the name: {}'.format(str(method_name)))
    print('    Exiting script')
except:
    print('\n+++ There was a problem adding the impact category to Brightway, contact Brightway developers')
