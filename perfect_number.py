num = int((input("Enter a number: ")))

divisor = 0

for i in range(1, num):
    if num % i == 0:
        divisor = divisor + i
        
if divisor == num:
    print (f"{num} is a perfect number.")

else:
    print(f"{num} is not a perfect number.")
