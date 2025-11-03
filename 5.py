
weights = [2, 3, 4, 5, 8, 7]
values =  [3, 4, 8, 9, 10, 6]
capacity = 15
n = len(weights)
max_value = 0
best_combo = []
for i in range(2 ** n):
    combo = bin(i)[2:].zfill(n)  
    total_weight = 0
    total_value = 0
    items = []

    for j in range(n):
        if combo[j] == '1': 
            total_weight += weights[j]
            total_value += values[j]
            items.append(j + 1) 

    if total_weight <= capacity and total_value > max_value:
        max_value = total_value
        best_combo = items

# Print result
print("Best item combination:", best_combo)
print("Maximum value:", max_value)
