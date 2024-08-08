def withdraw(balance, amount):
  if amount > balance:
      print("Insufficient funds.")
  else:
      balance -= amount
      print(f"Withdrawal successful. New balance: {balance}")
  return balance

def deposit(balance, amount):
  balance += amount
  print(f"Deposit successful. New balance: {balance}")
  return balance

def check_balance(balance):
  print(f"Your current balance is: {balance}")

def askToContinue():
  while True:
      tryAgain = input("Do you want to continue your transactions? (Y/N): ").strip().upper()
      if tryAgain == "Y":
          return True
      elif tryAgain == "N":
          return False
      else:
          print("Invalid input. Please enter 'Y' or 'N'.")

balance = 300.00
while True:
  print(f"\nWelcome to the ATM!")
  print("1. Withdraw")
  print("2. Deposit")
  print("3. Check Balance")
  print("4. Quit")
  print("")
  choice = input("Enter your choice (1-4): ")
  if choice == "1":
      amount = float(input("Enter the amount to withdraw: "))
      balance = withdraw(balance, amount)
  elif choice == "2":
      amount = float(input("Enter the amount to deposit: "))
      balance = deposit(balance, amount)
  elif choice == "3":
      check_balance(balance)
  elif choice == "4":
      print("Thank you for using the ATM. Goodbye!")
      break
  else:
      print("Invalid choice. Please try again.")

  if not askToContinue():
      print("Thank you for using the ATM. Goodbye!")
      break
