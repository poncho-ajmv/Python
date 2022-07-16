def suma(*args, **kwargs):
    return kwargs, args

print(suma("argumentos", 10, 2, a="hola mundo", b =23, c=True, d=False, e=56))

