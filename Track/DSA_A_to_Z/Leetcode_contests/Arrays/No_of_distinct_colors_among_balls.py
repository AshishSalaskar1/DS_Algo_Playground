"""
PROBLEM:
Link: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

- There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.
- Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.
- Note that when answering a query, lack of a color will not be considered as a color.

"""

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> List[int]:
        ball_to_color = {}  # Maps each ball to its current color
        color_frequency = {}  # Tracks how many balls are of each color
        unique_colors = set()  # Set to store the unique colors in use
        results = []  # List to store the number of unique colors after each query

        for ball, color in queries:
            if ball in ball_to_color:
                previous_color = ball_to_color[ball]
                # Decrement the count of the previous color
                color_frequency[previous_color] -= 1
                if color_frequency[previous_color] == 0:
                    unique_colors.remove(previous_color)
            
            # Update the ball's color
            ball_to_color[ball] = color
            if color not in color_frequency:
                color_frequency[color] = 0
            color_frequency[color] += 1
            unique_colors.add(color)
            
            results.append(len(unique_colors))

        return results