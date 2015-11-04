# This script contains various functions to parse chemicals
#   Required files: none
# Author: Andrew Aldrich
# Created on: 2015.11.4
# Edits:
#   - 

# Parses a comppound and returns it in a list of lists retaining the definition of any
#   polyatomic ions
# Return for input: Na2(OH)2 = [ [Na,2],[ [ [ (O,1],[H,1] ],2 ] ]
def parse_compound(str_name):
    expanded_compound = []

    # Parse the compound
    index = 0
    if not str_name[len(str_name)-1].isnumeric(): # Solve index bounds error
        str_name = str_name + '1'
    while index < len(str_name):
        element_name = 'null'
        coef = -1
        if str_name[index] == '(': # Checks for a poly-ion
            # Find end paranthese(-1 for start +1 for end)
            parentheses = -1
            index2 = index+1
            while parentheses  != 0: 
                if str_name[index2] == '(':
                    parentheses = parentheses - 1
                if str_name[index2] == ')':
                    parentheses = parentheses + 1
                index2 = index2 + 1
                if(index2 > len(str_name)):
                    print('Error: Unbalenced Parentheses')
                    break; 
            # Recursively finds EQ for poly-ion
            element_name = parse_compound(str_name[index+1:index2-1])
            index = index2
            
        elif str_name[index].isalpha(): # Check for compound name
            if str_name[index+1].islower(): # Cover case for 2 letter element name
                element_name = str_name[index:index+2]
                index = index + 2
            else:
                element_name = str_name[index]
                index = index +1
            
        if element_name != 'null': # determines if a name has been found and resets
            if str_name[index].isnumeric():
                coef = float(str_name[index])
            else:
                coef = 1
            expanded_compound.append([element_name, coef])
            element_name = 'null'
        else:
            index = index + 1
    return expanded_compound
