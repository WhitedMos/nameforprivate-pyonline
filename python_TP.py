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
    for i in range(2, n):
        if is_prime(i):
            prime_list.append(i)
    print(prime_list)
    return prime_list

if __name__ == '__main__':
    prime_number(10000)