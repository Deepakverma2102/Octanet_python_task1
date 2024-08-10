class ATM:
    def __init__(self, pin, balance=0):
        # Initialize the ATM with a PIN and an optional starting balance
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self):
        # Function to verify the PIN entered by the user
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def show_balance(self):
        # Function to display the current balance
        print(f"Your current balance is: ${self.balance}")

    def deposit_cash(self, amount):
        # Function to deposit cash and update balance
        self.balance += amount
        print(f"${amount} deposited successfully.")
        self.transaction_history.append(f"Deposited: ${amount}")

    def withdraw_cash(self, amount):
        # Function to withdraw cash if there are sufficient funds
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.transaction_history.append(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance.")

    def change_pin(self):
        # Function to change the user's PIN
        new_pin = input("Enter your new PIN: ")
        self.pin = new_pin
        print("PIN changed successfully.")
        self.transaction_history.append("PIN changed")

    def show_transaction_history(self):
        # Function to display the transaction history
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

def main():
    # Main function to drive the ATM simulation
    # Initialize the ATM with a default PIN and starting balance
    atm = ATM(pin="1234", balance=1000)
    
    print("Welcome to the ATM!")
    while True:
        if atm.check_pin():
            print("\nPlease choose an option:")
            print("1. Balance Inquiry")
            print("2. Cash Deposit")
            print("3. Cash Withdrawal")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                atm.show_balance()
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                atm.deposit_cash(amount)
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw_cash(amount)
            elif choice == "4":
                atm.change_pin()
            elif choice == "5":
                atm.show_transaction_history()
            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            continue

# Run the ATM simulation
if __name__ == "__main__":
    main()
