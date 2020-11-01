# Not sure how this works...but it did. Seems to just create an object
# that can be managed and accessed through here, but not directly using any of the applications
# that I have installed.

import dbm
import pickle
database = dbm.open("fruits", 'c')
database['1'] = 'apple'

database['2'] = pickle.dumps(('peach', 'orange', 'grape'))



print(database['1'])
print(database['2'])
print(pickle.loads(database['2']))
database.close()