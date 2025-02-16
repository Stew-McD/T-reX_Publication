#!/usr/bin/env python
# coding: utf-8
"""
## This function searches for and aggregates all wastes (category is flexible) 
## by total mass or volume and provides this as an indicator in the Impact Assessment stage 
## of a given LCA in the Activity Browser.
"""

#%% Section 1: Setting Up Variables and Importing Ecoinvent, Biosphere, and Custom Databases

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import brightway2 as bw
from brightway2 import *
from bw2data.parameters import ActivityParameter, DatabaseParameter, ProjectParameter, Group
import bw2data


# Set this input to your specific project
projects.set_current("ecoinvent-import2")

create_core_migrations() #???? is that needed?

# Import Custom Waste Biosphere Flows (Liquid and Solid Waste)
sp = bw.ExcelImporter("wasteBiosphere_final.xlsx")
sp.apply_strategies()
sp.statistics()
sp.write_database()

# Import Ecoinvent 3.8 Cutoff
fpei38 = "/Users/girk/Desktop/ecoinvent_3.8_cutoff_ecoSpold02/datasets"
ei38 = bw.SingleOutputEcospold2Importer(fpei38, 'ecoinvent 3.8 cutoff')
ei38.apply_strategies()
ei38.statistics()
ei38.write_database()

eidb = bw.Database('ecoinvent 3.8 cutoff')
bio3 = bw.Database('biosphere3')
wd = bw.Database('cstmBiosphere')

database_names = ('biosphere3', 'cstmBiosphere','ecoinvent 3.8 cutoff', 'example', 'waste demand')

#%% Section 2: Applying Wurst to Format Biosphere, Ecoinvent, and Custom Database Structure in Python
import wurst as w

custom = w.extract_brightway2_databases(["cstmBiosphere"])
data = w.extract_brightway2_databases(["ecoinvent 3.8 cutoff"])
biodata = w.extract_brightway2_databases(["biosphere3"])


#%% Section 3: Using Pandas Dataframe to Access Waste Exchanges Without Losing Ability to Connect Exchange to
## Original Process
df = pd.DataFrame(data,
               columns =['classifications', 'comment', 'location', 'database', 'code', 'name', 'reference product', 'unit', 'exchanges', 'parameters', 'parameters full'])
df

df = pd.DataFrame(data,
               columns =['code', 'exchanges'])
df


### Exploding Processes by Exchanges to get one Exchange Per Row
df_explode = df.explode("exchanges", ignore_index=False)
df_explode


### Resetting Index of Dataframe
df_explode = df.explode("exchanges").reset_index(drop=True)
df_explode




