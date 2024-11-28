def divide_elements(values, divisor):
    try:
        return [values / divisor for values in values]
    except ZeroDivisionError:
        print("Zero Division Error")
    except TypeError:
        print("Type Error")
    return None
values = [10, 20, 30]
print(divide_elements(values, 2))
print(divide_elements(values, 0))
print(divide_elements(values, "a"))