import pytest

from math import sqrt

from HW00b_agonzalez import classify_triangle


def test_triangle_scalene_right():
    assert classify_triangle(3, 4, 5) == "the triangle is: scalene and is a right triangle."

def test_triangle_equilateral():
    assert classify_triangle(3, 3, 3) == "the triangle is: equilateral and is not a right triangle."

def test_triangle_isosceles():
    assert classify_triangle(3, 3, 4) == "the triangle is: isosceles and is not a right triangle."

def test_triangle_isosceles_right():
    assert classify_triangle(5, 5, 5*sqrt(2)) == "the triangle is: isosceles and is a right triangle."

def test_triangle_scalene():
    assert classify_triangle(5, 4, 3) == "the triangle is: scalene and is not a right triangle."

def test_triangle_bad_arguments():
    with pytest.raises(TypeError): classify_triangle("x", "y", "z")
