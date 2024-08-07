#Inputs
p = float(input("Enter the Principal or Initial amount: "))
r = float(input("Enter the Rate of Interest(in percent): "))
t = float(input("How many years will the money be invested for: "))

#Computations
percentage = r / 100
simpleInterest = p * percentage * t

#Output
print("The simple interest is: ", simpleInterest)