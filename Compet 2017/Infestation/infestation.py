n = input()
w, h = int(len(n)-1), int(len(n)-1)

Matrix = [[0 for x in range(w)] for y in range(h)]

for j in range(h):
    Matrix[0][j] = n[j]

for i in range(1,h):
    line = input()
    for j in range(0,w):
        Matrix[i][j] = line[j]

for k in range(0, h):
    for i in range(1,h):
        for j in range(1,w):
            boi = 0
            if(i > 0 and Matrix[i-1][j] == "1"):
                boi = boi + 1
            if(i < w - 1 and Matrix[i+1][j] == "1"):
                boi = boi + 1
            if(j> 0 and Matrix[i][j-1] == "1"):
                boi = boi + 1 
            if(j < w - 1 and Matrix[i][j+1] == "1"):
                boi = boi + 1
            
            if(boi > 1):
                Matrix[i][j] = "1"


for i in range(0,h):
    for j in range(0,w):
        print(Matrix[i][j], end="")
    print("")