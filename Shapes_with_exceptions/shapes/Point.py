class Point:
  definition: str = "Abstract geometric entity representing a location in space."

  def __init__(self, x: float = 0, y: float = 0):
    self.__x = x
    self.__y = y

  def __eq__(self, other_point):
    return self.__x == other_point.__x and self.__y == other_point.__y

  def __repr__(self):
    return f"({self.__x}, {self.__y})"

  def compute_distance(self, point) -> float:
    """
    The function `compute_distance` calculates the distance between two points in a two-dimensional space.

    :param point: The `compute_distance` method calculates the Euclidean distance between the current point (self) and another point passed as an argument. The `point` parameter represents the other point for which you want to calculate the distance from the current point
    :return: The `compute_distance` method calculates the Euclidean distance between the current point (self) and another point passed as an argument. The distance is rounded to two decimal places and returned as a float value.
    """
    return round(
        ((self.__x - point.__x)**2 + (self.__y - point.__y)**2)**(0.5), 2)

  def magnitude(self):
    """
    This function calculates the magnitude of a vector with coordinates x and y.
    :return: The `magnitude` method calculates the magnitude (or length) of a vector using the formula sqrt(x^2 + y^2) and returns the result rounded to 2 decimal places.
    """
    return round((self.__x**2 + self.__y**2)**(0.5), 2)

  def dot_product(self, point):
    """
    The `dot_product` function calculates the dot product of two points.

    :param point: The `dot_product` method you provided calculates the dot product between two points. The parameters `self` and `point` are both points in a 2D space. The method calculates the dot product by multiplying the x-coordinates of the two points and adding the product of the y-coordinates
    :return: The dot product of the current point object and the input point object is being returned.
    """
    return self.__x * point.__x + self.__y * point.__y

  def sum(self, i_point):
    """
    The `sum` function takes a Point object as input and returns a new Point object with the sum of the x and y coordinates of the two points.

    :param i_point: The `i_point` parameter in the `sum` method seems to represent another Point object that you want to add to the current Point object. The method calculates the sum of the x and y coordinates of the current Point object (`self`) with the x and y coordinates of the `i_point`
    :return: A new Point object is being returned, with the x-coordinate being the sum of the x-coordinates of the two points (self and i_point), and the y-coordinate being the sum of the y-coordinates of the two points.
    """
    return Point(self.__x + i_point.__x, self.__y + i_point.__y)

  def real_product(self, i_number: float):
    """
    This function takes a floating-point number as input and returns a new Point object with its coordinates multiplied by that number.

    :param i_number: The `i_number` parameter in the `real_product` method is a floating-point number that is used to multiply the `x` and `y` coordinates of a `Point` object. The method returns a new `Point` object with the coordinates multiplied by the `i_number` value
    :type i_number: float
    :return: The `real_product` method is returning a new `Point` object with coordinates that are the product of the current `Point` object's coordinates (`self.__x` and `self.__y`) and the input `i_number`.
    """
    return Point(self.__x * i_number, self.__y * i_number)

  def get_x(self):
    return self.__x

  def get_y(self):
    return self.__y



