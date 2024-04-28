from shapes.Point import Point
from shapes.Shape import Shape
from shapes.figures.Rectangle import Rectangle
from shapes.figures.Square import Square
from shapes.figures.Triangle import Triangle
from shapes.figures.Equilateral import Equilateral
from shapes.figures.Scalene import Scalene
from shapes.figures.Isosceles import Isosceles
from shapes.figures.TriRectangle import TriRectangle
from shapes.Error import UserError

if __name__ == "__main__":
  print(
      "Welcome to this code, this could calculate the area, the perimeter  and the \
inner angles of a shape")
  print("You could choose one of this shapes: ")
  print("rectangle, square, triangle, isosceles triangle, \
equilateral triangle, scalene triangle, TriRectangle, other figure")
  # This Python function is used to get the user's figure and validate it.
  shape: str = input("Write the name of the shape that you want to use: ")
  fuction: bool = True  #Ayuda al final a imprimir
  #los valores si se escogio una figura

  # This Python function depending on the ``shape`` value, ask some datums and realize the corresponding operation for calculating the area, perimeter and inner angles.
  try:
    match shape:
      case "rectangle":
        print("You chose a rectangle")
        center = Point(float(input("Write the x coordinate of the center: ")),
                       float(input("Write the y coordinate of the center: ")))

        width = float(input("Write the width of the rectangle: "))
        height = float(input("Write the height of the rectangle: "))
        my_shape = Rectangle(i_center=center, i_width=width, i_height=height)

      case "square":
        print("You chose a square")
        center = Point(float(input("Write the x coordinate of the center: ")),
                       float(input("Write the y coordinate of the center: ")))

        size = float(input("Write the size of the square: "))
        my_shape = Square(i_center=center, i_size=size)

      case "triangle":
        print("You chose a triangle")
        vertices = []
        for i in range(3):
          x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
          y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
          vertices.append(Point(x=x, y=y))
        my_shape = Triangle(vertices=vertices)

      case "isosceles triangle":
        print("You chose a isosceles triangle")
        vertices = []
        for i in range(3):
          x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
          y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
          vertices.append(Point(x=x, y=y))
        my_shape = Isosceles(vertices=vertices)

      case "equilateral triangle":
        print("You chose a equilateral triangle")
        vertices = []
        for i in range(3):
          x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
          y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
          vertices.append(Point(x=x, y=y))
        my_shape = Equilateral(vertices=vertices)

      case "scalene triangle":
        print("You chose a scalene triangle")
        vertices = []
        for i in range(3):
          x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
          y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
          vertices.append(Point(x=x, y=y))
        my_shape = Scalene(vertices=vertices)

      case "TriRectangle":
        print("You chose a TriRectangle")
        vertices = []
        for i in range(3):
          x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
          y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
          vertices.append(Point(x=x, y=y))
        my_shape = TriRectangle(vertices=vertices)

      case "other figure":
        print("You chose an other figure: ")
        number_vertices = 0
        while number_vertices < 3:
          number_vertices: int = int(
              input(
                  "Write the number of vertices of your figure (it can`t have less than 3 vertices): "
              ))
        vertices = []
        for i in range(number_vertices):
          x = float(input(f"Write the x coordinate of the vertex {i + 1}: "))
          y = float(input(f"Write the y coordinate of the vertex {i + 1}: "))
          vertices.append(Point(x=x, y=y))
        my_shape = Shape(vertices=vertices)

      case _:
        print("Invalid shape")
        fuction: bool = False

    # This part is used to print the area, perimeter and inner angles of the user`s shape.
    if fuction:
      print("The perimeter of the shape is",
            round(my_shape.compute_perimeter(), 3))
      print("The area of the shape is", round(my_shape.compute_area(), 4))
      print("The inner angles of the shape are", my_shape.compute_inner_angles())
      print("The shape is regular", my_shape.is_regular())
    else:
      print("Reset the program ")
  

  except ValueError:
    print(
        "Invalid input, you should write numbers as integer or float not as strings"
    )
  except IndexError as error:
    print(f"Error: {error}")


  except UserError as error:
    print(f"Error: {error}")


