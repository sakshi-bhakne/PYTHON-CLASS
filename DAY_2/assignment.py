#Que1: print tables:

for i in range(1, 10, 2):
    j = 1
    while j <= 10:
        print(i, "*", j, "=", i * j)
        j += 1
    print()

#Que2: sum of digits:

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits:", sum)

#Que3: split:

a = [10, "Sakshi",20,30,"sujal",25,26,35,"sampada",]

numbers = []
names = []

for i in a:
    if type(i) == int:
        numbers.append(i)
    else:
        names.append(i)
print("Numbers:", numbers)
print("Names:", names)
print("Highest number:", max(numbers))


#Que4: print pyrimid:

n = 5
for i in range(1,n+1):
   spaces = n - i
   stars = 2 * i - 1
   print(""*spaces + "*"*stars)

#Que5:palindrome:

name = input("Enter a name: ")

if name == name[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome") 

