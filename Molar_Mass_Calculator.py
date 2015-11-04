# Calculates molar mass of a compound 
#   Requires:  molar_mass.txt
# Author: Andrew Aldrich
# Created: 2015.10.21
# Edits:
#   - 2015.11.4
#       * removed parse_compound()
#       * implemented use of Chem_Parsing_Function module
import Chem_Parsing_Functions
from Chem_Parsing_Functions import parse_compound

# Calculates molar mass using expanded compound from parse_compound()
# returns a float
def calc_molar_mass(str_expanded_compound):
    molar_mass = 0
    for element in str_expanded_compound:
        if type(element[0]) is not list: # see if the program has reached the bottom of the recursion
            molar_mass = molar_mass + mass_dict[element[0]] * element[1]
        else:
            molar_mass = molar_mass + calc_molar_mass(element[0:len(element)-2]) * element[len(element)-1]
    return molar_mass

# Load molar masses of elemements
directory = 'C://Users//Andrew//Documents//Python//Chemistry//data//molar_mass.txt'
mass_data = open(directory, 'r').readlines()

# Create dictionary for the molar mass data
global mass_dict
mass_dict = {}
for element in mass_data:
    if(element == '\n'): # continues if the line is empty
        continue
    
    # Seperate chem symbol and molar mass
    t_index = element.find('\t')
    element = element.lstrip()
    name = element[0:t_index]
    number = element[t_index+1:]

    # Add to dictionary
    mass_dict[name] = float(number)
# Loop until user is done
while(True):

    # Get compound name from user
    compound = input('Compound name: ')

    expanded_compound = parse_compound(compound)
    
    molar_mass = calc_molar_mass(expanded_compound)
    print('The molar mass of compound is: ' + str(molar_mass) + ' g/mol')
        
    
    # Ask user if they want to quit
    exit_prompt = input('Do you want to quit? (y/n) ')
    if(exit_prompt.lower() == 'y'):
        break























