# AIMS Masters Application 2023
## Data Structures and Algorithms Coding question as part of the AIMS AI for Science Masters Application 2023

This repository contains my solution to the AIMS' AI for Science Masters application coding question for 2023.

### Instructions

A robot starts on a point marked “A” on a rectangular grid of points. The starting point is always the top left point on the grid. The robot can move left, right, up or down, moving from one point to the next. By moving in steps going left, right, up or down, the robot would like to reach a point marked “B”, which is always the bottom right point in the grid.

Sometimes, points are marked as “x”, and the robot is not allowed to visit them at all. A robot is never allowed to visit a point more than once.

In how many ways can the robot move from A to B and visit all points along the way?

For example, in the following grid, represented in text as:
```
A . .
. . B
```
there is only one path from A to B:

![image](https://user-images.githubusercontent.com/56385852/229277441-a8eabe94-31fd-4d67-8e66-595bab987a09.png)

In the following grid, represented in text as:
```
A . .
x x B
```
there is still only one path (we're lucky because of the two x's):

![image](https://user-images.githubusercontent.com/56385852/229277460-c5762d4c-8cda-4836-99a1-193b8746f256.png)

However, in the grid:
```
A . .
. x B
```
there are no ways for the robot to move from A to B and visit all points that are not marked with “x”.

### Task 
Write a single file of Python code that can be used to count the number of paths from A to B for any given input grid. Inside this file, your code should call a function that has the following boilerplate format:
```
def count_paths(input_string):
  # parse the string input here, possibly calling other functions that you’ve
  # written in your Python code file

  # possibly call other functions that you’ve written in your Python code
  # file to count the number of paths

  # return the (integer) number of paths
  return number_of_paths
```

If your code was called with:
```
input_string = 'A . . .\n. . . B'
number_of_paths = count_paths(input_string)
print(number_of_paths)
```
the number 0 should be printed. 

If your code was called with:
```
input_string = 'A . . .\n. . . .\n. . . .\n. . x B'
number_of_paths = count_paths(input_string)
print(number_of_paths)
```
a number larger than one should be printed. We’ll leave it to you to determine what it is.

Your code doesn’t have to run on grids larger than 10x10 points, and should only make use of the Python Standard Library.

### Bonus question
Can you say anything about the complexity of the problem?

How much longer do you guess it will take to obtain an answer for a 100x100 grid compared to a 10x10 grid? And a 1x10 grid compared to a 10x10 grid? Can you postulate some general rules of thumb?

# My solution

### My coding solution:

Below is an explanation behind the functions are variables I used in my`.py` script. 

- `input_string`: the string representing the grid. Can be changed by the user. 
- `count_paths`: this is a user-defined function takes an `input_string` argument, which is a string representing the grid.
- `remove_spaces`: this function removes spaces from the `input_string`.
- `grid`: is used to store the list of lists (rows). This variable is created by splitting the input string by newline characters (`\n`) and then converting each row into a list of characters.
- `height`: this variable is set to the number of rows in the given grid.
- `width`: this variable is set to the number of columns in the given grid. 
- `nr_points`: calculated by multiplying the `height` with the `width` to determine the total number of points the grid consists of.
- `nr_of_x`: stores the number of times 'x' appears in the `input_string`.
- `nr_to_be_visited`: stores the number of cells the robot needs to visit on its journey from point A to point B. Calculated by subtracting `nr_of_x` from `nr_points`. 
- `dfs`: this function takes three arguments: 
  - `curr_i`: the current row,
  - `curr_j`: the current column, and
  - `visited_count`: the number of visited points so far. 
- `visited_counts`: this list is used to store the count of visited points for each valid path.

**More on the depth-first search approach:**
The base case of the recursion is when the current position is the bottom-right corner of the grid (`curr_i == height-1` and `curr_j == width-1`), i.e. it is at point B. In this case, the `visited_count` is appended to the `visited_counts` list and the function returns.

Before visiting a new cell, we mark it as visited by changing its value to 'x'. Then, we explore all possible directions from the current position by checking if the adjacent cells are not marked as 'x'. If so, we recursively call the `dfs` function on the adjacent cell with the updated `visited_count`. After all possible paths from the current position are explored, we mark the cell as unvisited by changing its value back to '.'.

This depth-first search algorithm explores all possible paths from the top-left corner (point A) to the bottom-right corner (point B) of the grid, and counts the number of visited points for each valid path.

### Bonus question solution:

⌛ **Time complexity:** the algorithm iterates over each cell in `grid` once and for each cell it performs a constant number of operations. So, the time complexity of this algorithm is *O(rc)*.

🪐 **Space complexity:** the algorithm uses a matrix of size `r` x `c`, which requires *O(rc)* space.

👍 **General rules of thumb:**

The time it takes to calculate the number of possible paths from A to B increases as: 
1. the size of the grid increases.
2. the number of obstacles ('x') in the grid increases.

### References

1. Anmol Agrawal, FreeCodeCamp (n.d.). Learn Dynamic Programming to Solve Coding Challenges. Available at: https://www.freecodecamp.org/news/learn-dynamic-programing-to-solve-coding-challenges/ [Accessed on 23 March 2023].
2. HackerEarth. (n.d.). Dynamic Programming - 2D Array. Available at: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/tutorial/ [Accessed 24 March 2023].
3. LeetCode (n.d.). Finding Unique Paths in a Grid With Obstacles - A Dynamic Programming Approach. Available at: https://leetcode.com/problems/unique-paths-ii/solutions/3225310/finding-unique-paths-in-a-grid-with-obstacles-a-dynamic-programming-approach/ [Accessed 24 March 2023]
4. OpenAI. (2023). ChatGPT (GPT-3.5). Retrieved March 31, 2023, from [https://chat.openai.com/].
