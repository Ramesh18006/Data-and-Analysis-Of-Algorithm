#Implement Cominations from scratch (do not use inbuilt methods) ) - For any data type
def generate_combinations(data, r):
    def backtrack(start, current):
        if len(current) == r:
            print(tuple(current))  # or use a callback to collect
            return
        for i in range(start, len(data)):
            current.append(data[i])
            backtrack(i + 1, current)
            current.pop()  # backtrack

    backtrack(0, [])
data = ['A', 'B', 'C', 'D']
r = int(input("Enter number of ways to choose the element: "))
generate_combinations(data, r)
