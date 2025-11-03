#Permutation Without Using Built in function
def Permutate(a, size):
    if size == 1:
        print(tuple(a))
        return
    for i in range(size):
        Permutate(a, size - 1)
        if size % 2 == 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]

n=int(input("Enter Number of Elements: "))
s=list(map(int, input(f"Enter {n} elements separated by space: ").split()))
a = list(s)
Permutate(a, len(a))