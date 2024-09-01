def test_func():
    a = 'Я test_func'
    print(a)
    def inner_func():
        a = 'Я в области видимости функции test_func'
        print(a)
    inner_func()
test_func()
#inner_func() - Данную функцию можно вызвать только внутри основной функции