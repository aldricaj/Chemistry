# This program will solve Gas Law problems
# Author: A Aldrich
# Last Change: 2015.10.21

gas_constant = 22.4/273 # gas constant in mol * K/(atm * L)

print('Enter a <?> for any unkown value.')

# Get input from user
pressure = input('P(atm) = ')
volume = input('V(L) = ')

n_mols = input('n(mol) = ')
temp = input('T(K) = ')

# Find out what the unkown is
if(pressure == '?'):
    # Convert known values into floats
    volume = float(volume)
    n_mols = float(n_mols)
    temp = float(temp)
    pressure = 0.0

    # Solve
    pressure = n_mols * gas_constant * temp / volume # P = nRT/V
    
    print('The pressure is ' + str(pressure) + ' atm.')
elif(volume == '?'):
    # Convert known values into floats
    pressure = float(pressure)
    n_mols = float(n_mols)
    temp = float(temp)

    # Solve
    volume = n_mols * gas_constant * temp / pressure # V = nRT/P

    print('The volume is ' + str(volume) + ' L.')
elif(n_mols == '?'):
    # Convert known values into floats
    pressure = float(pressure)
    volume = float(volume)
    temp = float(temp)

    # Solve
    n_mols = pressure * volume / (gas_constant * temp) # n = PV/(RT)

    print('The number of moles is ' + n_mols + ' mol.')
elif(temp == '?'):
    # Convert known values into floats
    pressure = float(pressure)
    volume = float(volume)
    n_mols = float(n_mols)

    # Solve
    temp = pressure * volume / (gas_constant * n_mols) # T = PV/(nR)
    print('The tempeture is ' + str(temp) + ' K.')
