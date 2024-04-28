import math
import copy
from shapes.Line import Line
from shapes.Error import UserError


class Shape:
    def __init__(self, vertices: list):
      self.__vertices = vertices

      # Makes a verification of the vertices, preventing there were two equal vertices

      different_vertices = []

      for vertices_comparer in vertices:
        if vertices_comparer not in different_vertices or different_vertices == []:
          different_vertices.append(vertices_comparer)        

      if len(different_vertices) != len(vertices):
        raise UserError(f"Vertices are not unique {vertices}")

      
      self.__edges = []
      for i in range(len(vertices) - 1):
        self.__edges.append(Line(vertices[i], vertices[i + 1]))
      if vertices[0] != vertices[-1]:
        self.__edges.append(Line(vertices[-1], vertices[0]))
        self.__vertices.append(vertices[0])

      

      


      self.__is_regular = True
      #compare lenghts
      for i in range(len(self.__edges) - 1):
        if self.__edges[i].length() != self.__edges[i + 1].length():
          self.__is_regular = False
          break

      angles = self.compute_inner_angles()
      for i in range(len(angles) - 1):
        if angles[i] != angles[i + 1]:
          self.__is_regular = False
          break

    def compute_area(self):
      
      """
      The function computes the area of a polygon using the vertices provided.
      :return: The `compute_area` method is calculating the area of a polygon using the vertices stored in `self.__vertices`. It appears to be using the Shoelace formula to calculate the area. The method returns the absolute value of half the difference between two sums calculated using the vertices.
      """
      
      sum = 0
      for i in range(len(self.__vertices) - 1):
        sum += self.__vertices[i].get_x() * self.__vertices[i + 1].get_y()
      sum += self.__vertices[-1].get_x() * self.__vertices[0].get_y()

      other_sum = 0
      for i in range(len(self.__vertices) - 1):
        sum += self.__vertices[i + 1].get_x() * self.__vertices[i].get_y()
      other_sum += (self.__vertices[0].get_x() * self.__vertices[-1].get_y())
      return math.fabs(sum - other_sum) / 2
      
    def compute_perimeter(self):
      """
      This Python function calculates the perimeter of a shape based on the lengths of its edges.
      :return: The `compute_perimeter` method is returning the total perimeter of the shape represented by the edges stored in the `self.__edges` list. The method calculates the perimeter by iterating over each edge in the list and adding up the length of each edge. The final result is the total perimeter of the shape.
      """
      
      perimeter = 0.0
      for line in self.__edges:
        perimeter += line.length()
      return perimeter

    def compute_inner_angles(self):
      """
      This Python function computes the inner angles between edges in a polygon.
      :return: The function `compute_inner_angles` returns a list of angles calculated between consecutive edges in a polygon, including the angle between the last and first edges to complete the inner angles of the polygon.
      """
      
      angles = []
      for i in range(0, len(self.__edges) - 1):
        angle =self.__edges[i].reverse().compute_angle(self.__edges[i + 1])
        angles.append(angle)
      angles.append(self.__edges[0].compute_angle(self.__edges[-1].reverse()))
      return angles

    def is_regular(self):#This Python function determine if the shape is regular ot not.
      
      return self.__is_regular

    def get_vertices(self):
      
      return self.__vertices

    def get_edges(self):
      
      return self.__edges
