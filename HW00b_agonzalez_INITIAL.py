def classify_triangle(a, b, c):
    triangle_type = "none"
    if a == b and b == c:
        triangle_type = "equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"

    if triangle_type == "none":
        return "invalid arguments"

    if pow(a,2) + pow(b,2) == pow(c,2):
        return f"the triangle is: {triangle_type} and is a right triangle."
    else:
        return f"the triangle is: {triangle_type} and is not a right triangle."
