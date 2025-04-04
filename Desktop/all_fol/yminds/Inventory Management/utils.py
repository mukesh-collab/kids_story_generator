def validate_positive_int(value):
    try:
        value = int(value)
        if value < 0:
            raise ValueError()
        return value
    except ValueError:
        raise ValueError("Value must be a non-negative integer.")

def validate_positive_float(value):
    try:
        fvalue = float(value)
        if fvalue < 0:
            raise ValueError()
        return fvalue
    except ValueError:
        raise ValueError("Value must be a non-negative number.")
