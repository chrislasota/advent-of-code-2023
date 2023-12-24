# Advent of Code 2023
# Day 24
# Part 1

import re

def process_input_line(line_str):
    physics_filter = re.compile('[-]*\d+')
    data = physics_filter.findall(line_str)
    for index in range(6):
        data[index] = int(data[index])
    position = data[:3]
    velocity = data[3:]
    return position, velocity


def main() -> int:
    number_of_intersections = 0
    test_area_x_low = test_area_y_low = 200000000000000
    test_area_x_high = test_area_y_high = 400000000000000
    positions = []
    velocities = []
    with open("input_day_24.txt") as input_file:
        for line in input_file:
           line = line.rstrip()   # remove newline chars
           position, velocity = process_input_line(line)
           positions.append(position)
           velocities.append(velocity)

    # find tentative intersections
    how_many_hailstones = len(positions)
    for first in range(how_many_hailstones):
        for second in range(first + 1, how_many_hailstones):
            xA = positions[first][0]
            yA = positions[first][1]
            xB = positions[second][0]
            yB = positions[second][1]
            vAx = velocities[first][0]
            vAy = velocities[first][1]
            vBx = velocities[second][0]
            vBy = velocities[second][1]
            A_velocity_ratio = vAy / vAx
            B_velocity_ratio = vBy / vBx

            # skip any hailstones moving parallel to each other
            if A_velocity_ratio == B_velocity_ratio:
                continue

            x_intersect = ((yB - yA) - (xB * B_velocity_ratio) + (xA * A_velocity_ratio)) / (A_velocity_ratio - B_velocity_ratio)
            y_intersect = yA + (x_intersect - xA) * A_velocity_ratio

            # check if intersection occurs in past (t < 0)
            if ((x_intersect - xA) / vAx) < 0 or ((x_intersect - xB) / vBx) < 0:
                continue

            # check if intersection occurs in test area
            x_inside = False
            y_inside = False
            if x_intersect >= test_area_x_low and x_intersect <= test_area_x_high:
                x_inside = True
            if y_intersect >= test_area_y_low and y_intersect <= test_area_y_high:
                y_inside = True
            if x_inside and y_inside:
                number_of_intersections += 1

    return number_of_intersections


if __name__ == "__main__":
    print(f"The number of intersections occuring in the test area is : {main()}")
