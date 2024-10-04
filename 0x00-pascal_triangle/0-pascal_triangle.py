#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    
    # Initialize the first row of Pascal's Triangle
    triangle = [[1]]
    
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        
        # Calculate the values for the middle elements of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # End each row with 1
        row.append(1)
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle

