n = int(input("Enter a number: "))

temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
    
print(rev)

if n == rev:
    print(n, "is a palindrome number")
    
else:
    print(n, "is not a palindrome number")