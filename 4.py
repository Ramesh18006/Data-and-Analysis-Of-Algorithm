dist = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 17],
    [15, 35, 0, 30, 28],
    [20, 25, 30, 0, 22],
    [25, 17, 28, 22, 0]
]

def generate_permutations(arr, start, result):
    if start == len(arr):
        result.append(arr[:])
    else:
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            generate_permutations(arr, start + 1, result)
            arr[start], arr[i] = arr[i], arr[start]  

cities = [1, 2, 3, 4]
all_routes = []
generate_permutations(cities, 0, all_routes)
min_cost = 999999
best_route = []

for route in all_routes:
    full_route = [0] + route + [0] 
    cost = 0
    for i in range(len(full_route) - 1):
        cost += dist[full_route[i]][full_route[i+1]]
    if cost < min_cost:
        min_cost = cost
        best_route = full_route

# Print result
names = ['A', 'B', 'C', 'D', 'E']
path = [names[i] for i in best_route]
print("Best route:", " -> ".join(path))
print("Total distance:", min_cost, "km")
