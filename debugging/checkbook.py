class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and balance inquiries.
    """

    def __init__(self):
        """
        Initialize a Checkbook object with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook balance.

        Parameters:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook balance.

        Parameters:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to run the checkbook program.
    Provides a user interface for depositing, withdrawing, checking balance, and exiting.

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Deposit amount must be positive. Please try again.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Withdrawal amount must be positive. Please try again.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()