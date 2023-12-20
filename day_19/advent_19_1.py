# Advent of Code 2023
# Day 19
# Part 1

import re

def process_rating(rating_str):
    # returns part ratings as an ordered list of integer values: [x, m, a, s]
    rating_filter = re.compile('\d+')
    values_list = rating_filter.findall(rating_str)
    for index in range(4):
        values_list[index] = int(values_list[index])
    return values_list


def process_workflow(workflow_str):
    dissected_workflows_dict = {}
    workflow_index = workflow_str.find('{')
    this_workflow_name = workflow_str[:workflow_index]
    this_workflow_actions = workflow_str[workflow_index + 1 : -1]
    this_workflow_conditionals = this_workflow_actions.split(',')
    dict_list = []
    for item in this_workflow_conditionals:
        if item[0] in {'x','m','a','s'} and item[1] in {'<', '>'}:
            variable = item[0]
            check = item[1]
            colon_index = item.find(':')
            threshold = int(item[2:colon_index])  # convert to integer
            next = item[colon_index+1 :]
            dict_list.append([variable, check, threshold, next])
        else:
            dict_list.append(['*', this_workflow_conditionals[-1]])
    dissected_workflows_dict[this_workflow_name] = dict_list
    return dissected_workflows_dict


def main() -> int:
    total_sum_of_ratings = 0
    workflows = []       # a list of each workflow string read from the input file
    part_ratings = []    # a list of N 4-element lists converted to integers : [N][x, m, a, s]
    accepted_parts = []  # holds the indices of accepted parts in part_ratings[] list
    with open("input_day_19.txt") as input_file:
        reading_workflows = True
        for line in input_file:
           line = line.rstrip()   # remove newline chars
           if reading_workflows:
               if line == '':
                   reading_workflows = False
                   continue
               workflows.append(line)
           else:
               part_ratings.append(process_rating(line))

    # process the input workflow information and prepare it for use
    workflow_dict = {}
    for workflow in workflows:
        workflow_dict.update(process_workflow(workflow))

    # start the workflow iterative process
    for part_index in range(len(part_ratings)):
        ratings = part_ratings[part_index]
        current_workflow = 'in'
        done_flag = False
        while not done_flag:
            if current_workflow == 'R':
                done_flag = True
                continue
            if current_workflow == 'A':
                accepted_parts.append(part_index)
                done_flag = True
                continue
            else:
                for item in workflow_dict[current_workflow]:
                    if item[0] == '*':
                        current_workflow = item[1]
                        break
                    if item[0] == 'x' and item[1] == '<':
                        if part_ratings[part_index][0] < item[2]:
                            current_workflow = item[3]
                            break
                    if item[0] == 'x' and item[1] == '>':
                        if part_ratings[part_index][0] > item[2]:
                            current_workflow = item[3]
                            break
                    if item[0] == 'm' and item[1] == '<':
                        if part_ratings[part_index][1] < item[2]:
                            current_workflow = item[3]
                            break
                    if item[0] == 'm' and item[1] == '>':
                        if part_ratings[part_index][1] > item[2]:
                            current_workflow = item[3]
                            break
                    if item[0] == 'a' and item[1] == '<':
                        if part_ratings[part_index][2] < item[2]:
                            current_workflow = item[3]
                            break
                    if item[0] == 'a' and item[1] == '>':
                        if part_ratings[part_index][2] > item[2]:
                            current_workflow = item[3]
                            break
                    if item[0] == 's' and item[1] == '<':
                        if part_ratings[part_index][3] < item[2]:
                            current_workflow = item[3]
                            break
                    if item[0] == 's' and item[1] == '>':
                        if part_ratings[part_index][3] > item[2]:
                            current_workflow = item[3]
                            break
    # that was ugly

    for part in accepted_parts:
        total_sum_of_ratings += sum(part_ratings[part])
    return total_sum_of_ratings


if __name__ == "__main__":
    print(f"The sum of all of the ratings for accepted parts is : {main()}")
