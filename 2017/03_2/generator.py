def gen(a):
    print(a)
    b = yield(23)
    print(b)
    yield(34)
    yield(4)

asd = gen(15)
print("a", next(asd))
print("a", asd.send(444))
print("a", next(asd))