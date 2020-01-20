
# 将函数作为返回值


def foo():
    return hi


def my_decorator(f):
    def inner_func(*args, **kwargs):
        print('内部函数开始')
        f()
        print('内部函数结束')

    return inner_func


def hi(name='Jack'):
    print('Hi, {0}'.format(name))


@my_decorator
def hi2(name='Jack'):
    print('Hi, {0}'.format(name))


if __name__ == "__main__":
    # hi()

    # print(foo())

    # dd = my_decorator(hi)
    # print(dd())

    hi2('Mark')
