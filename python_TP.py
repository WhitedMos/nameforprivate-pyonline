import math
# Question 1: Donner le 10000eme nombre premier 2,3,5,7,11
# 问题1：给出第10000个质数
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_number(n):
    prime_list = []
    i = 2
    while len(prime_list) < n:
        if is_prime(i):
            prime_list.append(i)
        i += 1
    print(f"Le {n}eme nombre premier: {prime_list[n - 1]}\n")
    return prime_list

if __name__ == '__main__':
    print("Question 1:")
    prime_number(10000)

# Question 2: Afficher tous les a, b, c dans N3 <= 1000 tels que a^2 + b^2 = c^2
# 问题2：显示所有满足a^2 + b^2 = c^2的a、b、c在N3 <= 1000中
def pythagorean_triplet(n):
    abc_list = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer() and c <= n:
                abc_list.append([a, b, int(c)])
    print(f"Tous les [a, b, c] que a^2 + b^2 = c^2 dans N^3 <= {n}: {abc_list}\n")
    return abc_list

if __name__ == '__main__':
    print("Question 2:")
    pythagorean_triplet(1000)

# Question 3: Tous n dans N tels que u_(n+2) = (1/3)*((u_(n-1))^3 + u_n +1)
# u_0 = 0, u_1 = 1/2, u_10000 = ?
# 问题3：所有n在N中使得u_(n+2) = (1/3)*((u_(n-1))^3 + u_n +1)
# u_0 = 0, u_1 = 1/2, u_10000 = ?

def u_n(n, u1=0, u2=1/2):
    u_list = [u1, u2]
    for i in range(2, n + 1):
        u = (1/3)*((u_list[i - 2])**3 + u_list[i - 1] + 1)
        u_list.append(u)
    print(f"u_{n} = {u_list[n]}\n")
    return u_list

if __name__ == '__main__':
    print("Question 3:")
    u_n(10000)

# Question 4: Tous v dans N tels que v_(n+1) = v_n /2 si v_n est pair, 3*v_n + 1 si v_n est impair
# montre que pour v_0 = 13, il existe un p dans N tel que v_p = 1
# 问题4：所有v在N中使得v_(n+1) = v_n /2 si v_n是偶数, 3*v_n + 1 si v_n是奇数
# 证明对于v_0 = 13, 存在一个p在N中使得v_p = 1
def v_n(v0=13):
    v_list = [v0]
    while v_list[-1] != 1:
        if v_list[-1] % 2 == 0:
            v = v_list[-1] / 2
        else:
            v = 3*v_list[-1] + 1
        v_list.append(v)
    print(f"C'est vrai pour v_0 = {v0}, p = {len(v_list) - 1}\n")
    return v_list

if __name__ == '__main__':
    print("Question 4:")
    v_n(13)