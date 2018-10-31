"""
Exercise 1: (5 points)

a) Using the slides & the script, put together a file
    containing the complete Account class.
    Each method must have a documentation string at the
    beginning which describes what the method is doing.
    (1 points)

b) Create a main application where you create a number of accounts.
    Play around with depositing / withdrawing money.
    Change the account holder of an account using a setter method.
    (1 point)

c) Change the withdraw function such that the minimum balance
    allowed is -1000.
    (1 point)

d) Write a function apply_interest(self) which applies an interest
    rate of 1.5% to the current balance and call it on your objects.
    (1 points)

e) Draw a UML diagram representing your Account class. (1 point)

"""


class Account:
    """ The class contains a constructor that sets the account
    holder and first deposit. Functions deposit(), withdraw(),
    apply_interest() modify the account balance. Functon
    set_holder() changes the account holder.
    """

    def __init__(self, number, holder, start_balance):
        """
        create account, set account ID, holder and first
        deposit(start balance)
        """
        self.number = number
        self.holder = holder
        self.balance = start_balance

    def __str__(self):
        """
        string representation of the account object
        """
        res = "*** Account Info ***\n"
        res += "Account ID: " + str(self.number) + "\n"
        res += "Holder: " + self.holder + "\n"
        res += "Balance: " + str(self.balance) + "\n"
        return res

    def deposit(self, amount):
        """
        used on an account object, amount = money deposited
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        used on an account object, amount = money withdrawn;
        limit is set so that the balance afterwards cannot
        be lower than -1000
        """
        if self.balance - amount <= -1000:
            print("Account balance cannot be lower than -1000!")
            print("Try another amount.")
        else:
            self.balance -= amount

    def set_holder(self, new_holder):
        """
        in case the account holder needs to be changed,
        new_holder = name of the new holder
        """
        self.holder = new_holder

    def apply_interest(self):
        """
        apply interest of 1.5%
        the balance is multiplied by 1.015
        """
        self.balance = round(self.balance * 1.015)

if __name__ == "__main__":
    print("Welcome to the Stirnlappenbasilisk Bank!")

    print("Tom Sawyer opens an account and deposits $1000.")
    account1 = Account(1, "Tom Sawyer", 1000)

    account1.deposit(150)
    print("Tom deposits $150 more on his account.")
    print("The current balance is $" + str(account1.balance) + ".")

    print("Tom tries to withdraw $5000.")
    account1.withdraw(5000)

    account1.withdraw(1000)
    print("Tom withdraws $1000")
    print("The current balance is $" + str(account1.balance) + ".")

    account1.set_holder("Huck Finn")
    print("The account now belongs to Huck Finn")
    print("Huck Finn has $" + str(account1.balance) + " on his account.")

    account1.apply_interest()
    print("An interest of 1.5% is applied on Huck's account.")
    print("The current balance is $" + str(account1.balance) + ".")
