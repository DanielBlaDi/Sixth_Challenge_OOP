from type_selector import type_sel

class InvalidSignError(Exception):
  """
  Special exception created for this code

  Args:
    message: You enter an invalid sign
  """

  def __init__(self, message):
    super().__init__(message)

def calculator(first_numb, second_numb, oper):
    '''This function receives a word and returns True or false
    depending on whether the word is a palindrome or not'''
    
    y, z = first_numb, second_numb # Transform both values: str into values: int, and assigning a variable for each one
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

if __name__ == "__main__": # Function main, the starting point of the code

    starter: bool = True

    # This fuction let you choose with wich numbers would you like to work (integer or float)
    type_input = type_sel()

    while starter:
        
        print("This program is a basic calculator")

        try:
            fst = type_input(input("Enter the first number: ")) # Receive the values for the operation
            scd = type_input(input("Enter the second number: "))
            oper: str = input("Enter the sing of operation that you wanna do (+, -, /, *): ") # You can't dive by 0, so we add a conditional
            print("The result of this operation is: ", calculator(fst, scd, oper))
            starter: bool = False

        except ValueError:
            print("You can't enter a string in the numbers input")

        except ZeroDivisionError:
            print("You can't divide by 0 ")

        except InvalidSignError as error:
            print(f"Error {error}")

        