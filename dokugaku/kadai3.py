# def f(x):
#     return x * 2
#
#
# f(2)
# result = f(2)
# print(result)
#
# def

# def f(x):
#     return x + 1
#
#
# z = f(4)
#
# if z == 5:
#     print("z=5")
# else:
#     print("z!=5")

# def f():
#     return 1 + 1
#
#
# result = f()
# print(result)
#
# def f(x, y, z):
#     return x + y + z
#
#
# result = f(1, 2, 3)
# print(result)
# def f():
#     z = 1 + 1
#
#
# result = f()
# print(result)
# print(float(100.01))
# age=input("enter your age:")
# int_age=int(age)
# if int_age<21:
#     print("you are young")
# else:
#     print("wow,you are old")
# def even_odd(x):
#     if x % 2 == 0:
#         print("even")
#     else:
#         print("odd")
#
#
# even_odd(2)
# even_odd(3)
#
# def even_odd():
#     n = input("type a number:")
#     n = int(n)
#     if n % 2 == 0:
#         print("even")
#     else:
#         print("odd")
#
#
# even_odd()
# even_odd()
# even_odd()
# def f(x=2):
#     return x ** x
#
#
# print(f())
# print(f(4))
#
# def add_it(x,y=10):
#     return x+y
# result=add_it(2)
# print(result)
# x = 1
# y = 2
# z = 3
#
#
# def f():
#     x=1
#
# print(x)

# x = 100


# def f():
#     global x
#     x += 1
#     print(x)
#
#
# f()
#

a=input("type a number:")
b=input("type a number:")
a=int(a)
b=int(b)
try:
    a = input("type a number:")
    b = input("type a number:")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError,ValueError):
    print("era-")


def f(x):
    return x**2
print(f(2))

def f(x):
    """

    :param x: string
    :return:
    """
    print(x)
f("aaa")

def f(x,y,z,a=1,b=2):
    """

    :param x: int
    :param y: int
    :param z: int
    :param a: int
    :param b: int
    :return: int
    """
    return x+y+z+a+b
print(f(2,2,2))

def f1(x):
    return x // 2


def f2(x):
    return x * 4


a = f1(10)
print(f2(a))
def f(x):
    """

    :param x: string
    :return: string convert to float
    """
    try:
        return float(x)
    except ValueError:
        return "era-"


print(f("a"))
