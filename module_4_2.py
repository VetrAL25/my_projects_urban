# Работающая версия:

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function ()
test_function()

# Неработающая версия:
#
# def test_function():
#     def inner_function():
#         print("Я в области видимости функции test_function")
#     inner_function ()
# test_function()
#     inner_function()

# И так тоже не работает:
#
# def test_function():
#     def inner_function():
#         print("Я в области видимости функции test_function")
#     inner_function ()
# test_function()
# inner_function()
