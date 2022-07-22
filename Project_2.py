# Made by Rachit Master

# Task - 1
# input from the user
n = int(input("Enter the number of times you want Fibonacci Numbers to loop: "))
a = 0
b = 1
sum = 0
count = 1
# while loop where it will run the amount of times specified by the user
while count <= n:
    print(sum)
    count += 1
    a = b
    b = sum
    sum = a + b

# Task - 2
# input from user and split it by ','
x = [int(x) for x in input("Enter the numbers you want the positives for separated by ',': ").split(",")]
# for loop where if the number is more or equal to 0 it prints it
for num in x:
    if num >= 0:
        print(num, end=" ")
