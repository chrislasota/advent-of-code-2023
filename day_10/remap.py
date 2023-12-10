# convert the ugly input file into something more visually appealing
# using unicode characters for drawing windows on text-based terminals

remap_dict_1 = {'|': "\u2551",
                '-': "\u2550",
                'L': "\u255a",
                'J': "\u255d",
                '7': "\u2557",
                'F': "\u2554",
                '.': ' ',
                'S': '\u2588'
}

remap_dict_2 = {'|': "\u2502",
                '-': "\u2500",
                'L': "\u2514",
                'J': "\u2518",
                '7': "\u2510",
                'F': "\u250c",
                '.': ' ',
                'S': '\u2588'
}

remap_dict_3 = {'|': "\u2503",
                '-': "\u2501",
                'L': "\u2517",
                'J': "\u251b",
                '7': "\u2513",
                'F': "\u250f",
                '.': ' ',
                'S': '\u2588'
}



with open("input_day_10.txt",'r') as input_file:
    for line in input_file:
        line = line.rstrip()
        for c in line:
            print(remap_dict_2[c], end='')
        print()

# just pipe the output to a text file
