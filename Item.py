class Item:
    def __init__(self, weight, amount):
        self.weight = weight
        self.amount = amount

    def __str__(self):
        return "Weight: " + str(self.weight) + " Amount: " + str(self.amount)

    def effectiveWeight(self):
        return self.weight * self.amount