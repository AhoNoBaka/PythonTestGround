def celsiusToFahrenheit(celsius):
  return (celsius * 9 / 5) + 32

def farhenheitToCelsius(farhenheit):
  return (farhenheit - 32) * 5 / 9

while True:
  mode = input('Type "F" to convert Fahrenheit to Celsius or "C" to convert Celsius to Fahrenheit (or type "Q" to quit): ').strip().upper()

  if mode == "F":
    try:
      farhenheit = float(input("Enter the temperature in Fahrenheit: "))
      c = farhenheitToCelsius(farhenheit)
      print(f"The temperature in Celsius is: {c:.2f}°C")
    except ValueError:
      print("Please enter a numeric value in the temperature.")

  elif mode == "C":
    try:
      celsius = float(input("Enter the temperature in Celsius: "))
      f = celsiusToFahrenheit(celsius)
      print(f"The temperature in Fahrenheit is: {f:.2f}°F")
    except ValueError:
      print("Please enter a numeric value in the temperature.")

  elif mode == "Q":
    print("Goodbye!")
    break

  else:
    print("Invalid mode. Please type 'F', 'C', or 'Q'.")