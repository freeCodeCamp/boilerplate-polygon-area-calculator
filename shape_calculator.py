class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
    def set_width(self, width:float) -> None:
        self.width = width
    def set_height(self, height:float) -> None:
        self.height = height
    def get_area(self) ->int:
        return self.width * self.height
    def get_perimeter(self) -> int:
        return 2*self.width + 2*self.height
    def get_diagonal(self) ->float:
        return (self.width ** 2 + self.height**2) ** .5

    def get_picture(self) ->str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        ret_str = ""
        for i in range(self.height):
            for j in range(self.width):
                ret_str += "*"
            ret_str += "\n"
        return ret_str
    def get_amount_inside(self, other_rectangle) -> int:
        return self.get_area() // other_rectangle.get_area()
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'



class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def __str__(self):
        return f'Square(side={self.width})'
    def set_height(self, height: float) -> None:
        super().set_height(height)
        super().set_width(height)
    def set_width(self, width: float) -> None:
        super().set_height(width)
        super().set_width(width)
    def set_side(self, length):
        self.set_width(length) 

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
