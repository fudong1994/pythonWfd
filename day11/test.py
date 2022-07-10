"""
@Time : 2022/7/10 0010  11:19
@File : test
@Project : pythonWfd
"""
a = 11


def pythontest01(a, b, c, d=10, *args, **kwargs):
    a = 10
    print(d)
    print(args, type(args))
    print(kwargs, type(kwargs))

    def pythontest02():
        nonlocal a
        print(a)

    pythontest02()


pythontest01(2, 3, 4, 5, 5, f=10)
