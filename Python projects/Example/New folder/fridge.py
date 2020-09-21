import functools
class logged:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('you called {.__name__}({}{}{})'.format(func, str(list(args))[1:-1], ',' if kwargs else '',
                                                      ','.join('{}={}'.format(*pair) for pair in kwargs.items()), ))
        val = func(*args, **kwargs)
        print('it returned', val)

        return val