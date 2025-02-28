# https://docs.python.org/3/library/collections.html#collections.Counter

from collections import Counter

inventory = Counter()

loot = {'sword': 1, 'bread': 3}

inventory.update(loot)
print(inventory)

more_loot = {'sword': 1, 'apple': 1}

inventory.update(more_loot)
print(inventory)

print(len(inventory))			# 3
print(sum(inventory.values()))	# 6