from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3
    yellow = 4
    pink = 5

print(Color.red)
print(Color(4))
print(Color['blue'])

[c for c in Color]
