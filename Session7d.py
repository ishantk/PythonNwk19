class Counter:

    def __init__(self):
        self.count = 1

    def increment(self):
        self.count = self.count + 1

    def showCount(self):
        print(">> count is:", self.count)


c1 = Counter()  # Counter() -> Object Construction and execute constructor
c2 = Counter()  # Counter() -> Object Construction and execute constructor
c3 = c1         # reference copy

# --- 2 Objects ---
# c1/c3   |       c2
# 1       |       1
# 2               2
# 3               3
# 4
# 5

c1.increment()  # 2
c2.increment()  # 2
c3.increment()  # 3

c1.increment()  # 4
c2.increment()  # 3
c1.increment()  # 5

# How many Objects are created in memory: 2
c1.showCount()  # >> count is: 5
c2.showCount()  # >> count is: 3
c3.showCount()  # >> count is: 5

# 2, 5, 3, 5

