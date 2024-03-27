# set = collection which is unordered, unindexed. no duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()
utensils.update(dishes)
print(utensils.difference(dishes))

dinner_table = utensils.union(dishes)

for x in utensils:
    print(x)
print()
for x in dinner_table:
    print(x)























