dict1 = {"a": 1, "b": 2}
dict2 = dict(a=1, b=2)
dict3 = dict([("a", 1), ("b", 2)])
print(dict1)
print(dict2)
print(dict3)

print(dict1.keys())
print(dict1.pop("a"))
print(dict1)
print("---------")
dict2 = dict1.fromkeys([1, 2, 3], "a")
print(dict1)
print(dict2)
print(":::::::")

print({i: i*i for i in range(9)})

print("+++++++++++++++")

dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

print("字典值 : %s" % dict.items())

# 遍历字典列表
for key, values in dict.items():
    print(key, values)