#%% Section 4: Iterating through All Exchanges to Pull Out Waste Exchanges. Writing These Exchanges to a .txt File.
### solid waste output
open("solidWaste.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'kilogram' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('solidWaste.txt', 'a') as f:
            f.write(x + '\n')


# In[30]:


### liquid waste output
open("liquidWaste.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'cubic meter' in str(rowSeries['unit']):
        y = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('liquidWaste.txt','a') as f:
            f.write(y + '\n')


# In[32]:


### hazardous waste kg output
open("hazardWasteKg.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if ('hazard' in str(rowSeries['name']) or 'radioactice' in str(rowSeries['name'])) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'kilogram' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('hazardWasteKg.txt', 'a') as f:
            f.write(x + '\n')


# In[34]:


### non-hazardous waste kg output
open("nonhazardWasteKg.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if ('hazard' not in str(rowSeries['name']) and 'radioactive' not in str(rowSeries['name'])) and 'waste' in str(rowSeries['name']) and str(rowSeries['amount']) != '-1.0' and '1.0' not in str(rowSeries['amount']) and 'kilogram' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('nonhazardWasteKg.txt', 'a') as f:
            f.write(x + '\n')


# In[35]:


### non-hazardous waste m3 output
open("nonhazardWasteM3.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if ('hazard' not in str(rowSeries['name']) and 'radioactive' not in str(rowSeries['name'])) and 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'cubic meter' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('nonhazardWasteM3.txt', 'a') as f:
            f.write(x + '\n')


# In[36]:


### incinerated waste kg output
open("incineratedWasteKg.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if 'incineration' in str(rowSeries['name']) and 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'kilogram' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('incineratedWasteKg.txt', 'a') as f:
            f.write(x + '\n')


# In[37]:


### incinerated waste m3 output
open("incineratedWasteM3.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if 'incineration' in str(rowSeries['name']) and 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'cubic meter' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('incineratedWasteM3.txt', 'a') as f:
            f.write(x + '\n')


# In[38]:


### recycled waste kg output
open("recycledWasteKg.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if ('recycling' in str(rowSeries['name']) or 'recycled' in str(rowSeries['name'])) and 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'kilogram' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('recycledWasteKg.txt', 'a') as f:
            f.write(x + '\n')


# In[39]:


### recycled waste m3 output
open("recycledWasteM3.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if ('recycling' in str(rowSeries['name']) or 'recycled' in str(rowSeries['name'])) and 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'cubic meter' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('recycledWasteM3.txt', 'a') as f:
            f.write(x + '\n')


# In[40]:


### composted waste kg output
open("compostedWasteKg.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if ('composting' in str(rowSeries['name']) or 'compost' in str(rowSeries['name'])) and 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'kilogram' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('compostedWasteKg.txt', 'a') as f:
            f.write(x + '\n')


# In[41]:


### composted waste m3 output
open("compostedWasteM3.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if ('composting' in str(rowSeries['name']) or 'compost' in str(rowSeries['name'])) and 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'cubic meter' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('compostedWasteM3.txt', 'a') as f:
            f.write(x + '\n')


# In[42]:


### landfilled waste kg output
open("landfilledWasteKg.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if ('landfill' in str(rowSeries['name']) or 'open dump' in str(rowSeries['name']) or 'underground deposit' in str(rowSeries['name'])) and 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'kilogram' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('landfilledWasteKg.txt', 'a') as f:
            f.write(x + '\n')


# In[43]:


### landfilled waste m3 output
open("landfilledWasteM3.txt", "w").close()
for i in range(0, df_explode.shape[0]):
    # get row contents as series using iloc{]
    # and index position of row
    rowSeries = df_explode.iloc[i, 1]
    rowSeries['process code']= df_explode.iloc[i,0]
    if ('landfill' in str(rowSeries['name']) or 'open dump' in str(rowSeries['name']) or 'underground deposit' in str(rowSeries['name'])) and 'waste' in str(rowSeries['name']) and '-' in str(rowSeries['amount']) and str(rowSeries['amount']) != '-1.0' and 'cubic meter' in str(rowSeries['unit']):
        x = str(rowSeries['process code']) + ';' + str(rowSeries['name']) + ';' + str(rowSeries['amount']) + ';' + str(rowSeries['unit'])
        with open('landfilledWasteM3.txt', 'a') as f:
            f.write(x + '\n')


# In[44]:


### Reading .txt files into Pandas Dataframes
df3 = pd.read_csv("liquidWaste.txt", sep=';', header=None)
df3.columns = ['process code', 'name', 'amount', 'unit']
df4 = pd.read_csv("solidWaste.txt", sep=';', header=None)
df4.columns = ['process code', 'name', 'amount', 'unit']
df5 = pd.read_csv("hazardWasteKg.txt", sep=';', header=None)
df5.columns = ['process code', 'name', 'amount', 'unit']
df7 = pd.read_csv("nonhazardWasteKg.txt", sep=';', header=None)
df7.columns = ['process code', 'name', 'amount', 'unit']
df8 = pd.read_csv("nonhazardWasteM3.txt", sep=';', header=None)
df8.columns = ['process code', 'name', 'amount', 'unit']
df9 = pd.read_csv("incineratedWasteKg.txt", sep=';', header=None)
df9.columns = ['process code', 'name', 'amount', 'unit']
df10 = pd.read_csv("incineratedWasteM3.txt", sep=';', header=None)
df10.columns = ['process code', 'name', 'amount', 'unit']
df11 = pd.read_csv("recycledWasteKg.txt", sep=';', header=None)
df11.columns = ['process code', 'name', 'amount', 'unit']
df13 = pd.read_csv("compostedWasteKg.txt", sep=';', header=None)
df13.columns = ['process code', 'name', 'amount', 'unit']
df15 = pd.read_csv("landfilledWasteKg.txt", sep=';', header=None)
df15.columns = ['process code', 'name', 'amount', 'unit']


# In[47]:


## Section 5: Testing Process to Append Exchanges for a Specific Process
process = eidb.get('25df23fb456a580f2efc674d4b1f4732')
process.as_dict()


# In[48]:

#%%
for exc in process.exchanges():
    print(exc)


# In[52]:


## Section 6: Appending all Processes with Waste Exchanges with Custom Biosphere Waste Exchanges in Same Amount and Unit as Technosphere Exchange
for i in range(0, df3.shape[0]):
    code1 = df3.iloc[i,0]
    amount1 = df3.iloc[i,2]
    unit1 = df3.iloc[i,3]
    process1 = eidb.get(code1)
    try1 = wd.get("Liquid_waste")
    process1.new_exchange(input=try1.key,amount= amount1,unit= unit1,type='biosphere').save()


# In[53]:


for i in range(0, df4.shape[0]):
    code3 = df4.iloc[i,0]
    amount3 = df4.iloc[i,2]
    unit3 = df4.iloc[i,3]
    process3 = eidb.get(code3)
    try3 = wd.get("Solid_waste")
    process3.new_exchange(input=try3.key,amount= amount3,unit= unit3,type='biosphere').save()


# In[54]:


for i in range(0, df5.shape[0]):
    code4 = df5.iloc[i,0]
    amount4 = df5.iloc[i,2]
    unit4 = df5.iloc[i,3]
    process4 = eidb.get(code4)
    try4 = wd.get("Hazardous_waste_kg")
    process4.new_exchange(input=try4.key,amount= amount4,unit= unit4,type='biosphere').save()


# In[55]:


for i in range(0, df7.shape[0]):
    code6 = df7.iloc[i,0]
    amount6 = df7.iloc[i,2]
    unit6 = df7.iloc[i,3]
    process6 = eidb.get(code6)
    try6 = wd.get("Nonhazardous_waste_kg")
    process6.new_exchange(input=try6.key,amount= amount6,unit= unit6,type='biosphere').save()


# In[56]:


for i in range(0, df8.shape[0]):
    code7 = df8.iloc[i,0]
    amount7 = df8.iloc[i,2]
    unit7 = df8.iloc[i,3]
    process7 = eidb.get(code7)
    try7 = wd.get("Nonhazardous_waste_m3")
    process7.new_exchange(input=try7.key,amount= amount7,unit= unit7,type='biosphere').save()


# In[57]:


for i in range(0, df9.shape[0]):
    code8 = df9.iloc[i,0]
    amount8 = df9.iloc[i,2]
    unit8 = df9.iloc[i,3]
    process8 = eidb.get(code8)
    try8 = wd.get("Incinerated_waste_kg")
    process8.new_exchange(input=try8.key,amount= amount8,unit= unit8,type='biosphere').save()


# In[58]:


for i in range(0, df10.shape[0]):
    code9 = df10.iloc[i,0]
    amount9 = df10.iloc[i,2]
    unit9 = df10.iloc[i,3]
    process9 = eidb.get(code9)
    try9 = wd.get("Incinerated_waste_m3")
    process9.new_exchange(input=try9.key,amount= amount9,unit= unit9,type='biosphere').save()


# In[59]:


for i in range(0, df11.shape[0]):
    code10 = df11.iloc[i,0]
    amount10 = df11.iloc[i,2]
    unit10 = df11.iloc[i,3]
    process10 = eidb.get(code10)
    try10 = wd.get("Recycled_waste_kg")
    process10.new_exchange(input=try10.key,amount= amount10,unit= unit10,type='biosphere').save()


# In[60]:


for i in range(0, df13.shape[0]):
    code11 = df13.iloc[i,0]
    amount11 = df13.iloc[i,2]
    unit11 = df13.iloc[i,3]
    process11 = eidb.get(code11)
    try11 = wd.get("Composted_waste_kg")
    process11.new_exchange(input=try11.key,amount= amount11,unit= unit11,type='biosphere').save()


# In[61]:


for i in range(0, df15.shape[0]):
    code12 = df15.iloc[i,0]
    amount12 = df15.iloc[i,2]
    unit12 = df15.iloc[i,3]
    process12 = eidb.get(code12)
    try12 = wd.get("Landfilled_waste_kg")
    process12.new_exchange(input=try12.key,amount= amount12,unit= unit12,type='biosphere').save()


# In[62]:


### Confirming That the Append was Successful
#g = eidb.get('0c8bd5a75f3ad3e07842825e26eb8b8f')
#for exc in g.exchanges():
#    print(exc)

#%% 

## Section 7: Creating Impact Factors for Liquid and Solid Waste and Setting Characterization Factor to 1
# USER VARIABLES
# the name of the impact category file:
file_name = 'TWDsolid.xlsx'
# the name of the Brightway project to add the impact category to:
project_name = 'ecoinvent-import2'
# the name of the biosphere database in above project:
biosphere_name = 'cstmBiosphere'


def confirmation(question, message=''):
    """Ask user for confirmation [yes/no], return True or False as confirmation.

    An additional message before the question is optional."""
    if len(message) > 0:
        print(message)
    inp = ''
    valid_inp = ['y', 'yes', 'n', 'no']
    first = True
    while inp.lower() not in valid_inp:
        if not first:
            print("    You must answer either 'y' or 'n'.")
        inp = input(question)
        first = False
    if inp.lower() in valid_inp[:2]:
        return True
    else:
        return False


# ask user to confirm adding impact category
m = "\n+++ This script will add the impact category 'Solid Waste' to Brightway2\n"     "    This script will use the following variables:\n"     "    > impact category file:    {}\n"     "    > Brightway project name : {}\n"     "    > Biosphere database name: {}\n"     "    If you wish to change one of the above variables, cancel the script now".format(file_name, project_name, biosphere_name)
q = '\n+++ continue? [y/n]: '
cont = confirmation(question=q, message=m)
if not cont:
    print("+++ To change variables, open this script in a text editor (like notepad) and change the \n"
          "    variable names under the header '# USER VARIABLES' near the top of the file.")
    raise Exception('USER EXIT')
    exit()

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
    method_name = ('Waste Footprint', 'Total Waste Demand', 'Solid Waste')
    print('+++ Adding the new impact category to Brightway...')
    m = bw2data.Method(method_name)
    m.register(description="For Estimating Total Waste Demand of a Process", unit='kg')
    m.write(new_method)
    print('+++ Success!')
    print('    The impact category was added with the name: {}'.format(str(method_name)))
    print('    Exiting script')
except:
    print('\n+++ There was a problem adding the impact category to Brightway, contact Brightway developers')


# In[64]:


# USER VARIABLES
# the name of the impact category file:
file_name = 'TWDliquid.xlsx'
# the name of the Brightway project to add the impact category to:
project_name = 'ecoinvent-import2'
# the name of the biosphere database in above project:
biosphere_name = 'cstmBiosphere'


def confirmation(question, message=''):
    """Ask user for confirmation [yes/no], return True or False as confirmation.

    An additional message before the question is optional."""
    if len(message) > 0:
        print(message)
    inp = ''
    valid_inp = ['y', 'yes', 'n', 'no']
    first = True
    while inp.lower() not in valid_inp:
        if not first:
            print("    You must answer either 'y' or 'n'.")
        inp = input(question)
        first = False
    if inp.lower() in valid_inp[:2]:
        return True
    else:
        return False


# ask user to confirm adding impact category
m = "\n+++ This script will add the impact category 'Liquid Waste' to Brightway2\n"     "    This script will use the following variables:\n"     "    > impact category file:    {}\n"     "    > Brightway project name : {}\n"     "    > Biosphere database name: {}\n"     "    If you wish to change one of the above variables, cancel the script now".format(file_name, project_name, biosphere_name)
q = '\n+++ continue? [y/n]: '
cont = confirmation(question=q, message=m)
if not cont:
    print("+++ To change variables, open this script in a text editor (like notepad) and change the \n"
          "    variable names under the header '# USER VARIABLES' near the top of the file.")
    raise Exception('USER EXIT')
    exit()

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


# In[65]:


# USER VARIABLES
# the name of the impact category file:
file_name = 'TWDlandfill.xlsx'
# the name of the Brightway project to add the impact category to:
project_name = 'ecoinvent-import2'
# the name of the biosphere database in above project:
biosphere_name = 'cstmBiosphere'


def confirmation(question, message=''):
    """Ask user for confirmation [yes/no], return True or False as confirmation.

    An additional message before the question is optional."""
    if len(message) > 0:
        print(message)
    inp = ''
    valid_inp = ['y', 'yes', 'n', 'no']
    first = True
    while inp.lower() not in valid_inp:
        if not first:
            print("    You must answer either 'y' or 'n'.")
        inp = input(question)
        first = False
    if inp.lower() in valid_inp[:2]:
        return True
    else:
        return False


# ask user to confirm adding impact category
m = "\n+++ This script will add the impact category 'Total Waste Demand' to Brightway2\n"     "    This script will use the following variables:\n"     "    > impact category file:    {}\n"     "    > Brightway project name : {}\n"     "    > Biosphere database name: {}\n"     "    If you wish to change one of the above variables, cancel the script now".format(file_name, project_name, biosphere_name)
q = '\n+++ continue? [y/n]: '
cont = confirmation(question=q, message=m)
if not cont:
    print("+++ To change variables, open this script in a text editor (like notepad) and change the \n"
          "    variable names under the header '# USER VARIABLES' near the top of the file.")
    raise Exception('USER EXIT')
    exit()

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
    matches = bs[(bs['name'] == row[1]['name']) & (bs['unit'] == row[1]['unit'])]
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
    method_name = ('Waste Footprint', 'Total Waste Demand', 'Landfilled Waste')
    print('+++ Adding the new impact category to Brightway...')
    m = bw2data.Method(method_name)
    m.register(description="For Estimating Total Waste Demand of a Process", unit='kg/m3')
    m.write(new_method)
    print('+++ Success!')
    print('    The impact category was added with the name: {}'.format(str(method_name)))
    print('    Exiting script')
except:
    print('\n+++ There was a problem adding the impact category to Brightway, contact Brightway developers')


# In[66]:


# USER VARIABLES
# the name of the impact category file:
file_name = 'TWDincinerate.xlsx'
# the name of the Brightway project to add the impact category to:
project_name = 'ecoinvent-import2'
# the name of the biosphere database in above project:
biosphere_name = 'cstmBiosphere'


def confirmation(question, message=''):
    """Ask user for confirmation [yes/no], return True or False as confirmation.

    An additional message before the question is optional."""
    if len(message) > 0:
        print(message)
    inp = ''
    valid_inp = ['y', 'yes', 'n', 'no']
    first = True
    while inp.lower() not in valid_inp:
        if not first:
            print("    You must answer either 'y' or 'n'.")
        inp = input(question)
        first = False
    if inp.lower() in valid_inp[:2]:
        return True
    else:
        return False


# ask user to confirm adding impact category
m = "\n+++ This script will add the impact category 'Total Waste Demand' to Brightway2\n"     "    This script will use the following variables:\n"     "    > impact category file:    {}\n"     "    > Brightway project name : {}\n"     "    > Biosphere database name: {}\n"     "    If you wish to change one of the above variables, cancel the script now".format(file_name, project_name, biosphere_name)
q = '\n+++ continue? [y/n]: '
cont = confirmation(question=q, message=m)
if not cont:
    print("+++ To change variables, open this script in a text editor (like notepad) and change the \n"
          "    variable names under the header '# USER VARIABLES' near the top of the file.")
    raise Exception('USER EXIT')
    exit()

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
    matches = bs[(bs['name'] == row[1]['name']) & (bs['unit'] == row[1]['unit'])]
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
    method_name = ('Waste Footprint', 'Total Waste Demand', 'Incinerated Waste')
    print('+++ Adding the new impact category to Brightway...')
    m = bw2data.Method(method_name)
    m.register(description="For Estimating Total Waste Demand of a Process", unit='kg/m3')
    m.write(new_method)
    print('+++ Success!')
    print('    The impact category was added with the name: {}'.format(str(method_name)))
    print('    Exiting script')
except:
    print('\n+++ There was a problem adding the impact category to Brightway, contact Brightway developers')


# In[67]:


# USER VARIABLES
# the name of the impact category file:
file_name = 'TWDrecycle.xlsx'
# the name of the Brightway project to add the impact category to:
project_name = 'ecoinvent-import2'
# the name of the biosphere database in above project:
biosphere_name = 'cstmBiosphere'


def confirmation(question, message=''):
    """Ask user for confirmation [yes/no], return True or False as confirmation.

    An additional message before the question is optional."""
    if len(message) > 0:
        print(message)
    inp = ''
    valid_inp = ['y', 'yes', 'n', 'no']
    first = True
    while inp.lower() not in valid_inp:
        if not first:
            print("    You must answer either 'y' or 'n'.")
        inp = input(question)
        first = False
    if inp.lower() in valid_inp[:2]:
        return True
    else:
        return False


# ask user to confirm adding impact category
m = "\n+++ This script will add the impact category 'Total Waste Demand' to Brightway2\n"     "    This script will use the following variables:\n"     "    > impact category file:    {}\n"     "    > Brightway project name : {}\n"     "    > Biosphere database name: {}\n"     "    If you wish to change one of the above variables, cancel the script now".format(file_name, project_name, biosphere_name)
q = '\n+++ continue? [y/n]: '
cont = confirmation(question=q, message=m)
if not cont:
    print("+++ To change variables, open this script in a text editor (like notepad) and change the \n"
          "    variable names under the header '# USER VARIABLES' near the top of the file.")
    raise Exception('USER EXIT')
    exit()

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
    matches = bs[(bs['name'] == row[1]['name']) & (bs['unit'] == row[1]['unit'])]
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
    method_name = ('Waste Footprint', 'Total Waste Demand', 'Recycled Waste')
    print('+++ Adding the new impact category to Brightway...')
    m = bw2data.Method(method_name)
    m.register(description="For Estimating Total Waste Demand of a Process", unit='kg/m3')
    m.write(new_method)
    print('+++ Success!')
    print('    The impact category was added with the name: {}'.format(str(method_name)))
    print('    Exiting script')
except:
    print('\n+++ There was a problem adding the impact category to Brightway, contact Brightway developers')


# In[68]:


# USER VARIABLES
# the name of the impact category file:
file_name = 'TWDcompost.xlsx'
# the name of the Brightway project to add the impact category to:
project_name = 'ecoinvent-import2'
# the name of the biosphere database in above project:
biosphere_name = 'cstmBiosphere'


def confirmation(question, message=''):
    """Ask user for confirmation [yes/no], return True or False as confirmation.

    An additional message before the question is optional."""
    if len(message) > 0:
        print(message)
    inp = ''
    valid_inp = ['y', 'yes', 'n', 'no']
    first = True
    while inp.lower() not in valid_inp:
        if not first:
            print("    You must answer either 'y' or 'n'.")
        inp = input(question)
        first = False
    if inp.lower() in valid_inp[:2]:
        return True
    else:
        return False


# ask user to confirm adding impact category
m = "\n+++ This script will add the impact category 'Total Waste Demand' to Brightway2\n"     "    This script will use the following variables:\n"     "    > impact category file:    {}\n"     "    > Brightway project name : {}\n"     "    > Biosphere database name: {}\n"     "    If you wish to change one of the above variables, cancel the script now".format(file_name, project_name, biosphere_name)
q = '\n+++ continue? [y/n]: '
cont = confirmation(question=q, message=m)
if not cont:
    print("+++ To change variables, open this script in a text editor (like notepad) and change the \n"
          "    variable names under the header '# USER VARIABLES' near the top of the file.")
    raise Exception('USER EXIT')
    exit()

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
    matches = bs[(bs['name'] == row[1]['name']) & (bs['unit'] == row[1]['unit'])]
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
    method_name = ('Waste Footprint', 'Total Waste Demand', 'Composted Waste')
    print('+++ Adding the new impact category to Brightway...')
    m = bw2data.Method(method_name)
    m.register(description="For Estimating Total Waste Demand of a Process", unit='kg/m3')
    m.write(new_method)
    print('+++ Success!')
    print('    The impact category was added with the name: {}'.format(str(method_name)))
    print('    Exiting script')
except:
    print('\n+++ There was a problem adding the impact category to Brightway, contact Brightway developers')


# In[69]:


# USER VARIABLES
# the name of the impact category file:
file_name = 'TWDhazard.xlsx'
# the name of the Brightway project to add the impact category to:
project_name = 'ecoinvent-import2'
# the name of the biosphere database in above project:
biosphere_name = 'cstmBiosphere'


def confirmation(question, message=''):
    """Ask user for confirmation [yes/no], return True or False as confirmation.

    An additional message before the question is optional."""
    if len(message) > 0:
        print(message)
    inp = ''
    valid_inp = ['y', 'yes', 'n', 'no']
    first = True
    while inp.lower() not in valid_inp:
        if not first:
            print("    You must answer either 'y' or 'n'.")
        inp = input(question)
        first = False
    if inp.lower() in valid_inp[:2]:
        return True
    else:
        return False


# ask user to confirm adding impact category
m = "\n+++ This script will add the impact category 'Total Waste Demand' to Brightway2\n"     "    This script will use the following variables:\n"     "    > impact category file:    {}\n"     "    > Brightway project name : {}\n"     "    > Biosphere database name: {}\n"     "    If you wish to change one of the above variables, cancel the script now".format(file_name, project_name, biosphere_name)
q = '\n+++ continue? [y/n]: '
cont = confirmation(question=q, message=m)
if not cont:
    print("+++ To change variables, open this script in a text editor (like notepad) and change the \n"
          "    variable names under the header '# USER VARIABLES' near the top of the file.")
    raise Exception('USER EXIT')
    exit()

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
    matches = bs[(bs['name'] == row[1]['name']) & (bs['unit'] == row[1]['unit'])]
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
    method_name = ('Waste Footprint', 'Total Waste Demand', 'Hazardous Waste')
    print('+++ Adding the new impact category to Brightway...')
    m = bw2data.Method(method_name)
    m.register(description="For Estimating Total Waste Demand of a Process", unit='kg/m3')
    m.write(new_method)
    print('+++ Success!')
    print('    The impact category was added with the name: {}'.format(str(method_name)))
    print('    Exiting script')
except:
    print('\n+++ There was a problem adding the impact category to Brightway, contact Brightway developers')


# In[70]:


# USER VARIABLES
# the name of the impact category file:
file_name = 'TWDnonhazard.xlsx'
# the name of the Brightway project to add the impact category to:
project_name = 'ecoinvent-import2'
# the name of the biosphere database in above project:
biosphere_name = 'cstmBiosphere'


def confirmation(question, message=''):
    """Ask user for confirmation [yes/no], return True or False as confirmation.

    An additional message before the question is optional."""
    if len(message) > 0:
        print(message)
    inp = ''
    valid_inp = ['y', 'yes', 'n', 'no']
    first = True
    while inp.lower() not in valid_inp:
        if not first:
            print("    You must answer either 'y' or 'n'.")
        inp = input(question)
        first = False
    if inp.lower() in valid_inp[:2]:
        return True
    else:
        return False


# ask user to confirm adding impact category
m = "\n+++ This script will add the impact category 'Total Waste Demand' to Brightway2\n"     "    This script will use the following variables:\n"     "    > impact category file:    {}\n"     "    > Brightway project name : {}\n"     "    > Biosphere database name: {}\n"     "    If you wish to change one of the above variables, cancel the script now".format(file_name, project_name, biosphere_name)
q = '\n+++ continue? [y/n]: '
cont = confirmation(question=q, message=m)
if not cont:
    print("+++ To change variables, open this script in a text editor (like notepad) and change the \n"
          "    variable names under the header '# USER VARIABLES' near the top of the file.")
    raise Exception('USER EXIT')
    exit()

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
    matches = bs[(bs['name'] == row[1]['name']) & (bs['unit'] == row[1]['unit'])]
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
    method_name = ('Waste Footprint', 'Total Waste Demand', 'NonHazardous Waste')
    print('+++ Adding the new impact category to Brightway...')
    m = bw2data.Method(method_name)
    m.register(description="For Estimating Total Waste Demand of a Process", unit='kg/m3')
    m.write(new_method)
    print('+++ Success!')
    print('    The impact category was added with the name: {}'.format(str(method_name)))
    print('    Exiting script')
except:
    print('\n+++ There was a problem adding the impact category to Brightway, contact Brightway developers')

