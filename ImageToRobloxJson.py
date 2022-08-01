from PIL import Image
from numpy import asarray

image = Image.open('example.png')
numpydata = asarray(image)
file = open("output.txt", "w")

count = 0
nub2 = 0
file.write("[\n")
for x in numpydata:
    file.write("[\n")
    nub2 = nub2+1
    nub = 0
    for y in x:
        nub = nub+1
        if nub >= len(x):
            file.write("[\n")
            file.write(str(y[0]) + ", " + str(y[1]) + ", " +  str(y[2]))
            count += 1
            file.write("\n]")
        else:
            file.write("[\n")
            file.write(str(y[0]) + ", " + str(y[1]) + ", " +  str(y[2]))
            count += 1
            file.write("\n],")
    if nub2 >= len(numpydata):
        file.write("\n]")
    else:
        file.write("\n],")
file.write("]")
file.close()
