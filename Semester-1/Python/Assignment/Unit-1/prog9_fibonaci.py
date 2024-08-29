n1 = 0
n2 = 1
number = int(input("Enter any number: "))

print("Fibonacci series:",end = " ")
# print("Fibonacci series up to", number, "terms:")

print(n1, end=" ")
print(n2, end=" ")

for x in range(2, number):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3