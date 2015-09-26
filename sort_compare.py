#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK4 Assignment Part II - Using search and sort algorithms."""

import time
import random



def insertion_sort(a_list):
    """Insertion list sort function."""
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end = time.time()
    return end-start, a_list


def gap_insertion_sort(a_list, start, gap):
    """Gap inserstion sort function."""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def shell_sort(a_list):
    """Shell list sort function."""
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    return end-start, a_list


def python_sort(a_list):
    """Builtin list sort function."""
    start = time.time()
    a_list = a_list.sort()
    end = time.time()
    return end-start, a_list


def random_list(length):
    """A random list generator."""
    randlist = []
    for item in range(length):
        randlist.append(random.randint(1,length))
    return randlist


def main():
    """The main function that runs tests upon calling the program."""
    test_numbers = [500,1000,10000]
    for items in test_numbers:
        counter = 100
        result = [0,0,0]
        while counter > 0:
            randlist = random_list(items)
            result[0] += insertion_sort(randlist)[0]
            result[1] += shell_sort(randlist)[0]
            result[2] += python_sort(randlist)[0]
            counter -= 1
        print "For the list of {}... ".format(items)
        print "Insertion Sort took %10.7f seconds to run, on average" % (result[0] / 100)
        print "Shell Sort " + "took %10.7f seconds to run, on average" % (result[1] / 100)
        print "Python Sort " + "took %10.7f seconds to run, on average" % (result[2] / 100)

if __name__ == "__main__":
    main()
