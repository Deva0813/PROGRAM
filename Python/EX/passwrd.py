import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
sym = "!@#$%^&*"

all = lower + upper + num + sym
length = 10
passwd = "".join(random.sample(all, length))

print(passwd)
print("hello")
