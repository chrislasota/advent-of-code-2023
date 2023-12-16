# Advent of Code 2023
# Day 15
# Part 2

def compute_hash(input_str):
    current = 0
    for ch in input_str:
        current = ((current + ord(ch)) * 17) % 256
    return current


def main() -> int:
    focusing_power = 0
    boxes = []
    for i in range(256):
        boxes.append([])
    with open("input_day_15.txt") as input_file:
        # the file is a SINGLE enormous line of continuous text characters
        line = input_file.readline()

    line = line.rstrip()   # remove newline
    labels = line.split(',')
    for label in labels:
        if '=' in label:
           action = label[-2]
        else:
           action = label[-1]
        label_name = label[:label.find(action)]
        which_box = compute_hash(label_name)
        lens_list = boxes[which_box]

        if action == '-':
            for index in range(len(lens_list)):
                if lens_list[index][0] == label_name:
                    lens_list.pop(index)
                    boxes[which_box] = lens_list
                    break

        if action == '=':
            lens_focus = int(label[-1])
            found_it = False
            for index in range(len(lens_list)):
                if lens_list[index][0] == label_name:
                    lens_list[index][1] = lens_focus
                    found_it = True
                    break
            if found_it == False:
                lens_list.append([label_name, lens_focus])

    for box_index in range(256):
        for lens_index in range(len(boxes[box_index])):
            focusing_power += (box_index + 1) * (lens_index + 1) * boxes[box_index][lens_index][1]

    return focusing_power


if __name__ == "__main__":
    print(f"The total focusing power is : {main()}")
