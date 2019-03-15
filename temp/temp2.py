def foo():
    print('from foo')
    bar()
def bar():
    print('from bar')
    foo()
foo()
