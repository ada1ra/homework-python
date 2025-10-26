def curry(func, arity):
    if arity < 0:
        raise ValueError("Арность не может быть отрицательной")

    def curried(*args):
        if len(args) >= arity:
            return func(*args[:arity])
        else:
            def next_function(x):
                new_args = args + (x,)
                return curried(*new_args)

            return next_function

    return curried


def uncurry(curried_func, arity):
    if arity < 0:
        raise ValueError("Арность не может быть отрицательной")

    def uncurried(*args):
        if len(args) != arity:
            raise TypeError(f"Ожидается {arity} аргументов, получено {len(args)}")

        result = curried_func
        for arg in args:
            result = result(arg)
        return result

    return uncurried
