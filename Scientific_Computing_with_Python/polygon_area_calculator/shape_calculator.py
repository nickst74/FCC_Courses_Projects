class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def set_width(self, width) -> None:
        self.width = width

    def set_height(self, height) -> None:
        self.height = height
    
    def get_area(self) -> int:
        return self.width * self.height
    
    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height
    
    def get_amount_inside(self, shape):
        vert = self.height // shape.height
        hor = self.width // shape.width
        return vert * hor
    
    def __str__(self) -> str:
        return "Rectangle(width={}, height={})".format(self.width, self.height)
        



class Square(Rectangle):
    def __init__(self, length) -> None:
        super().__init__(length, length)
    
    def set_side(self, length) -> None:
        super().set_width(length)
        super().set_height(length)
    
    def set_width(self, width) -> None:
        self.set_side(width)
    
    def set_height(self, height) -> None:
        self.set_side(height)
    
    def __str__(self) -> str:
        return "Square(side={})".format(self.width)
