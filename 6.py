weights = [2, 3, 4, 5, 9, 7]
values  = [3, 4, 8, 8, 10, 6]
capacity = 15
n = len(weights)

max_value = 0
best_combo = []
def generate_combinations(index, current_combo):
    global max_value, best_combo
    if index == n:
        total_weight = sum(weights[i] for i in current_combo)
        total_value = sum(values[i] for i in current_combo)
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combo = current_combo[:]
        return
    current_combo.append(index)
    generate_combinations(index + 1, current_combo)
    current_combo.pop()
    generate_combinations(index + 1, current_combo)

generate_combinations(0, [])

print("Best item combination:", [i + 1 for i in best_combo]) 
print("Maximum value:", max_value)
