class BankAccount:
  def __init__(self, account, balance):
    self.account= account
    self.balance= float(balance)
    
  def deposit(self, input_Dep):
    self.balance += input_Dep
    return f"Deposit Input: {input_Dep}. Current balance: {self.balance} php"
  
  def withdraw(self, input_Withdraw):
    if self.balance < input_Withdraw:
      return f"Error: Insufficient Funds for Withdrawal! Current balance is {self.balance}"
    elif self.balance >= input_Withdraw:
      self.balance -= input_Withdraw
      return f"Withdrew {input_Withdraw}php. Current balance is {self.balance} php"
    
  def __str__(self):
    return f"""\nGood Day {self.account}!
  How may we help you today?se
  
  Personal Information
  Bank Account: {self.account}
  Current Balance: {self.balance} php"""
  
print("Please enter your Bank Account Name and your Current Balance.")
account= input("Enter your Bank Account Name: ")
balance= input("Enter your current balance: ")
test= BankAccount(account, balance)
print(test)

dec= input("\nWould you like to Withdraw or Deposit? (W / D): ")
decision= dec.upper()
if decision == "W":
  input_Withdraw= float(input("Enter the amount you would like to withdraw: "))
  print(test.withdraw(input_Withdraw))
elif decision == "D":
  input_Dep= float(input("Enter the amount you would like to deposit: "))
  print(test.deposit(input_Dep))
else:
  print("Error: Enter a valid input {self.account}.")