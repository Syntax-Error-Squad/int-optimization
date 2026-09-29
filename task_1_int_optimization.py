def check(n):
    """Проверяет, берется ли целое число из кэша малых чисел.

    Значение n + 0 вычисляется во время выполнения. Если вернул 
    тот же объект, что и n, значит, число кэшировано.

    Parameters
    ----------
    n : int
        Проверяемое целое число.

    Returns
    -------
    bool
        True, если id(n) == id(n + 0), 
        иначе False.
    """
    x = n
    y = n + 0
    return id(x) == id(y)

n = 0
while check(n):
    n += 1
right = n - 1

n = -1
while check(n):
    n -= 1
left = n + 1

print(f"[{left}, {right}]")

