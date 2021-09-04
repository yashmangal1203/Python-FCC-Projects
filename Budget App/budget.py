class Category:
    def __init__(self, name):
        self.name = name
        self._ledger = list()
    
    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        totalstr = ''
        total = 0
        lines = ''
        for entry in self._ledger:
            amount = entry["amount"]
            description = entry["description"][:23]
            lines += f"{description:<23}" + \
                f"{amount:>7.2f}"+'\n'
            total += entry["amount"]
        totalstr = 'Total: '+str(total)
        return title + lines + totalstr

    def deposit(self, amount, description=""):
        """
        A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
        """
        self._ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
        """
        if (self.check_funds(amount)):
            self._ledger.append({"amount": -1*amount, "description": description})
            return True
        return False

    def get_balance(self):
        """
        A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
        """
        cuurent_balance = 0
        for entry in self._ledger:
            cuurent_balance += entry["amount"]
        return cuurent_balance

    def transfer(self, amount, category):
        """
        A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
        """
        if (self.check_funds(amount)):
            self.withdraw(amount, "Transfer to "+category.name)
            category.deposit(amount, "Transfer from "+self.name)
            return True
        return False

    def check_funds(self, amount):
        """
        A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
        """
        if amount > self.get_balance():
            return False
        return True


def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    spending = {}
    line = ''
    for category in categories:
        for i in category._ledger:
            if i["amount"] < 0:
                spending.setdefault(category.name, 0)
                spending[category.name] += round(i["amount"])
    total = round(sum(spending.values()))
    percentageSpent = list(map(lambda amount: int((((amount/total)*10)//1)*10), spending.values()))

    for i in range(100, -10, -10):
        line += str(i).rjust(3, " ")+"|"
        for percentage in percentageSpent:
            if percentage >= i:
                line += ' o '
            else:
                line += '   '
        line += ' \n'
    footer = '-'*(len(percentageSpent)*3+1)
    line += footer.rjust(len(footer)+4, ' ')+'\n'
    footer = ''
    biggestname = max(spending.keys(), key=len)
    for i in range(len(biggestname)):
        footer += '     '
        for name in spending.keys():
            if i >= len(name):
                footer += '   '
            else:
                footer += name[i]+'  '
        if (i != len(biggestname)-1):
            footer += '\n'

    return title+line+footer


