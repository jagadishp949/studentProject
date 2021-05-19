"""
Implement a group_by_owners function that:

·         Accepts a dictionary containing the file owner name for each file name.

·         Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

"""

def group_by_owners(data):
    ownerdict = {}
    for key, value in data.items():
        if value in ownerdict:
          ownerdict[value].append(key)
        else:
          ownerdict[value] = [key]
    return ownerdict

data = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(data))
