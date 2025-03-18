from tabulate import tabulate

def decorator(func):
    def wrapper(*args, **kwargs):
        print("-" * 20)
        result = func(*args, **kwargs)
        print("-" * 20)
        return result
    return wrapper

# Exercice 1
print("\nExercice 1")
x = True
y = int (x)
print(y)
print(f"1.1: {type(x)}, {type(y)}")

x = False
y = int (x)
print(y)
print(f"1.2: {type(x)}, {type(y)}")

print("1.3: Il convertit True en 1 et False en 0")

x = False
y = True
print(x + x)
print(x + y)
print(f"1.4: {type(x)}, {type(y)}")

print("1.5: Il convertit False en 0 et True en 1, puis fait l'addition")

# Exercice 2
print("\nExercice 2")
x = 2
y = 5
print(max(x, y))
print(min(x, y))
print("2.1: La commande max() renvoie le plus grand nombre, min() le plus petit")

print("2.2:")
x = input("x")
y = input("y")
max_input = max(x,y)
if max_input == x:
    print(1)
else:
    print(0)

print("2.3:")
if input("x") >= input("y"):
    print("maximal est x")
else:
    print("maximal est y")

print("2.4:")
if input("x") >= input("y"):
    print("minimal est y")
else:
    print("minimal est x")

# Exercice 3
print("\nExercice 3")

def xor(a, b):
    return a != b
headers = ["A", "B", "A xor B"]
table = [[True, True, xor(0, 0)],
        [True, False, xor(0, 1)],
        [False, True, xor(1, 0)],
        [False, False, xor(1, 1)]]

print(f"3.1: {tabulate(table, headers, tablefmt='grid')}")

