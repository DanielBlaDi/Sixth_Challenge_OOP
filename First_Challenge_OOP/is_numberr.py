def is_number(x):
    try:
        if int(x) or float(x):
            return True
    except ValueError:
        return False