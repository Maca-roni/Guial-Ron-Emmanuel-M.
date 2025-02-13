n = int(input("Enter the number of terms: "))

first_num = 0
second_num = 1

print("Fibbonacci Series: ", end= "")
for i  in range(n):
    print(first_num, end= " ")
    next_num = first_num + second_num
    first_num = second_num
    second_num = next_num
