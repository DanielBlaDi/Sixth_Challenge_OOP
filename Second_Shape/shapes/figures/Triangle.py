from shapes.Shape import Shape


class Triangle(Shape):
  def __init__(self, vertices: list):
      super().__init__(vertices)
  """
  This Python function calculates the area of a triangle using its side lengths.
  :return: The code is calculating the area of a triangle using Heron's formula and returning the calculated area.
  """
  def compute_area(self):
      side1_lenght1=self.get_edges()[0].length()
      side2_lenght2=self.get_edges()[1].length()
      side3_lenght3=self.get_edges()[2].length()
      s=(side1_lenght1+side2_lenght2+side3_lenght3)/2
      area=(s*(s-side1_lenght1)*(s-side2_lenght2)*(s-side3_lenght3)**0.5)
      return area

  """
    The function `compute_perimeter` calculates the perimeter of a shape by summing the lengths of its edges.
    :return: The `compute_perimeter` method calculates the perimeter of a shape by iterating through its edges and summing up their lengths. The method returns the total perimeter of the shape.
  """

  def compute_perimeter(self):

      perimeter = 0
      for line in self.get_edges():
          perimeter += line.length()
      return perimeter
