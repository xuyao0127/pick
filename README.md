PICK 2.0
========

## Requirement
Python 3

## Run
On Linux/macOS, you can use `chmod +x pick.py` to give executive permission
to run this script without the prifixing `python` command.

```
python pick.py [command]
```

### Add a restaurant
```
python pick.py add [name]
```
Add [name] to the list. New restaurant's weight will be the same as the highest one in the list.

### Remove a restaurant
```
python pick.py remove [name]
```
Remove [name] to the list.

### Pick a restaurant
```
python pick.py pick
```
Pick a restaurant the list.

### List restaurants
```
python pick.py list
```
List all added restaurants and its weight.

### Reset restaurants' weights
```
python pick.py reset
```
Reset all restaurants' weights to 1.

## Manual config
The script will automatically generates a config file "restaurants.json". You can update or backup the file manually. The key is restaurant's name and the value is the weight (larger than 0)
