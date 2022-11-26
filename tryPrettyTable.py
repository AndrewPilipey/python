from prettytable import PrettyTable
from collections import Counter

x = Counter("ABC")
y = Counter("DEF")
z = Counter("GHI")
print(x, y, z)

table = PrettyTable()
table.field_names = ["Letters 1", "Letters 2", "Letters 3"]
table.add_row(["ABC", "DEF", "GHI"])
table.add_row([x, y, z])

print(table)