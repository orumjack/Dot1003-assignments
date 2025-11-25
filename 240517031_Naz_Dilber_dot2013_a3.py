def spruce():
    height = int(input("Spruce height: "))
    box_size = int(input("Box Size: "))

    print("-" * box_size)

    print("|" + " " * (box_size - 2) + "|")

    for i in range(1, height + 1):
        stars = "*" * (2 * i - 1)
        left_padding = (box_size - 2 - len(stars)) // 2
        line = "|" + " " * left_padding + stars + " " * (box_size - 2 - left_padding - len(stars)) + "|"
        print(line)

    trunk_padding = (box_size - 2 - 1) // 2
    trunk_line = "|" + " " * trunk_padding + "*" + " " * (box_size - 2 - trunk_padding - 1) + "|"
    print(trunk_line)

    print("-" * box_size)


spruce()