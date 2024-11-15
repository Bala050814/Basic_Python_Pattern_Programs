#program to print the Pattern in Python
"""
*
* *
* * *
* * * *
* * * * *
"""

for row in range(5):
    for col in range(row+1):
        print("*",end=" ")
    print()