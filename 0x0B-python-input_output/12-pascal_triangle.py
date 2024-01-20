#!/usr/bin/python3
"""Define a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents the Pascal's Triangle of size n.

    Returns the list of lists of integers that represent the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trian = triangles[-1]
        tempo = [1]
        for i in range(len(trian) - 1):
            tempo.append(trian[i] + trian[i + 1])
        tempo.append(1)
        triangles.append(tempo)
    return triangles
