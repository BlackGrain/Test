import os

# os.mkdir("testdir")

# os.removedirs("testdir")

print(os.listdir("/"))
print(os.getcwd())

print(os.path.exists("b"))


if not os.path.exists("b"):
    os.mkdir("b")

if not os.path.exists("/base_python/1_StandardLib/d"):
    os.mkdir("d")

if not os.path.exists("b/test.txt"):
    f = open("b/test.txt", "w")
    f.write("hello world")
    f.close()

