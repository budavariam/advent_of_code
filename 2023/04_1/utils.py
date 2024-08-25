from time import perf_counter

def profiler(method):
    def decorator_method(*arg, **kw):
        t = perf_counter()
        result = method(*arg, **kw)
        print(f"{method.__name__}: {perf_counter()-t:2.5f} sec")
        return result
    return decorator_method