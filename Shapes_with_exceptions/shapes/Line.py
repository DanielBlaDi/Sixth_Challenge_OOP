from shapes.Point import Point
import math


class Line:
  definition: str = "It's a join between two points"

  def __init__(self, start_point: Point, end_point: Point):
    self.__start_point = start_point
    self.__end_point = end_point

  def length(self):
    """
    The `length` function calculates the distance between the start and end points of a line segment.
    :return: The `length` method is returning the distance between the `__start_point` and `__end_point` of the object.
    """
    return self.__start_point.compute_distance(self.__end_point)

  def get_starting_point(self):
    return self.__start_point

  def get_ending_point(self):
    return self.__end_point

  def to_vector(self):
    """
    The function `to_vector` calculates the vector between the end point and the start point.
    :return: The `to_vector` method is returning the vector that starts from the `start_point` and ends at the `end_point`. The vector is calculated by subtracting the `start_point` from the `end_point`.
    """
    return self.__end_point.sum(self.__start_point.real_product(-1))

  def compute_angle(self, i_line):
    try:
      """
      The function computes the angle between two vectors represented by self and i_line.
  
      :param i_line: It looks like you have provided a code snippet for computing the angle between two vectors represented by `self` and `i_line`. However, the information about `i_line` is missing. Could you please provide more details about `i_line` so that I can assist you further with the computation of
      :return: The function `compute_angle` calculates the angle between the self vector and the input vector `i_line` using the dot product formula. It then converts the cosine of the angle to degrees using the `math.acos` and `math.degrees` functions. The rounded angle in degrees is returned.
      """
      self_vector = self.to_vector()
      i_vector = i_line.to_vector()
  
      magnitude_product = (self_vector.magnitude() * i_vector.magnitude())
      cos = self_vector.dot_product(i_vector) / magnitude_product   #take care with the division by zero
  
      return round(math.degrees(math.acos(cos)), 3)
    except ZeroDivisionError as error:
      print(f"Error: {error}")

  def reverse(self):
    """
    The `reverse` function in the given Python code snippet returns a new Line object with its start and end points swapped.
    :return: The `reverse` method is returning a new `Line` object with the start and end points swapped.
    """
    return Line(self.__end_point, self.__start_point)
