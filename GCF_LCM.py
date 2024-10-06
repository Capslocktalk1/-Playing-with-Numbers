def gcdCalculate(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

gcd = gcdCalculate(num1, num2)
lcm = (num1*num2) / gcd

print("The GCD is: " , gcd)
print("The LCM is: " , lcm)