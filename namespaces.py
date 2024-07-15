def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function() # при вызове функции test_function внутри нее создастся функция inner_function и вызовется
# inner_function()  -> а если попытаться вызвать inner_function в глобальной области, то она не вызовется, потому что
#                      она даже не иницилизировалась