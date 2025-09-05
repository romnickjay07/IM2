num = int(input("Enter a number for multiplication table: "))

print(f"\nMultiplication Table of {num}\n")

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")