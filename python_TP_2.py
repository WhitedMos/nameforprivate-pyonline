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
x = input("x:")
y = input("y:")
max_input = max(x,y)
if max_input == x:
    print(1)
else:
    print(0)

print("2.3:")
if input("x:") >= input("y:"):
    print("maximal est x")
else:
    print("maximal est y")

print("2.4:")
if input("x:") >= input("y:"):
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

print(f"3.1: \n{tabulate(table, headers, tablefmt='grid')}")

print(f"xor(a,b):{xor(bool(input("bool a")), bool(input("bool b")))}")

# Exercice 4
print("\nExercice 4")
print("4.1:")
x = range(0, 10)
y = [*range(0, 10)]
z = [k for k in range(0, 10)]
print(x,"\t",type(x))
print(y,"\t", type(y))
print(z,"\t", type(z))
print(y == z)
print("4.2:")
y = [range(0, 10)]
print(y,"\t", type(y))
print(len(y))
print(y == z)
print("4.3:")
print([*range(0, input("n:"))])
print("4.4: if we got int(float(x)), it will give us x without the decimal part")
print("4.5:")
print([*range(0, 10, 2)])
