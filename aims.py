# Jessica Sarah Stow
# stowjess@gmail.com

# AIMS AI for Science Masters Application 2023
# Data Structures and Algorithms Coding Question

def count_paths(input_string):

    def remove_spaces(input_string): # define function to remove all spaces (" ") from input_string
        return input_string.replace(" ", "")
    input_string = remove_spaces(input_string) # remove spaces

    # split the input_string into rows using the 'split()' function
    # with the newline character '\n' separating each row
    grid = [list(row) for row in input_string.split('\n')]

    height = len(grid) # calculate the number of rows the grid contains
    width = len(grid[0]) # calculate the number of columns the grid contains

    nr_points = height*width # calculate the number of points in the grid
    nr_of_x = input_string.count('x') # calculate the number of x's (blocked cells) in the grid
    nr_to_be_visited = nr_points - nr_of_x # calculate the number of cells that should be visited when moving from point A to point B

    visited_counts = [] # create a list with the number of visited cells it takes to reach B from A for all possible paths
    # the above list contains the number of cells visited for all different paths, whether they visited only some, or all of the cells

    # using a depth-first search we can calculate how many cells were visited for each path taken, and compile these in a list ('visited_counts')
    def dfs(curr_i, curr_j, visited_count): # find all paths from the starting point to the end point
        # `curr_i` represents the current row
        # `curr_j` represents the current column
        # `visited_count` is the number of visited points so far
        if curr_i == height-1 and curr_j == width-1: # check whether the current point is the end point (B)
            visited_counts.append(visited_count) # append visited_count to visited_counts list
            return

        grid[curr_i][curr_j] = 'x' # mark the current point as visited by changing its value to 'x' in the grid

        if curr_i > 0 and grid[curr_i-1][curr_j] != 'x':
            dfs(curr_i-1, curr_j, visited_count+1)

        if curr_i < height-1 and grid[curr_i+1][curr_j] != 'x':
            dfs(curr_i+1, curr_j, visited_count+1)

        if curr_j > 0 and grid[curr_i][curr_j-1] != 'x':
            dfs(curr_i, curr_j-1, visited_count+1)

        if curr_j < width-1 and grid[curr_i][curr_j+1] != 'x':
            dfs(curr_i, curr_j+1, visited_count+1)

        grid[curr_i][curr_j] = '.' # after all paths from the current position are explored mark the cell as unvisited by changing value back to "."
        grid[0][0] = 'A' # and reset first value back to 'A' (This is not necessary for code to run correctly)

    dfs(0, 0, 1) # set the initial position to (0, 0) and the number of visited points as 1 (the starting point)

    # count the number of times that ALL the non-x cells were visited
    # this was done by counting the number of times the 'nr_to_be_visited' appears
    # in the 'visited_counts' list
    total = visited_counts.count(nr_to_be_visited)
    # 'total' returns the total number of paths that can be taken
    # to get from point A to point B,
    # while visiting all cells excluding cells marked with an 'x'
    return total

input_string = 'A x . .\n. . . .\n. . x B' # insert your string here
number_of_paths = count_paths(input_string)
print(number_of_paths)


# See also:
# My GitHub repository for this problem: https://github.com/jessicastow/AIMS_Masters_Application


# References
# https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/tutorial/
# https://leetcode.com/problems/unique-paths-ii/solutions/3225310/finding-unique-paths-in-a-grid-with-obstacles-a-dynamic-programming-approach/
# https://www.freecodecamp.org/news/learn-dynamic-programing-to-solve-coding-challenges/
# https://chat.openai.com/
