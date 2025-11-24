class Banking:
    def __init__(self, name, account_number, account_balance, pin):
        self.name = name
        self.__account_number = account_number
        self.__account_balance = account_balance
        self.__pin = pin
        self.__failed_attempts = 0
        self.__blocked = False

    # -------------------------
    # PIN Validation
    # -------------------------
    def __validate_pin(self, pin):
        if self.__blocked:
            print("Account is blocked, contact support.")
            return False

        if pin == self.__pin:
            self.__failed_attempts = 0
            return True
        else:
            self.__failed_attempts += 1
            print("Incorrect Pin!")

        if self.__failed_attempts >= 3:
            self.__blocked = True
            print("Account is BLOCKED due to 3 wrong attempts!")

        return False

    # -------------------------
    # Check Balance
    # -------------------------
    def check_balance(self, pin):
        if self.__validate_pin(pin):
            print(f"Balance of {self.name} is: ₹{self.__account_balance}")

    # -------------------------
    # Deposit Money
    # -------------------------
    def deposit(self, pin, amount):
        if self.__validate_pin(pin):
            if amount > 0:
                self.__account_balance += amount
                print(f"₹{amount} deposited successfully!")
            else:
                print("Invalid deposit amount")

    # -------------------------
    # Withdraw Money
    # -------------------------
    def withdraw(self, pin, amount):
        if self.__validate_pin(pin):
            if amount <= 0:
                print("Invalid amount")
            elif self.__account_balance >= amount:
                self.__account_balance -= amount
                print(f"₹{amount} withdrawn successfully!")
            else:
                print("Insufficient Balance!")

    # -------------------------
    # Transfer Money
    # -------------------------
    def transfer(self, pin, amount, receiverAccount):
        if self.__validate_pin(pin):
            if amount <= 0:
                print("Invalid amount")
            elif self.__account_balance >= amount:
                self.__account_balance -= amount
                receiverAccount.__account_balance += amount
                print(f"₹{amount} transferred successfully to {receiverAccount.name}")
            else:
                print("Gareeb kya dekh raha hai, paise kama pehle! 😂")

acc1 = Banking("Vijay", 101, 5000, 1111)
acc2 = Banking("Rahul", 102, 3000, 2222)

print("---- Checking Balance ----")
acc1.check_balance(1111)

print("---- Deposit ----")
acc1.deposit(1111, 2000)

print("---- Withdraw ----")
acc1.withdraw(1111, 1000)

print("---- Transfer ----")
acc1.transfer(1111, 500, acc2)

print("---- Wrong PIN test ----")
acc1.withdraw(1234, 100)
acc1.withdraw(9999, 100)
acc1.withdraw(7777, 100)
