#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK4 Assignment Part I - Using search and sort algorithms."""

import time
import random



def sequential_search(a_list, item):
    """A sequential list search."""
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    return end-start, found


def ordered_sequential_search(a_list, item):
    """A sequential sorted list search."""
    a_list.sort()
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    return end-start, found


def binary_search_iterative(a_list, item):
    """An iterative binary list search."""
    a_list.sort()
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return end-start, found


def binary_search_recursive(a_list, item):
    """A recursive binary list search."""
    a_list.sort()
    start = time.time()
    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)
    end = time.time()
    return end-start, found


def random_list(length):
    """A random list generator."""
    randlist = []
    for item in range(length):
        randlist.append(random.randint(1,length))
    return randlist


def main():
    """The main function that runs tests upon calling the program."""
    test_numbers = [500,1000,10000]
    for test in test_numbers:
        counter = 100
        result = [0,0,0,0]
        while counter > 0:
            randlist = random_list(test)
            result[0] += sequential_search(randlist, -1)[0]
            result[1] += ordered_sequential_search(randlist, -1)[0]
            result[2] += binary_search_iterative(randlist, -1)[0]
            result[3] += binary_search_recursive(randlist, -1)[0]
            counter -= 1
        print "For the list of {}... ".format(test)
        print "Sequential Search took %10.7f seconds to run, on average" % (result[0] / 100)
        print "Ordered Sequential Search " + "took %10.7f seconds to run, on average" % (result[1] / 100)
        print "Iterative Binary Search " + "took %10.7f seconds to run, on average" % (result[2] / 100)
        print "Recursive Binary Search " + "took %10.7f seconds to run, on average" % (result[3] / 100)


if __name__ == "__main__":
    main()
