def addition(a, b):
  result = a + b
  return result


def subtraction(a, b):
  result = a - b
  return result


def multiplication(a, b):
  result = a * b
  return result


def division(a, b):
  if b != 0:
    result = a / b
  else:
    result = "Error: Division by zero"
  return result


# To prevent unnecessary decimals
def resultFormat(result):
  if isinstance(result, str):
    return result
  elif result.is_integer():
    return int(result)
  else:
    return result


a = float(input("Enter an operand here: "))
b = float(input("Enter an operand here: "))

print("Sum: ", resultFormat(addition(a, b)))
print("Difference: ", resultFormat(subtraction(a, b)))
print("Product: ", resultFormat(multiplication(a, b)))
print("Quotient", resultFormat(division(a, b)))
