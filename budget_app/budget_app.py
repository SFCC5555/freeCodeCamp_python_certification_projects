# --Budget App--


class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = "".join(
            f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
            for item in self.ledger
        )
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    # Calculate the percentage spent for each category
    withdrawals_list = []
    for category in categories:
        withdrawals = sum(
            -item["amount"] for item in category.ledger if item["amount"] < 0
        )

        withdrawals_list.append(withdrawals)

    total_wiwithdrawals = sum(withdrawals_list)

    spent_percentages = [
        (withdrawal / total_wiwithdrawals) * 100 for withdrawal in withdrawals_list
    ]
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for percent in spent_percentages:
            chart += "o" if percent >= i else " "
            chart += "  "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    max_name_length = max(len(category.category) for category in categories)

    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += f"{category.category[i]}  "
            else:
                chart += "   "
        chart += "\n"

    return chart.strip("\n")


if __name__ == "__main__":
    food_budget = Category("Food")
    clothing_budget = Category("Clothing")
    auto_budget = Category("Auto")

    food_budget.deposit(1000, "initial deposit")
    food_budget.withdraw(10.15, "groceries")
    food_budget.withdraw(15.89, "restaurant and more foo")

    clothing_budget.deposit(500, "initial deposit")
    clothing_budget.withdraw(50, "clothing and accessories")

    auto_budget.deposit(1500, "initial deposit")
    auto_budget.withdraw(75.99, "gas and fuel")

    print(create_spend_chart([food_budget, clothing_budget, auto_budget]))
