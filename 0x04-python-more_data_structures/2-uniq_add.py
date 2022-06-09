#!/usr/bin/python3
def uniq_add(my_list=[]):
   """adds all unique integers in a list"""
    conv_set = set(my_list)
    return sum(list(conv_set))
