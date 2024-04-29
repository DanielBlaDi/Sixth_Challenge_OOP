# Sixth_Challenge
In this challenge we have to take the code of the [last challenge](https://github.com/DanielBlaDi/fifth_Challenge_OOP), Shapes and making exceptions on it and also, making exceptions in the code of the [first_repository](https://github.com/DanielBlaDi/First_Challenge_OOP) that we made for OOP class:

## First_repository

I added the commonly exceptions like `ValueError` - `ZeroDivisionError` - `TypeError`, also I created me own exceptions:

- InvalidSignError
That apper when the user don't select one of the following operation sings: `+`, `-`, `*`, `/`

```python
match oper: # Use "match" to no use "elif" (The last one could make the same thing)
        case "+": # It evaluates the value of oper and, dependent on it, makes a determinate operation
            return y + z
        case "-":
            return y - z
        case "*":
            return y * z
        case "/":
            return y / z
        case _:
            raise InvalidSignError("Invalid sign")
```


Also I create two fuctions fuctions that I import to some modules:

1. ### `type_selector`
This let the user select the type of numbers that he wanna operate


```python
def type_sel() -> type:
    print("Would you like to work with integers or floats numbers")
    starter: bool = True
    while starter:
        type_input: str = input("Enter i for integers and f for floats: ")
        if type_input == "f":
            return float
            starter = False
        elif type_input == "i":
            return int
            starter = False
        else:
            print("Invalid input, try again")
```


2. ### `is_number`
In the `second_point.py` and `fifth_point.py` I raise an error when the user enter a string of numbers and not a word (string of letters)


```python
if is_number(x):
            raise TypeError("You enter a str of numbers not a word (str of letters)")
```


This fuction let the program know when it happens


```python
def is_number(x):
    try:
        if int(x) or float(x):
            return True
    except ValueError:
        return False
```


## Shape

We add some exceptions in this package, the new exceptions made:


1. The user can't enter strings in the program where it doesn't correspond


2. We created an own exception that appers when the user add more than two times the same vertex, this stop the program 
and don't let the program create the object

```python
different_vertices = []

      for vertices_comparer in vertices:
        if vertices_comparer not in different_vertices or different_vertices == []:
          different_vertices.append(vertices_comparer)        

      if len(different_vertices) != len(vertices):
        raise UserError(f"Vertices are not unique {vertices}")
```


