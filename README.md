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

### Bonus question solution:

⌛ **Time complexity:** the algorithm iterates over each cell in `grid` once and for each cell it performs a constant number of operations. So, the time complexity of this algorithm is *O(rc)*.

🪐 **Space complexity:** the algorithm uses a matrix of size `r` x `c`, which requires *O(rc)* space.

👍 **General rules of thumb:**

The time it takes to calculate the number of possible paths from A to B increases as: 
1. the size of the grid increases.
2. the number of obstacles ('x') in the grid increases.
