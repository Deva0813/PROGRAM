def salaiva(x):
    y = a * x + (b * x * x) + (c * x * x * x) + (d * x * x * x * x)
    return y


a = int(input())
b = int(input())
c = int(input())
d = int(input())


for i in range(10):
    moulee = int(input())
    print(f"Solution for given {moulee} is : ", salaiva(moulee))
    print("helllo")
