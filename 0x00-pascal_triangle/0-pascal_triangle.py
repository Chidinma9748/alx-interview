#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return[]

    """Initializing the first row of the Pascals triangle"""
    triangle - [[1]]

     for i in range(1, n):
         """each row starts with 1"""
         row = [1]

         """calculate the middle numbers"""
         for j in range(1, i):
             row.append(triangle[i-1][j-1] + triangle[i-1][j])

             """end each row with 1"""
         row.append(1)

         """add row to the triangle"""
         triangle.append(row)

     return triangle
