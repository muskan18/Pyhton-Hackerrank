In this task, you will store the weights of a family of a four weighing of 70, 80, 45 and 50 kg
respectively in a list and perform do some operations on it to calculate the mean of the weights.

======================code====================
# Code starts here
weights=[70,80,45,50]
# create list of weights

maximum = max(weights)
# maximum weight
print(maximum)
weights[2] = 48
print(weights)
# change values
total = sum(weights)
print(total)
# calculate sum
element = len(weights)
mean = total/element
# calculate mean
print(mean)
# Code ends here
