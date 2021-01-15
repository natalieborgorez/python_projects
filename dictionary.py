# Code by Natalie Borgorez

inventory = {'silver': 1000, 'handbag': ['handkerchief', 'lighter', 'hand gel'],
             'backpack': ['bottle', 'dagger', 'Raspberry Pi', 'portable charger'],
             'burlap bag': ['banana', 'chocolate sweets', 'three-toed sloth']}

# Adding a key 'pocket' and assigning a list to it
inventory['pocket'] = ['seashell', 'bluberry', 'mint']

# Adding up 50 quid to the 'silver' key with the value of 1000
inventory['silver'] += 50

# Sorting the list found under the key 'handbag'
inventory['handbag'].sort()

# Remove a value out of the 'backpack' key
inventory['backpack'].remove('dagger')

# Sorting the list after removing the dagger
inventory['backpack'].sort()

# Sorting and printing out the list starting out from its end
sorted(inventory, reverse=True)

print("Your dictionary is as follows: \n"+str(inventory))

# Making the printed dictionary look nice and neat
print("\nYour nice and neat dictionary: \n")
for key, value in dict.items(inventory):
        print("%s --> %s"%(value, key))

# Code by Natalie Borgorez
