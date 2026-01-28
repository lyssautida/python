print("Default module import")
# import math
from math import sqrt

# square_root = math.sqrt(25)
square_root = sqrt(25)
print(f"Result square root 25 is {square_root}")

from my_module import greeting, double

message = greeting("Keeki")
result = double(5)
print(message)
print(f"Double 5 is {result}") 