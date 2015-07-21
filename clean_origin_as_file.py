# GOAL:
# Clean file origin_as_mapping
# Write output in clean_origin_as_mapping.txt
# Takes data from 3303.txt

prefixes_3303 = {}

with open('3303.txt', 'rb') as txt:

    for line in txt:
        if not line.startswith("#"):
            elements = line.split(" ")
            prefixes_3303[elements[0]] = elements[0]

with open("clean_origin_as_mapping.txt", "wb") as output:
    with open("origin_as_mapping.txt", "r") as input:
        for line in input:
            elements = line.split(" ")
            elements[1] = elements[1].lstrip()
            elements[1] = elements[1].rstrip('\r\n')
            if elements[1] != "3303":
                output.write(line)

    for prefix in prefixes_3303:
        new_line = prefix + " 3303\n"
        output.write(new_line)
