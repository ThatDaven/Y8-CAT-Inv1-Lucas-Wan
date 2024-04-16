# Y8-CAT-Inv1-Lucas-Wan


Part 1.1: Create and explain a reusable means of achieving translations (10 Marks)
To achieve translations on the Cartesian plane according to the specified directions and distances, we can create a reusable function that utilizes a lookup table approach.

1. Lookup Table Creation: A lookup table that maps each direction (1 to 8) to the corresponding Pythagorean triple (a, b, c). This table will help us quickly determine the appropriate translation for each direction.
2. Translation Function: A function that takes the desired distance and direction as inputs. Using the lookup table, it will identify the corresponding Pythagorean triple and calculate the translation vector accordingly.
3. Error Handling: Error handling to ensure that the input direction is within the valid range (1 to 8) and that the distance is non-negative.
4. Documentation: We'll thoroughly document the function's purpose, inputs, outputs, and usage to ensure clarity and ease of understanding.


Part 1.2:  Use functions, validate input and document imports (10 Marks)
1. Function Usage: Ensure that all operations, calculations, and functionalities are encapsulated within functions. This promotes modularity, readability, and reusability of code.
2. Input Validation: Validate input data to ensure it meets the specified criteria. For example, we'll reject negative lengths and directions beyond the range of 1 to 8.
3. Custom Implementation: Instead of relying on built-in libraries like math, have own versions of functions to perform required operations. For instance, if distance calculation is needed, we'll implement our own function instead of using math.dist().

# Example usage of input validation and distance calculation
point1 = (2, -4)
point2 = (-5, 3)
if validate_distance(calculate_distance(point1, point2)):
    print("Distance:", calculate_distance(point1, point2))
else:
    print("Invalid distance.")

# Example of validating direction
direction = 10
if validate_direction(direction):
    print("Valid direction.")
else:
    print("Invalid direction.")