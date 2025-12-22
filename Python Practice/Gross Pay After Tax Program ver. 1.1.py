class tax:
    def __init__(self, input_Gross):
        self.input_Gross= input_Gross
        
    def to_Pay(self, input_Gross):
        if input_Gross in range(0, 10000):
           print("Tax Rate: 0%")
           print("Tax Amount: 0.00 php")
           print(f"Total Amount to Pay after Taxes: {input_Gross} ")
           
        elif input_Gross in range (10000, 50000):
            print("Tax Rate: 10%")
            tax_Amount= input_Gross * 0.10
            print(f"Tax Amount= {tax_Amount}")
            total_Amount= input_Gross + tax_Amount
            print(f"Total Amount to Pay after Taxes: {total_Amount}")
            
        elif input_Gross >= 50000:
            print("Tax Rate: 50%")
            tax_Amount= input_Gross * 0.50
            print(f"Tax Amount= {tax_Amount}")
            total_Amount= input_Gross + tax_Amount
            print(f"Total Amount to Pay after Taxes: {total_Amount}")
            
while(True):
    print("""
Total Amount After Tax Program
Enter the Amount you want to pay and the program will calculate the total amount you need to pay after taxes""")
    
    input_Gross= int(input(f"Input that amount to pay: "))
    taxing= tax(input_Gross)
    taxing.to_Pay(input_Gross)
    
    decision= input("\nDo you want to continue? (y/n): ")
    dec= decision.lower()
    if dec == "n":
        print("Thank you for using our program!")
        break