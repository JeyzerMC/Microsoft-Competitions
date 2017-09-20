with open("input.txt") as i:
    for line in i:
        # Code start here
        palyndrome = ""
        line = line.split()
        pos = -1
        for word in range(len(line)):
            for letter in range(len(word)):
                pos = line.find(letter, pos + 1)
                if pos == -1
                    break
