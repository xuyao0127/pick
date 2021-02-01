PICK 2.0
========

# Requirement
Python 3.6+

# Run
'''
python pick.py [command]
'''

## Add a resturant
'''
python pick.py add [name]
'''
Add [name] to the list. New resturant's weight will be the same as the highest one in the list.

## Remove a resturant
'''
python pick.py remove [name]
'''
Remove [name] to the list.

## Pick a resturant
'''
python pick.py pick
'''
Pick a resturant the list.

## List resturants
'''
python pick.py list
'''
List all added resturants and its weight.

## Reset resturants' weight
'''
python pick.py reset
'''
Reset all resturants' weight to 1.

# Manual config
The script will automatically generates a config file "resturants.json". You can update or backup the file manually. The key is resturant's name and the value is the weight (larger than 0)