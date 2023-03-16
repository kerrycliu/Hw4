'''Create a file named bug1.py and copy the code below.
• When you submit only update the code such that you get the correct output below.
• You should not see any errors or warnings if you completly corrected the code.
Hint: - I suggest reading this article https://realpython.com/python3-object-oriented-programming/'''

# TODO: there's code missing in one or more lines below


class Base:

    def __init__(self, x, y, size):
        # TODO: will need to fill this in
        x

    def draw(self):

        return ""


class Circle():
    def __init__(x, y, size):

        super().__init__(x, y, size)

    def draw(self):

        return f"""
({self.x}, {self.y})
{self.size}
, - ~ ~ ~ - ,
, ' ' ,
, ,
, ,
, ,
, ,
, ,
, ,
, ,
, , '
' - , _ _ _ , '
"""


class Square(Base):
    def __init__(self, y, size):
        super().__init__(x, y, size)

    def draw():
        return f"""

({self.x}, {self.y})
{self.size}
--------------------
| |
| |
| |
| |
| |
| |
| |
| |
--------------------
"""
# All of the code below is correct


def draw_any_shape(myShape):
    print(myShape.draw())


def main():

    s = Square(1, 2, 3)
    draw_any_shape(s)
    c = Circle(2, 2, 1)
    draw_any_shape(c)


main()