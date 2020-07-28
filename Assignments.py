#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment - 10 (Sudoku Displayer)
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
for ii in range(9):
    if ii in (0, 3, 6):
        print(15 * '- ')
    for i in range(9):
        if i in(2, 5, 8):
            print(sudoku[ii][i], '| ', end = '')
        else:
            print(sudoku[ii][i], ' ', end = '')
    print()
print(15 * '- ')

