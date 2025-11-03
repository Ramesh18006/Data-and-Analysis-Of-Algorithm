def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a = x // (10 ** m)
    b = x % (10 ** m)
    c = y // (10 ** m)
    d = y % (10 ** m)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    product = (ac * (10 ** (2 * m))) + (ad_bc * (10 ** m)) + bd
    return product
x = int(input("Enter The Number: "))
y = int(input("Enter The Number: "))
result = karatsuba(x, y)
print(f"{x} * {y} = {result}")