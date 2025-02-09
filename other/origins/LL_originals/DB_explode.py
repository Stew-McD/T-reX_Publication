#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Explode DB
Created on Wed Nov 16 11:31:38 2022
@author: stew
"""
import bw2io as bi
import bw2data as bd
import wurst as w
import pandas as pd
import os

#%% 
project = "EOL-WDI-SCM-1"
db = "ei38_co"

#%% Introduction and project/db choice (if not given in function call)

print("** DBexplode returns a list of all exchanges in given BW2 database **")
print("\n * Using packages: ", 
      "\n\t bw2io" , bi.__version__, 
      "\n\t bw2data" ,bd.__version__,
      "\n\t wurst" , w.__version__)

try: bd.projects.set_current(project)
except NameError:
    print("\n* Available projects: \n\t" , [i[0] for i in bd.projects.report()])
    project = input("\n* Enter name of project to copy: ")
    bd.projects.set_current(project)
    project = input("\n* Enter name of project new project: ")
    bd.projects.copy_project(project)

try: db = bd.Database(db)
except NameError: 
    print("\n* Availabile databases in "+ bd.projects.current() +": " + str(list(bd.databases)))
    db = input("\n* Enter name of database to be processed: ")
    db = bd.Database(db)

print("\n* db:", db.name, "in project:", bd.projects.current, "will be processed")

#%% Explode database
print("\n Opening the sausage... \n")
guts = w.extract_brightway2_databases(db.name)

print("\n Extracting activities from db...")
df = pd.DataFrame(guts, columns =['code', 'exchanges'])

print("\n Exploding exchanges from activities...")
df = df.explode("exchanges", ignore_index=False)

print("\n Pickling...")
tmp = os.getcwd() + "/tmp"
if not os.path.isdir(tmp): os.mkdir(tmp)
pickle_path = os.path.join(tmp, "db.pickle")
df.to_pickle(pickle_path)
print(db.name, "was exploded and pickled. yay.")







