num = int(input("Enter an integer: "))
binary = bin(num)[2:]
print(f"Binary of {num} is {binary}")
pos = int(input("Enter the bit position to check : "))
if pos < 0 or pos >= len(binary):
    print("Invalid position!")
else:
    bit = binary[pos]
    print("True" if bit == '1' else "False")
