# Lab 5: Recursion — Koch Snowflake

**Course:** ENGR 221 – Python Programming  
**Student:** Cristofer Rojas  
**Date:** November 1, 2026

## Project Description

This lab explores recursion and stack-based programming by generating a Koch snowflake
using Python's Turtle graphics library. The program implements both recursive and
non-recursive methods to draw the same fractal pattern and compares their execution time
and memory consumption.

## Files Included

**snowflake.py**
- Contains the `KochSnowflake` class responsible for generating the snowflake.
- Implements `draw_curve_recursive_helper()` to draw curves using recursion.
- Implements `draw_curve_stack()` to draw curves using a stack and a while loop.
- Uses the Turtle graphics library to visualize the snowflake.
- Includes `compare_snowflake()` and `get_time_and_mem()` to measure execution time and
memory usage.

**answers.txt**
- Contains written responses to the questions in Parts 1 and 4.
- Explains how the drawing methods work and compares their performance.

## How to Run the Program

1. Open the Lab 5 folder in Visual Studio Code.
2. Open the terminal and navigate to the directory containing `snowflake.py`.
3. Install the required memory profiling library if it is not already installed:

   `py -m pip install memory_profiler`

4. Run the program using:

   `py snowflake.py`

5. A Turtle graphics window will open and draw the Koch snowflake.

## Program Configuration

The snowflake's size and complexity can be modified by changing the parameters of the
`KochSnowflake` object.

Example:

` s = KochSnowflake(500, 3) `

- `500` represents the initial side length.
- `3` represents the recursion depth, which determines the complexity of the snowflake.

To run the recursive method:

` s.draw_snowflake_recursive() `

To run the non-recursive method:

` s.draw_snowflake_stack() `

To compare both methods:

` s.compare_snowflake() `

## Results and Analysis

Both implementations successfully generated the same Koch snowflake pattern.

| Measurement | Recursive | Non-Recursive |
|---|---|---|
| Memory Usage | 41.0859375 MB | 29.9921875 MB |
| Execution Time | 19.08452 s | 18.88661 s |

The non-recursive method used less memory and completed slightly faster in this test. The
recursive method relies on repeated function calls, while the non-recursive method manages
drawing instructions using an explicit stack.

## Conclusion

This lab demonstrated how recursion and stacks can solve the same programming problem using 
different approaches. Both methods produced identical snowflake patterns, while the 
performance comparison highlighted differences in their memory usage and execution time.