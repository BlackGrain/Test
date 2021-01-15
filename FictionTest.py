def method(a, b):
    """
    :param b:
    :param a:
    :return:
    """
    print(f"a={a}")
    print(f"b={b}")


print("method(1, 2)")
method(1, 2)

print("method(b=3, a=2)")
method(b=3, a=2)


def method2(**c):
    print(c.keys())


method2(a=1, b=2, c=3)


def method3(*d):
    for a in d:
        print(a)


method3(1, 3, 4, 5, 6, 8)

print("-----------")


def method(*, a):
    print(a)


method(a=12)
print("--------------------------")

print(list(range(3, 6)))
list_a = (3, 6)
list(range(*list_a))

print("--------------------------")


def method(a, b, c):
    print(a)
    print(b)
    print(c)


dec = {"a": 1, "b": 2, "c": 3}
method(**dec)
print("-----------------")


def y1(x, y, z):
    return x + y + z


print(y1(1, 2, 3))
