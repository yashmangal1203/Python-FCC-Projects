class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return round(self.width*self.height)

    def get_perimeter(self):
        return ((2*self.width)+(2*self.height))

    def get_diagonal(self):
        return (((self.width ** 2 + self.height ** 2) ** .5))

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                picture += '*'*self.width+'\n'
            return picture

    def get_amount_inside(self, shape):
        noOfShapes = self.get_area()/shape.get_area()
        return int(noOfShapes)


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
