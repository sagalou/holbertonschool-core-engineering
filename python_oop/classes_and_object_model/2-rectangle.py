def area(self):
    """Returns the area of the rectangle"""
    return self.__width * self.__height


def perimeter(self):
    """Returns the perimeter of the rectangle"""
    if self.__width == 0 or self.__height == 0:
        return 0
    return 2 * (self.__width + self.__height)
