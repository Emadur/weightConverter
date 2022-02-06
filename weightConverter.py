# This program converts the user's weight from lbs to kg
# User is asked to input "l" or "k"
# Program then converts lbs to kg or kg to lbs based on what the user inputs

weight = input("Weight: ")
kg_to_lbs = float(weight) * 2.2
lbs_to_kg = float(weight) * 0.45
lbs_or_kg = input(f'(L)bs or (K)g: ')

if lbs_or_kg.__contains__('L') or lbs_or_kg.__contains__('l'):
    print(f'You are {lbs_to_kg} kilos')
elif lbs_or_kg.__contains__('K') or lbs_or_kg.__contains__('k'):
    print(f'You are {kg_to_lbs} pounds')
