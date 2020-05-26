In this task, you will understand how to create a dictionary that stores a fruit as a key and its color as values.
Perform some common dictionary operations so that each fruit is correctly matched to its color.

=======================Code=======================

# Code starts here
fruits = {'apple':'green','banana':'yellow','cherry':'red'}

# initialize dictionary


# change color of apple
fruits['apple'] = 'red'

# add guava

d={'guava':'green'}
fruits.update(d)
# delete cherry
del fruits['cherry']

# display fruits
print(fruits)

# Code ends here
