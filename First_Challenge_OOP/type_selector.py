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