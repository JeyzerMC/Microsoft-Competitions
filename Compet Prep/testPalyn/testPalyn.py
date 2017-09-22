stri = "axbawbaseksqke"

lengthA = 0
lengthB = 0
posI = 0

for i in stri:
    substr = ""
    pos = stri.find(i, posI+1)
    if pos != -1:
        strD = stri[posI: pos+1]
        print(strD[::-1])
    posI+= 1
