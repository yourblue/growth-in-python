# coding:utf-8
import math

prime = [];
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # 在for循环正常执行完，不是通过break跳出的时候。就会执行else部分，else是for循环的一部分
        prime.append(i)
print(prime)


# def func_get_prime(n):
#     return filter(lambda x: not [x % i for i in range(2, int(math.sqrt(x)) + 1) if x % i == 0], range(2, n + 1))
#
#
# print(list(func_get_prime(100)))
