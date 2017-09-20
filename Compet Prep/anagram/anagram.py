while True:
    try:
        line = input()

        a, b = line.split(",")

        a = list(filter(lambda x: x.isalpha(), sorted(a.lower())))
        b = list(filter(lambda x: x.isalpha(), sorted(b.lower())))

        print("Valid Pattern" if a == b else "Invalid Pattern")

    except EOFError:
        break