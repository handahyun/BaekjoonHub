int1 = int(input())
int2 = int(input())

# 5
num1 = int(int1 * (int2 % 10))
# 85-5
num2 = int((int1 * (int2 % 100 - int2 % 10) / 10))
# 385 - 85
num3 = int((int1 * (int2 % 1000 - int2 % 100) / 100))

result = int1 * int2

print(num1)
print(num2)
print(num3)
print(result)
