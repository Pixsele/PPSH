import abc


class Transfeable(abc.ABC):
    @abc.abstractmethod
    def transfer(self):
        pass

class Transfer_Service():
    def __init__(self,sourse_id,distination_id,amount):
        self.sourse_id = sourse_id
        self.distination_id = distination_id
        self.amount = amount
    def transfer(self):
        self.sourse_id.transfer(self.distination_id,self.amount)

class Account(Transfeable):
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self,summa):
        self.balance += summa

    def withdraw(self,summa):
        self.balance -= summa

    def transfer(self,distination_id,amount):
        if self.balance >= amount:
            self.withdraw(amount)
            distination_id.deposit(amount)
        else:
            raise ValueError('Недостаточно средст')


class SavingAccount(Account):
    def __init__(self,id,name,balance,interest_rate):
        super().__init__(id,name,balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def get_interest_rate(self):
        self.balance += self.balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self,id,name,balance,fee_percentage):
        super().__init__(id,name,balance)
        self.fee_percentage = fee_percentage

    def deduct_fees(self):
        self.balance -= self.balance * self.fee_percentage

    def get_fee_percentage(self):
        self.balance += self.balance * self.fee_percentage


class Bank():
    def __init__(self):
        self.storage = []

    def found_account(self,desired):
        for account in self.storage:
            if account.id == desired:
                return account
        return None

    def add_account(self,account):
        if self.found_account(account) == None:
            self.storage.append(account)
        else:
            raise AttributeError

    def delete_account(self,account):
        if self.found_account(account.id) != None:
            self.storage.remove(account)
        else:
            raise AttributeError

    def transfer_funds(self,sourse_id,destination_id,amount):
        sourse = self.found_account(sourse_id)
        destination = self.found_account(destination_id)
        if sourse != None and destination != None:
            transfer_operation = Transfer_Service(sourse,destination,amount)
            transfer_operation.transfer()
        else:
            ValueError('Некорректные ID')


savings_account = SavingAccount("SAV-001",'AR',1000, 5)
checking_account = CheckingAccount("CHK-001",'AV',500, 2)


bank = Bank()
bank.add_account(savings_account)
bank.add_account(checking_account)

print("Savings Account Balance:", savings_account.get_balance())
print("Checking Account Balance:", checking_account.get_balance())

bank.transfer_funds("SAV-001", "CHK-001", 1000)

print("Savings Account Balance:", savings_account.get_balance())
print("Checking Account Balance:", checking_account.get_balance())