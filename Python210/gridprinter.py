#=========================================================================================
#Name: Grid Printer
#Author: Wesley Wang
#Date: 4/12/2018
#=========================================================================================

"""
Used by print_grid to draw horizontal line(floor)
:param: Number row/col, Size of grid
:return: Floor with specified row/col count and size
"""
def draw_floor(rowcol, size):
  for x in range(rowcol):
      print("+" + "-"*size, end='')
  print("+")

"""
:param: number row/col, size of grid
:return: Grid with specified row/col count and size
"""
def print_grid(rowcol, size):
  for y in range(rowcol):
    draw_floor(rowcol, size)
    for wall in range(size):
      print(("|"+" "*size)*rowcol + "|")
  draw_floor(rowcol, size) #Print bottom line


print_grid(5,4) #Print grid with 5 rows, 5 cols, and size of 4