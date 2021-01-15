try:
    num1 = int(input("input a number:"))
    num2 = int(input("input a numder:"))
    print(num1 / num2)
except ZeroDivisionError:
    print("this is a except")
except ValueError:
    print("error")
else:
    print("none error")
finally:
    print("--------------------")


class MyException(Exception):
    def __int__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


raise MyException("错", "sb")



