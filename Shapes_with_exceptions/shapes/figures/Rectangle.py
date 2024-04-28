from shapes.Point import Point
from shapes.Shape import Shape


class Rectangle(Shape):

  def __init__(self, i_center: Point, i_width: float, i_height: float):
    """
    The function initializes a rectangle with a given center point, width, and height.

    :param i_center: It looks like you were about to provide information about the `i_center` parameter in the code snippet you shared. Could you please provide more details or let me know how I can assist you further with this code snippet?
    :type i_center: Point
    :param i_width: It looks like you were about to provide some information about the `i_width` parameter in your code snippet. How can I assist you further with this?
    :type i_width: float
    :param i_height: The `i_height` parameter in the `__init__` method represents the height of a rectangle that is being created. It is used to calculate the y-coordinates of the vertices of the rectangle based on the center point provided
    :type i_height: float
    """
    vertices = [
        Point(i_center.get_x() - i_width / 2,
              i_center.get_y() - i_height / 2),
        Point(i_center.get_x() + i_width / 2,
              i_center.get_y() - i_height / 2),
        Point(i_center.get_x() + i_width / 2,
              i_center.get_y() + i_height / 2),
        Point(i_center.get_x() - i_width / 2,
              i_center.get_y() + i_height / 2)
    ]
    super().__init__(vertices)

  def compute_area(self):
    """
    This Python function calculates the area of a rectangle using the lengths of its sides.
    :return: The `compute_area` method is returning the area of a rectangle, which is calculated by multiplying the lengths of two adjacent sides of the rectangle.
    """
    side1_length = self.get_edges()[0].length()
    side2_length = self.get_edges()[1].length()
    return side1_length * side2_length

  def compute_perimeter(self):
    """
    This Python function calculates the perimeter of a shape by summing the lengths of its edges.
    :return: The `compute_perimeter` method calculates the perimeter of a shape by iterating through its edges and summing up their lengths. The method returns the total perimeter of the shape.
    """
    perimeter = 0
    for line in self.get_edges():
      perimeter += line.length()
    return perimeter

  def compute_inner_angles(self):
    return [90, 90, 90, 90]
