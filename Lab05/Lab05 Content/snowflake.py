'''Cristofer Rojas
11/01/2026
This program generates a Koch snowflake using both recursive and non-recursive
(stack-based) methods. It also compares the execution time and memory usage
of both approaches to evaluate their performance. '''


import turtle
import time 
from memory_profiler import memory_usage

class KochSnowflake:
    def __init__(self, init_length=500, init_depth=3):
        # Initialize the turtle
        self.t = None  

        # Length of one edge at 0 depth
        self.init_length = init_length  
        # Number of "layers" to draw
        self.init_depth = init_depth    
    

    
    def init_turtle(self):
        """Initialize the turtle for drawing the snowflake."""

        # Create or access the Turtle graphics screen
        screen = turtle.Screen()

        # Reset the screen before creating a new turtle
        screen.reset()

        # Create a new turtle object
        t = turtle.Turtle()

        # Set the turtle drawing speed
        t.speed(8)

        # Move the turtle to its starting position
        t.teleport(-200, -200)

        # Store the turtle object for other methods
        self.t = t



    ######################
    # Draw curve methods #
    ######################

    def draw_curve_recursive(self):
        """ The 'entry point' into the recursive curve method """
        self.draw_curve_recursive_helper(self.init_length, self.init_depth)


    
    def draw_curve_recursive_helper(self, length, depth):
        # This method draws one side of the Koch snowflake using recursion.

        # Check whether the recursion depth is negative.
        if depth < 0:
            # Stop the program if an invalid depth is provided.
            raise ValueError("Depth cannot be negative")

        # Base case: Stop recursion when depth reaches zero.
        elif depth == 0:
            # Move the turtle forward by the specified length,
            # drawing a straight line.
            self.t.forward(length)

        # Recursive case: Divide the line into smaller segments.
        else:
            # Divide the current line length into three equal parts.
            new_length = length / 3

            # FIRST SEGMENT

            # Recursively draw the first smaller segment.
            # Reduce depth by 1 to move toward the base case.
            self.draw_curve_recursive_helper(new_length, depth - 1)

            # SECOND SEGMENT

            # Rotate the turtle 60 degreesclockwise.
            self.t.right(60)

            # Recursively draw the second smaller segment.
            self.draw_curve_recursive_helper(new_length, depth - 1)

            # THIRD SEGMENT

            # Rotate the turtle 120 degrees counterclockwise.
            self.t.left(120)

            # Recursively draw the third smaller segment.
            self.draw_curve_recursive_helper(new_length, depth - 1)

            # FOURTH SEGMENT

            # Rotate the turtle 60 degrees clockwise.
            # This returns the turtle to its original heading.
            self.t.right(60)

            # Recursively draw the fourth smaller segment.
            self.draw_curve_recursive_helper(new_length, depth - 1)


    
    def draw_curve_stack(self):
        """
        Draws one side of the Koch snowflake using a stack
        instead of recursive function calls.
        """

        # Create a stack containing the initial drawing command.
        # The command includes its type, line length, and depth.
        commands = [("add_curve", self.init_length, self.init_depth)]

        # Continue executing commands until the stack is empty.
        while commands:

            # Remove the last command added to the stack (LIFO).
            command = commands.pop()

            # Check whether the command is to draw a curve.
            if command[0] == "add_curve":

                # Retrieve the length stored in the command.
                length = command[1]

                # Retrieve the recursion depth stored in the command.
                depth = command[2]

                # Prevent negative depth values.
                if depth < 0:
                    raise ValueError("Depth cannot be negative")

                # Base case: Draw a straight line when depth is zero.
                elif depth == 0:

                    # Move the turtle forward by the specified length.
                    self.t.forward(length)

                # If depth is greater than zero, divide the curve.
                else:

                    # Each smaller segment is one-third the current length.
                    new_length = length / 3

                    # Decrease the depth for the smaller segments.
                    new_depth = depth - 1

                    # Add commands in REVERSE execution order.
                    # The last command pushed will execute first.

                                    
                    # Fourth segment: Added first, executed last
                    commands.append(("add_curve", new_length, new_depth))

                    # Turn right 60 degrees before the fourth segment
                    commands.append(("turn_right", 60))

                    # Third segment
                    commands.append(("add_curve", new_length, new_depth))

                    # Turn left 120 degrees before the third segment
                    commands.append(("turn_left", 120))

                    # Second segment
                    commands.append(("add_curve", new_length, new_depth))

                    # Turn right 60 degrees before the second segment
                    commands.append(("turn_right", 60))

                    # First segment: Added last, executed first
                    commands.append(("add_curve", new_length, new_depth))


            # Check whether the command requires a left turn.
            elif command[0] == "turn_left":

                # Rotate the turtle counterclockwise by the stored angle.
                self.t.left(command[1])

            # Check whether the command requires a right turn.
            elif command[0] == "turn_right":

                # Rotate the turtle clockwise by the stored angle.
                self.t.right(command[1])



    ##########################
    # Draw snowflake methods #
    ##########################

    def draw_snowflake_recursive(self):
        """ Draw the three edges of the Koch snowflake using the 
            recursive curve method """

        self.init_turtle()

        for _ in range(3):
            self.draw_curve_recursive()
            self.t.left(120)
            
        turtle.clearscreen()


    def draw_snowflake_stack(self):
        """ Draw the three edges of the Koch snowflake using the 
            non-recursive curve method """

        self.init_turtle()

        for _ in range(3):
            self.draw_curve_stack()
            self.t.left(120)

        turtle.clearscreen()


    #########################@#
    # Compare the approaches! #
    ##########################@

    def compare_snowflake(self):
        """ Compare how much time and memory the recursive and non-recursive 
            implementations of drawing the Koch Snowflake used """
        
        rec_time, rec_mem = self.get_time_and_mem(self.draw_snowflake_recursive)
        nonrec_time, nonrec_mem = self.get_time_and_mem(self.draw_snowflake_stack)

        print(f"Recursive memory usage: {rec_mem} MB")
        print(f"Non-recursive memory usage: {nonrec_mem} MB")
        print()
        print(f"Recursive time taken: {rec_time:.5f} s")
        print(f"Non-recursive time taken: {nonrec_time:.5f} s")
        

    def get_time_and_mem(self, func):
        """ Find the time and memory used by the given function """

        # Start the timer
        time_start = time.perf_counter()
        # Run the function and find the memory used
        mem_usage = memory_usage((func, ), include_children=True, multiprocess=True)
        # End the timer
        time_end = time.perf_counter()

        # Find the total time taken
        time_taken = time_end - time_start 
        # Find the total memory used
        mem_used = max(mem_usage) - min(mem_usage)

        return time_taken, mem_used



if __name__ == "__main__":
    # Create a snowflake with side length 500 and depth 3
    s = KochSnowflake(500, 3)

    # Test the corrected recursive method
    s.draw_snowflake_recursive()


