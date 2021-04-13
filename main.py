import pandas as pd
import argparse
import numpy as np
from table_help import CoursesNeed, parse_timetable


def parse_arguments():
    """
    Get arguments from shell

    :output:
        arguments
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('--timetable_path', help='Path to table with timetable', required=True)

    return parser.parse_args()


def get_decart_mult(lhs_arr, rhs_arr, vertex):
    if vertex == None:
        return [lhs + rhs for lhs in lhs_arr for rhs in rhs_arr]
    else:
        return [lhs + rhs + [vertex] for lhs in lhs_arr for rhs in rhs_arr]

def dfs(vertex, table):
    """
    DFS to find all sets of courses
    :input:
        vertex - num of course
        table - timetable
    :output:
        [ courses ]
    """
    courses_to_take = table['dependencies'][vertex]

    total_courses = [[]]
    best_set = [[]]
    
    for course in courses_to_take:
        if course.is_one():
            get = dfs(course.get_elem(), table)
            total_courses = get_decart_mult(total_courses, get, None)
        else:
            for choose in course:
                curr_set = dfs(choose, table)
                best_set += curr_set
    
    if len(total_courses) > 1:
        total_courses.pop(0)
    
    if len(best_set) > 1:
        best_set.pop(0)
    
    total_courses = get_decart_mult(total_courses, best_set, vertex)
    
    if len(total_courses) == 0:
        total_courses = [[vertex]]


    return total_courses
            
            



def main():
    """
    Main function 
    """
    shell_args = parse_arguments()

    table = parse_timetable(shell_args.timetable_path)

    print()
    print('Choose courses to take (indexes):')

    courses_need = list(map(int, input().split()))

    print()
    print('Choose priority courses (indexes):')

    priority_courses = list(map(int, input().split()))

    print()
    print('Print minimal count of courses per term:')

    min_courses_per_term = int(input())

    print()
    print('Bachelor or undergraduate (print 0 or 1):')

    bachelor = bool(int(input()))

    courses_to_take_unsort = [[]]

    for course in courses_need:
        sets = dfs(course, table)

        answers = []
        for course_set in sets:
            course_set = list(np.unique(course_set))
            answers.append(course_set)
        
        courses_to_take_unsort = get_decart_mult(courses_to_take_unsort, answers, None)
    
    courses_to_take = []

    for course_set in courses_to_take_unsort:
        course_set = list(np.unique(course_set))
        courses_to_take.append(course_set)
    

    courses_to_take = sorted(courses_to_take, key=lambda x: (len(x), len(x) > min_courses_per_term * (3 if bachelor else 5)))

    if len(courses_to_take[0]) < min_courses_per_term * (3 if bachelor else 5):
        print("You can't choose plan :(")
    else:
        print('That is courses you need to take:')
        print(courses_to_take[0])


if __name__ == '__main__':
    main()