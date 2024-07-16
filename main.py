num = int(input("Введіть ціле число: "))
original_num = num

while num > 9:
    product = 1
    for digit in str(num):
        product *= int(digit)
    num = product

print(f"{original_num} -> {num}")