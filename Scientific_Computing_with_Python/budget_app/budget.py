class Category:
    def __init__(self, name):
        # from description i guess i shouldn't
        # store the current balance ???
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance
    
    def transfer(self, amount, category):
        if self.withdraw(amount, "Transfer to " + category.name):
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False
    
    def check_funds(self, amount):
        return not self.get_balance() < amount

    def get_spendings(self):
        sum = 0
        for item in self.ledger:
            if item["amount"] < 0:
                sum -= item["amount"]
        return sum
  
    def __str__(self):
        # title line
        title = self.name.center(30, "*")

        # ledger items
        items = ""
        for item in self.ledger:
            desc = "{:<23}".format(item["description"])[:23]
            amount = "{:>7.2f}".format(float(item["amount"]))[-7:]
            items += "\n" + desc + amount

        # Total
        total = "\nTotal: " + "{:.2f}".format(float(self.get_balance()))
        return title + items + total


def create_spend_chart(categories):
    amounts = {}
    sum = 0
    for cat in categories:
        cat_spend = cat.get_spendings()
        amounts[cat.name] = cat_spend
        sum += cat_spend
    
    cats = [(key, (value * 10) // sum) for key, value in amounts.items()]
    
    title = "Percentage spent by category"
    chart = ""
    for i in range(10, -1, -1):
        line = "\n" + str(i * 10).rjust(3) + "|"
        for _, v in cats:
            if(v >= i):
                line += " o "
            else:
                line += " " * 3
        chart += line + " "
      
    footer = "\n    " + "-" * (3 * len(cats) + 1)
    max_length = len(max(cats, key=lambda item : len(item[0]))[0])

    for i in range(max_length):
        footer += "\n    "
        for key, _ in cats:
            if len(key) > i:
                footer += " " + key[i] + " "
            else:
                footer += " " * 3
        footer += " "
    return title + chart + footer