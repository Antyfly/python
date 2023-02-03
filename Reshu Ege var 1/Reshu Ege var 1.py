# Task 2
# print("x,y,z,w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(((x<=y)==(z<=w)) or (x and w)):
#                     print(y,x)


# Task 5
# a = []
# for n in range(10,1000):
#     r = int(bin(n)[3:],2)
#     if n -r not in a:
#         a.append(n-r)
# print(len(a))


# Task 8
# import itertools
# alphabet = "МАТВЕЙ"
# ar = itertools.permutations(alphabet)
# arl = []
# for i in ar:
#     arl.append(list(i))
# count = 0
# for e in arl:
#     flag = True
#     for i in range(len(e) - 1):
#         if e[0] == 'Й' or (e[i] == 'А' and e[i + 1] == 'Е'):
#             flag = False
#     if flag == True: count += 1
# print(count)


# Task 12
# a = "9" * 1000
# while "999" in a or "888" in a:
#     if "888" in a:
#         a = a.replace('888', '9', 1)
#     else:
#         a = a.replace('999', '8', 1)
# print(a)


# Task 14
# count = 0
# a = 4 **2020 + 2**2017 - 15
# x = bin(a)[2:]
# x = str(x)
# for i in x:
#     if i == "1":
#         count +=1
# print(count)

# Task 15
# for a in range(300, 0, -1):
#     k = 0
#     for x in range(0, 300):
#         for y in range(0, 300):
#             if (2*x + 3*y < 30) or (x + y >= a):
#                 k += 1
#     if k == 90_000:
#         print(a)
#         break

# Task 16
# def f(n):
#     if n == 1:
#         return 1
#     if n>1:
#         return f(n-1)+n
# print(f(40))


# Task 19
# def f(x, y, h):
#     if h == 3 and x + y >= 69:
#         return 1
#     elif h == 3 and x + y < 69:
#         return 0
#     elif x + y >= 69 and h < 3:
#         return 0
#     else:
#         if h % 2 == 0:
#             return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1) or f(x * 3, y,
#                                                                                        h + 1)  # стратегия победителя
#         else:
#             return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1) or f(x * 3, y,
# for x in range(1, 59):
#     if f(x, 10, 1) == 1:
#         print("Задача 19:", x)
#         break

# Task 23
# def t23(start,finish):
#     if start>finish:
#         return 0
#     if start == finish:
#         return 1
#     if start<finish:
#         return t23(start+1, finish) + t23(start+2, finish) + t23(start*2, finish)
# print(t23(3,10) * t23(10,12))

# Task 24
# with open("24.txt") as f:
#     p = f.readline()
#     maxL = 0
#     curL = 0
#     for i in range(len(p)-1):
#         if p[i] == "X" and p[i+1] == "Z" and p[i+2] == "Z" and p[i+3] == "Y":
#             if maxL<curL:
#                 maxL = curL
#             curL = 3
#         else:
#             curL +=1
#         if  maxL < curL:
#             maxL = curL
# print(maxL)

# Task 25
def f1(x):
    while x % 2 == 0:
        x = x // 2
    if (x ** 0.25) == int(x ** 0.25):
        return True
    else:
        return False


def f(x):
    k = 2
    deliteli = set()
    if x % 2 != 0:
        deliteli.add(x)
    deliteli.add(1)
    while k * k <= x:
        if x % k == 0:
            if k % 2 != 0:
                deliteli.add(k)
            if x // k < x:
                if (x // k) % 2 != 0:
                    deliteli.add(x // k)
        k = k + 1
    return sorted(deliteli)
start = 45000000
end = 50000000
numbers = [int(x)
           for x in range(start, end + 1)
           if f1(x) == True]
for i in numbers:
    if len(f(i)) == 5:
        print(i)