# Author: Suchi Rodda
# Date Written: 02/10/2022
# Last Modified: 
#   03/01/2023 (fixed the integer or float index issue)
#   09/05/2023 (changed name from pretty_print_iterable to suchi_print)
#   09/05/2023 (for lists, displaying the datatype)
#   09/07/2023 (Consolidated code for tuples and lists, displaying datatypes for all)
# Accepts: Any iterable - list, tuple, dictionary, set
# Returns: Nothing
# This function prints any dictionary or list or tuple in a nice way to visualize the data


def suchi_print(data, index=0, indent=0):
  if is_an_iterable(data):
    print(item_type(data), "\n")
    if type(data) in [list, tuple]:
      pretty_print_list(data, index, indent)
    elif type(data) is dict:
      pretty_print_dict(data, index, indent)
  else:
    print(item_type(data), data)


# Handling Lists

def pretty_print_list(iter, index = 0, indent = 0):
  for index, item in enumerate(iter):
    if is_an_iterable(item):
      parse_list(item, index, indent)
    else:
      print(spaces(indent), index, ' -> ', item_type(item), item, sep = '')

def parse_list(item, index, indent):
  if type(item) in [list, tuple]:
    print(spaces(indent), index, ' -> ', item_type(item), sep = '')
    indent += 1
    for index, each_item in enumerate(item):
      parse_list(each_item, index, indent)
  elif type(item) is dict:
    print(spaces(indent), index, ' -> ', item_type(item), sep = '')
    indent += 1
    pretty_print_dict(item, index, indent)
  else:
    print(spaces(indent), index, ' -> ', item_type(item), item, sep = '')


# Handling Dictionaries

def pretty_print_dict(iter, index = 0, indent = 0):
  if is_an_iterable(iter):
    if type(iter) is dict:
      for idx in iter:
        if is_an_iterable(iter[idx]):
          parse_dict(iter[idx], idx, indent)
        else:
          print(spaces(indent), idx, ' -> ', item_type(iter[idx]), iter[idx], sep='')
  else:
    print(iter)


def parse_dict(item, index, indent):
  if type(item) is dict:
    print(spaces(indent), index, ' -> ', item_type(item), sep = '')
    indent += 1
    for index in item:
      parse_dict(item[index], index, indent)
  elif type(item) is list or type(item) is tuple:
    print(spaces(indent), index, ' -> ', item_type(item), sep = '')
    indent += 1
    pretty_print_list(item, index, indent)
  else:
    print(spaces(indent), index, ' -> ', item_type(item), item, sep = '')


# Supporting Functions

def is_an_iterable(my_iterable):
  return type(my_iterable) in [list, tuple, dict, set]

def spaces(indent):
  return "\t"*indent

def item_type(item):
  return "("+(str(type(item)).replace('<class','').replace('>','').replace("'",'')).strip()+") "

def main():
  print('''

  ------------------------------------------------------
  This is a print module written by Suchi Rodda

  To use this module you must 
  - call the function suchi_print() and 
  - pass ONE variable of any datatype as argument

  suchi_print() prints any sequence in a pretty format
  If it is not a sequence, it will print its datatype
  --------------------------------------------------------
  ''')

if __name__ == "__main__":
  main()