import math

n = int(input().replace(";", ""))

numberOfFit = 0
for i in range(0, n):
    line = input()
    line = line.replace(";", "")
    line = line.split(",")
    areaCylinder = math.pi * math.pow(int(line[0]), 2)
    if(line[1] == "3"):
        # Do code for triangle
        radiusTriangle = int(line[2]) / math.sqrt(3)
        areaTriangle = math.pi * math.pow(radiusTriangle, 2)
        if(areaTriangle < areaCylinder):
            numberOfFit = numberOfFit + 1
    else:
        # Do code for rectangle
        radiusRectangle = int(line[2]) * math.sqrt(2) / 2
        areaRectangle = math.pi * math.pow(radiusRectangle, 2)
        if(areaRectangle < areaCylinder):
            numberOfFit = numberOfFit + 1
            
print(numberOfFit)
