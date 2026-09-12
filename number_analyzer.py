n = int(input("Enter a number: "))
original = n

count = 0
digit_sum = 0
digit_product = 1
rev = 0

temp = n
while temp > 0:
    count += 1
    temp //= 10

temp = n
while temp > 0:
    d = temp % 10
    digit_sum += d
    digit_product *= d
    rev = rev * 10 + d
    temp //= 10

temp = n
divisors = 0
for i in range(1, n + 1):
    if n % i == 0:
        divisors += 1

if original % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"

if original == rev:
    palindrome = "Yes"
else:
    palindrome = "No"

arm = original
arm_total = 0
while arm > 0:
    d = arm % 10
    arm_total += d ** count
    arm //= 10

if arm_total == original:
    armstrong = "Yes"
else:
    armstrong = "No"

prime = "Yes"
if original < 2:
    prime = "No"
else:
    for i in range(2, original):
        if original % i == 0:
            prime = "No"
            break

print("Digits:", count)
print("Sum of Digits:", digit_sum)
print("Product of Digits:", digit_product)
print("Reverse:", rev)
print("Even/Odd:", even_odd)
print("Prime:", prime)
print("Palindrome:", palindrome)
print("Armstrong:", armstrong)
print("Divisors:", divisors)