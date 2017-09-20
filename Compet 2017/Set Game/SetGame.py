n = int(input())

count = ['1', '2', '3']
shading = ['E', 'F', 'S']
color = ['G', 'P', 'R']
shape = ['O', 'D', 'S']

for i in range(0,n):
    count = ['1', '2', '3']
    shading = ['E', 'F', 'S']
    color = ['G', 'P', 'R']
    shape = ['O', 'D', 'S']

    line = input().split()
    a = line[0]
    b = line[1]
    output = "Group " + str(i + 1) + ": "
    for i in range(len(a)):
        if(i == 0):
            if(count.index(a[i]) == count.index(b[i])):
                output = output + a[i]
            else:
                count.pop(count.index(a[i]))
                count.pop(count.index(b[i]))
                output = output + count[0]

        if(i == 1):
            if(shading.index(a[i]) == shading.index(b[i])):
                output = output + a[i]
            else:
                shading.pop(shading.index(a[i]))
                shading.pop(shading.index(b[i]))
                output = output + shading[0]

        if(i == 2):
            if(color.index(a[i]) == color.index(b[i])):
                output = output + a[i]
            else:
                color.pop(color.index(a[i]))
                color.pop(color.index(b[i]))
                output = output + color[0]

        if(i == 3):
            if(shape.index(a[i]) == shape.index(b[i])):
                output = output + a[i]
            else:
                shape.pop(shape.index(a[i]))
                shape.pop(shape.index(b[i]))
                output = output + shape[0]
        
    print(output)