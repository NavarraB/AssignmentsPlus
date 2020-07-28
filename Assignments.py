#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment - 10 (Sudoku Displayer)
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

