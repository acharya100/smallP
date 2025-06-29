credit_number = "0987-6543-2112-3410"

print(credit_number[0])
print(credit_number[7:])
print(credit_number[3:9])
print(credit_number[:8])
print(credit_number[-1:])
print(credit_number[-7:-1])
print(credit_number[1:9:3])
print(credit_number[:8:2])
print(credit_number[::2])
print(credit_number[1::2])



phone_number = "98104-98106-10728"

final_digits = phone_number[-5:]

print(f"Required final digits are XXXX-XXXX-{final_digits}")


print(phone_number[::-1])
print(phone_number[::-3])