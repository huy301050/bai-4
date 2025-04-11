def is_all_digits_even(num):
    for digit in str(num):
        if int(digit) % 2 != 0: 
            return False
    return True

result = []
for num in range(1000, 3001):
    if is_all_digits_even(num):
        result.append(str(num))

print(",".join(result))
print("Hoàng Nghĩa Huy")
print("MSSV:235752020710001")