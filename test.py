import random
a = "aaa"
b = "456"
c = "789"
print(a + b)
print("123" + "31232")
d = "1234{}{}"
print(d.format(a, c))
print(f"1234{a}{c}")

print("------------------")

a = random.randint(1, 100)
number = input("input your number:")
while True:
    number = int(number)
    if number == a:
        print("OK!")
        break
    elif number > a:
        number = input("too bigger,input your number:")
    elif number < a:
        number = input("too smaller,input your number:")
