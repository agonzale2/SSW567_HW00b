"""Program to classify triangles and determine if they are right triangles."""

from math import isclose


def classify_triangle(a, b, c):
    """Classify a triangle based on its side lengths."""

    if a == b and b == c:
        triangle_type = "equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"

    if isclose(pow(a, 2) + pow(b, 2), pow(c, 2)):
        return f"the triangle is: {triangle_type} and is a right triangle."

    return f"the triangle is: {triangle_type} and is not a right triangle."
