# Bin class, each bin has a capacity and a list of items. This will be used in binpacking.py

class Bin:
    def __init__(self, capacity):
        self.capacity = capacity
        self.effectiveCapacity = capacity
        self.items = []

    def add(self, item):
        if self.effectiveCapacity >= item.effectiveWeight():
            self.items.append(item)
            self.effectiveCapacity -= item.effectiveWeight()
            return True
        else:
            print("Item with weight " + str(item.effectiveWeight()) + " cannot be added to bin with effective capacity " + str(self.effectiveCapacity))
            return False

    def __str__(self):
        ret = f"Bin with capacity {str(self.effectiveCapacity)} ({self.capacity}):\n"

        for item in self.items:
            ret += "\t" + str(item) + "\n"

        return ret