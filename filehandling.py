# filepath is already given to you
filepath = text_file

# Code starts here
f= open(filepath,'r')
# open file in read mode

# iterate over the file object

# close the file

f.close()
# open file in write mode
nf = open(filepath,'a+')

nf.write("Successfully written to the text file.")
# write to the file

nf.close()
# close the file
# Code ends here

# Caution : do not delete this code
file = open(filepath,'r')
lines=[]
for line in file.readlines():
    lines.append(line)
file.close()


print(len(lines))
